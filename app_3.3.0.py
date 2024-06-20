import sys
import csv
import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame, QListWidget, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from datetime import datetime
import winsound


def ISBN2Details(ISBN):
    URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(ISBN)
    try:
        Response = requests.get(URL)
        Response.raise_for_status()
        BookData = Response.json()
        if BookData["totalItems"] == 0:
            return None
        else:
            volume_info = BookData["items"][0]["volumeInfo"]
            title = volume_info.get("title", "N/A")
            authors = volume_info.get("authors", ["N/A"])
            author = authors[0] if authors else "N/A"
            publisher = volume_info.get("publisher", "N/A")
            publishedDate = volume_info.get("publishedDate", "N/A")
            description = volume_info.get("description", "N/A")
            pageCount = volume_info.get("pageCount", "N/A")
            categories = volume_info.get("categories", ["N/A"])
            category = categories[0] if categories else "N/A"
            language = volume_info.get("language", "N/A")
            
            book_details = {
                "ISBN-13": ISBN,
                "Title": title,
                "Author": author,
                "Publisher": publisher,
                "Edition": publishedDate,
                "Description": description,
                "Pages": pageCount,
                "Genre": category,
                "Language": language
            }
            return book_details
    except requests.exceptions.RequestException as e:
        print(f"Error fetching book details: {e}")
        return None


class ISBNScanner(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ISBN Scanner")
        self.setGeometry(100, 100, 1000, 600)

        self.video_label = QLabel(self)
        self.video_label.setFixedSize(640, 480)

        self.details_text = QTextEdit(self)
        self.details_text.setReadOnly(True)

        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.close)

        self.status_label = QLabel("Ready", self)
        self.status_label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.status_label.setAlignment(Qt.AlignLeft)

        self.process_list = QListWidget(self)
        self.book_list = QListWidget(self)
        self.book_list.itemClicked.connect(self.display_selected_book_details_wrapper)

        self.layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()

        self.left_layout.addWidget(self.video_label)
        self.left_layout.addWidget(self.status_label)

        self.right_layout.addWidget(self.details_text)
        self.right_layout.addWidget(self.book_list)
        self.right_layout.addWidget(self.process_list)
        self.right_layout.addWidget(self.quit_button)

        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(self.right_layout)
        self.setLayout(self.layout)

        self.scanned_books = []
        self.load_scanned_books()

        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

    def decode_barcodes(self, frame):
        try:
            return decode(frame, symbols=[ZBarSymbol.EAN13])
        except Exception as e:
            print(f"Error decoding barcodes: {e}")
            return []

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            barcodes = self.decode_barcodes(frame)

            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                barcode_data = barcode.data.decode('utf-8')
                barcode_type = barcode.type

                if barcode_type != "EAN13":
                    continue

                text = f"{barcode_data} ({barcode_type})"

                if any(book['isbn'] == barcode_data for book in self.scanned_books):
                    self.update_status("Entry already exists")
                    # self.display_selected_book_details(barcode_data)
                    self.play_sound("status_change")
                else:
                    book_details = ISBN2Details(barcode_data)
                    if book_details:
                        self.show_book_details(barcode_data, book_details)
                        self.scanned_books.append({
                            'isbn': barcode_data,
                            'details': book_details,
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                        self.save_scanned_books()
                        self.play_sound("scan_success")
                    else:
                        self.update_status("Invalid barcode")
                        self.play_sound("scan_error")

                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            img = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            pix = QPixmap.fromImage(img)
            self.video_label.setPixmap(pix)

    def show_book_details(self, isbn, book_details):
        self.details_text.clear()
        self.details_text.append(f"Title: {book_details['Title']}")
        self.details_text.append(f"Author: {book_details['Author']}")
        self.details_text.append(f"Publisher: {book_details['Publisher']}")
        self.details_text.append(f"Published Date: {book_details['Edition']}")
        self.details_text.append(f"Description: {book_details['Description']}")
        self.details_text.append(f"Pages: {book_details['Pages']}")
        self.details_text.append(f"Genre: {book_details['Genre']}")
        self.details_text.append(f"Language: {book_details['Language']}")

        self.book_list.addItem(f"{isbn} - {book_details['Title']}")
        self.process_list.addItem(f"Scanned: {isbn} - {book_details['Title']}")

    def display_selected_book_details(self, isbn):
        book = next((book for book in self.scanned_books if book['isbn'] == isbn), None)
        if book:
            self.details_text.clear()
            self.details_text.append(f"Title: {book['details']['Title']}")
            self.details_text.append(f"Author: {book['details']['Author']}")
            self.details_text.append(f"Publisher: {book['details']['Publisher']}")
            self.details_text.append(f"Published Date: {book['details']['Edition']}")
            self.details_text.append(f"Description: {book['details']['Description']}")
            self.details_text.append(f"Pages: {book['details']['Pages']}")
            self.details_text.append(f"Genre: {book['details']['Genre']}")
            self.details_text.append(f"Language: {book['details']['Language']}")

    def update_status(self, message):
        self.status_label.setText(message)

    def save_scanned_books(self):
        try:
            with open('scanned_books.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['isbn', 'title', 'author', 'publisher', 'publish_date', 'description', 'pages', 'genre', 'language', 'timestamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for book in self.scanned_books:
                    writer.writerow({
                        'isbn': book['isbn'],
                        'title': book['details']['Title'],
                        'author': book['details']['Author'],
                        'publisher': book['details']['Publisher'],
                        'publish_date': book['details']['Edition'],
                        'description': book['details']['Description'],
                        'pages': book['details']['Pages'],
                        'genre': book['details']['Genre'],
                        'language': book['details']['Language'],
                        'timestamp': book['timestamp']
                    })
        except IOError as e:
            print(f"Error saving scanned books: {e}")

    def load_scanned_books(self):
        try:
            with open('scanned_books.csv', 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.scanned_books.append({
                        'isbn': row['isbn'],
                        'details': {
                            'Title': row['title'],
                            'Author': row['author'],
                            'Publisher': row['publisher'],
                            'Edition': row['publish_date'],
                            'Description': row['description'],
                            'Pages': row['pages'],
                            'Genre': row['genre'],
                            'Language': row['language']
                        },
                        'timestamp': row['timestamp']
                    })
                    self.book_list.addItem(f"{row['isbn']} - {row['title']}")
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error loading scanned books: {e}")

    def display_selected_book_details_wrapper(self, item):
        isbn = item.text().split(' - ')[0]
        self.display_selected_book_details(isbn)

    def play_sound(self, sound_type):
        if sound_type == "scan_success":
            winsound.Beep(1000, 200)
        elif sound_type == "scan_error":
            winsound.Beep(500, 400)
        elif sound_type == "status_change":
            winsound.Beep(800, 300)
        else:
            print(f"Unknown sound type: {sound_type}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scanner = ISBNScanner()
    scanner.show()
    sys.exit(app.exec_())
