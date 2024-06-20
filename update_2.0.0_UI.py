import cv2
from pyzbar.pyzbar import decode
import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

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
        self.video_frame.pack()

        self.details_frame = ttk.LabelFrame(root, text="Book Details")
        self.details_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.details_text = tk.Text(self.details_frame, height=10)
        self.details_text.pack(fill="both", expand=True)

        self.quit_button = ttk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

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

                if barcode_type == "EAN13":
                    book_details = get_book_details(barcode_data)
                    if 'title' in book_details:
                        text = f"{book_details['title']} by {book_details['author']}"
                        self.show_book_details(book_details)
                    else:
                        text = "Book details not found"
                        messagebox.showwarning("Book Details", "Book details not found")
                else:
                    text = f"{barcode_data} ({barcode_type})"

                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_frame.imgtk = imgtk
            self.video_frame.configure(image=imgtk)

        self.root.after(10, self.update_frame)

    def show_book_details(self, book_details):
        self.details_text.delete(1.0, tk.END)
        for key, value in book_details.items():
            self.details_text.insert(tk.END, f"{key.capitalize()}: {value}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ISBNScanner(root)
    root.mainloop()
