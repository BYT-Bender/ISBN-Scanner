import sys
import csv
import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame, QListWidget, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from PIL import Image
from datetime import datetime
import warnings


def get_book_details(ISBN):
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
            publish_date = volume_info.get("publishedDate", "N/A")
            book_details = {"title": title, "author": author, "publisher": publisher, "publish_date": publish_date}
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
                    continue  # Skip non-EAN13 barcodes

                text = f"{barcode_data} ({barcode_type})"

                if any(book['isbn'] == barcode_data for book in self.scanned_books):
                    self.update_status("Entry already exists")
                else:
                    book_details = get_book_details(barcode_data)
                    if book_details:
                        self.show_book_details(barcode_data, book_details)
                        self.scanned_books.append({
                            'isbn': barcode_data,
                            'details': book_details,
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                        self.save_scanned_books()
                    else:
                        self.update_status("Invalid barcode")

                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            img = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            pix = QPixmap.fromImage(img)
            self.video_label.setPixmap(pix)

    def show_book_details(self, isbn, book_details):
        self.details_text.clear()
        self.details_text.append(f"Title: {book_details['title']}")
        self.details_text.append(f"Author: {book_details['author']}")
        self.details_text.append(f"Publisher: {book_details['publisher']}")
        self.details_text.append(f"Published Date: {book_details['publish_date']}")

        self.book_list.addItem(f"{isbn} - {book_details['title']}")
        self.process_list.addItem(f"Scanned: {isbn} - {book_details['title']}")

    def update_status(self, message):
        self.status_label.setText(message)

    def save_scanned_books(self):
        try:
            with open('scanned_books.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['isbn', 'title', 'author', 'publisher', 'publish_date', 'timestamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for book in self.scanned_books:
                    writer.writerow({
                        'isbn': book['isbn'],
                        'title': book['details']['title'],
                        'author': book['details']['author'],
                        'publisher': book['details']['publisher'],
                        'publish_date': book['details']['publish_date'],
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
                            'title': row['title'],
                            'author': row['author'],
                            'publisher': row['publisher'],
                            'publish_date': row['publish_date']
                        },
                        'timestamp': row['timestamp']
                    })
                    self.book_list.addItem(f"{row['isbn']} - {row['title']}")
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error loading scanned books: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scanner = ISBNScanner()
    scanner.show()
    sys.exit(app.exec_())
