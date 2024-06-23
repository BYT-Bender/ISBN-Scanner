import requests
import pandas as pd

ISBNList = []
titleList = []
authorsList = []
publisherList = []
publishedDateList = []
descriptionList = []
pageCountList = []
categoriesList = []
languageList = []

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
            
            ISBNList.append(ISBN)
            titleList.append(title)
            authorsList.append(authors)
            publisherList.append(publisher)
            publishedDateList.append(publishedDate)
            descriptionList.append(description)
            pageCountList.append(pageCount)
            categoriesList.append(categories)
            languageList.append(language)

            '''book_details = {
                "ISBN-13" : ISBN,
                "Title" : title,
                "Authors" : ', '.join(authors),
                "Publisher" : publisher,
                "Edition": publishedDate,
                "Description" : description,
                "Pages" : pageCount,
                "Genres" : ', '.join(categories),
                "Language" : language
            }'''
            #return book_details
    else:
        return None
    
df = pd.DataFrame(
    {"ISBN-13" : ISBNList,
     "Title" : titleList,
     "Authors" : authorsList,
     "Publisher" : publisherList,
     "Edition" : publishedDateList,
     "Description" : descriptionList,
     "Pages" : pageCountList,
     "Genres" : categoriesList,
     "Language" : languageList},
     index = [1,2,3,4,5,6,7,8,9])

ISBN2Details(9780136019701)
ISBN2Details(9780063279636)
ISBN2Details(9780312539566)

print(authorsList)
print("All okay.")
