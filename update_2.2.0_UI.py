import csv
import cv2
from pyzbar.pyzbar import decode
import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import datetime

def get_book_details(ISBN):
    URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(ISBN)
    Response = requests.get(URL)
    if Response.status_code == 200:
        BookData = Response.json()
        if BookData["totalItems"] == 0:
            return None
        else:
            title = BookData["items"][0]["volumeInfo"]["title"]
            author = BookData["items"][0]["volumeInfo"]["authors"][0]
            publisher = BookData["items"][0]["volumeInfo"]["publisher"]
            publish_date = BookData["items"][0]["volumeInfo"]["publishedDate"]
            book_details = {"title": title, "author": author, "publisher": publisher, "publish_date": publish_date}
            return book_details
    else:
        return None

class ISBNScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("ISBN Scanner")
        self.root.geometry("800x600")

        self.video_frame = tk.Label(root)
        self.video_frame.pack(side=tk.LEFT, fill="both", expand=True)

        self.details_frame = ttk.LabelFrame(root, text="Book Details")
        self.details_frame.pack(side=tk.RIGHT, fill="both", expand=True, padx=10, pady=10)

        self.details_text = tk.Text(self.details_frame, height=10)
        self.details_text.pack(fill="both", expand=True)

        self.quit_button = ttk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10, side=tk.BOTTOM)

        self.status_label = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        self.process_box = tk.Listbox(self.details_frame, height=5, width=50)
        self.process_box.pack(side=tk.BOTTOM, fill="both", padx=10, pady=10)

        self.book_listbox = tk.Listbox(self.details_frame, height=10, width=40)
        self.book_listbox.pack(side=tk.RIGHT, fill="both", padx=10, pady=10)
        self.book_details = []
        self.scanned_books = []  # To store scanned book details
        self.load_scanned_books()  # Load previously scanned books

        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            barcodes = decode(frame)

            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                barcode_data = barcode.data.decode('utf-8')
                barcode_type = barcode.type

                text = f"{barcode_data} ({barcode_type})"

                if barcode_type == "EAN13":
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
                            self.save_scanned_books()  # Save scanned books to CSV
                        else:
                            self.update_status("Invalid barcode")
                            messagebox.showwarning("Book Details", "Book details not found")

                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_frame.imgtk = imgtk
            self.video_frame.configure(image=imgtk)

        self.root.after(10, self.update_frame)

    def show_book_details(self, isbn, book_details):
        self.details_text.delete(1.0, tk.END)
        self.details_text.insert(tk.END, f"Title: {book_details['title']}\n")
        self.details_text.insert(tk.END, f"Author: {book_details['author']}\n")
        self.details_text.insert(tk.END, f"Publisher: {book_details['publisher']}\n")
        self.details_text.insert(tk.END, f"Published Date: {book_details['publish_date']}\n")

        # Add to the listbox (show only ISBN and title)
        self.book_listbox.insert(tk.END, f"{isbn} - {book_details['title']}")

        # Update process box
        self.process_box.insert(tk.END, f"Scanned: {isbn} - {book_details['title']}")

    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.update_idletasks()

    def save_scanned_books(self):
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
                    self.book_listbox.insert(tk.END, f"{row['isbn']} - {row['title']}")
        except FileNotFoundError:
            pass  # File doesn't exist initially

if __name__ == "__main__":
    root = tk.Tk()
    app = ISBNScanner(root)
    root.mainloop()
