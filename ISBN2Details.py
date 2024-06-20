import requests

def ISBN2Details(ISBN):
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
