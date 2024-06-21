import csv
import os

def PushToCSV(ISBN_Dict)
    File = "BookCollection.csv"
    fields = ["ISBN-13", "Title", "Author", "Publisher", "Edition", "Description", "Pages", "Genre", "Language"]
    My_Dict = ISBN_Dict
    
    with open(File, 'w') as CSVFile :
        MyWriter = csv.writer(CSVFile, fieldnames = fields)
        
        if not(os.path.exists(File)):    # Headers WILL necessarily be present if the .csv file already exists.
            MyWriter.writeheader()
        else :
            continue
        
        MyWriter.writerows(My_Dict)
    
    CSVFile.close()
