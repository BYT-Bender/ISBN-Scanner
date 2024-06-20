import requests

def ISBN2Details(ISBN):
    URL = "https://www.googleapis/com/books/v1/volumes?q=isbn:" + str(ISBN)
    Response = requests.get(URL)
    if Response.status_code == 200:
        BookData = Response.json()
        if BookData["totalItems"] == 0:
            return None
        else :
            Title = BookData["items"][0]["volumeInfo"]["title"]
            Author = BookData["items"][0]["volumeInfo"]["title"][0]    #First author is the main one.
            Publisher = BookData["items"][0]["volumeInfo"]["publisher"]
            Publish_Date = BookData["items"][0]["volumeInfo"]["publishedDate"]
            Details_Dict = {"Title" : Title, "Author" : Author, "Publisher" : Publisher, "Publish_Date" : Publish_Date}
            return Details_Dict
