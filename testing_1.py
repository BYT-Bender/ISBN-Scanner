import cv2
import numpy as np
from pyzbar.pyzbar import decode
import requests
from bs4 import BeautifulSoup

def get_book_details(isbn):
    url = f"https://isbnsearch.org/isbn/{isbn}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Book not found"}

    soup = BeautifulSoup(response.content, 'html.parser')

    book_info = soup.find('div', class_='bookinfo')

    if not book_info:
        return {"error": "Book info not found"}

    title = book_info.find('h1').text.strip() if book_info.find('h1') else "Title not found"

    isbn13_tag = book_info.find('p', text=lambda t: t and "ISBN-13:" in t)
    print(isbn13_tag)
    isbn13 = isbn13_tag.find('a').text.strip() if isbn13_tag else "ISBN-13 not found"

    isbn10_tag = book_info.find('p', text=lambda t: t and "ISBN-10:" in t)
    isbn10 = isbn10_tag.find('a').text.strip() if isbn10_tag else "ISBN-10 not found"

    author_tag = book_info.find('p', text=lambda t: t and "Author:" in t)
    author = author_tag.text.split(":")[1].strip() if author_tag else "Author not found"

    edition_tag = book_info.find('p', text=lambda t: t and "Edition:" in t)
    edition = edition_tag.text.split(":")[1].strip() if edition_tag else "Edition not found"

    binding_tag = book_info.find('p', text=lambda t: t and "Binding:" in t)
    binding = binding_tag.text.split(":")[1].strip() if binding_tag else "Binding not found"

    publisher_tag = book_info.find('p', text=lambda t: t and "Publisher:" in t)
    publisher = publisher_tag.text.split(":")[1].strip() if publisher_tag else "Publisher not found"

    published_tag = book_info.find('p', text=lambda t: t and "Published:" in t)
    published = published_tag.text.split(":")[1].strip() if published_tag else "Published not found"

    book_details = {
        "title": title,
        "isbn13": isbn13,
        "isbn10": isbn10,
        "author": author,
        "edition": edition,
        "binding": binding,
        "publisher": publisher,
        "published": published
    }

    return book_details

print(get_book_details("9781909531611"))

# def main():
#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("Error: Could not open webcam.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: Could not read frame.")
#             break

#         barcodes = decode(frame)

#         for barcode in barcodes:
#             (x, y, w, h) = barcode.rect
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#             barcode_data = barcode.data.decode('utf-8')
#             barcode_type = barcode.type

#             if barcode_type == "ISBN13" or barcode_type == "ISBN10":
#                 book_details = get_book_details(barcode_data)
#                 text = f"{book_details['title']} by {book_details['author']}"
#             else:
#                 text = f"{barcode_data} ({barcode_type})"

#             cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#             print(f"Decoded {barcode_type}: {barcode_data}")
#             if barcode_type == "ISBN13" or barcode_type == "ISBN10":
#                 print(book_details)

#         cv2.imshow('Barcode/ISBN Scanner', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
