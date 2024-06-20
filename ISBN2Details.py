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
            authors = BookData["items"][0]["volumeInfo"]["authors"]
            publisher = BookData["items"][0]["volumeInfo"]["publisher"]
            publishedDate = BookData["items"][0]["volumeInfo"]["publishedDate"]
            description = BookData["items"][0]["volumeInfo"]["description"]
            pageCount = BookData["items"][0]["volumeInfo"]["pageCount"]
            categories = BookData["items"][0]["volumeInfo"]["categories"]
            language = BookData["items"][0]["volumeInfo"]["language"]
            
            book_details = {
                "ISBN-13" : ISBN,
                "Title" : title,
                "Author" : authors[0],
                "Publisher" : publisher,
                "Edition": publishedDate,
                "Description" : description,
                "Pages" : pageCount,
                "Genre" : categories,
                "Language" : language
            }
            return book_details
    else:
        return None
