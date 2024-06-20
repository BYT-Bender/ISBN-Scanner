from ISBN2Details import ISBN2Details
import csv

File = "BookCollection.csv"
fields = ["ISBN-13", "Title", "Author", "Publisher", "Edition", "Description", "Pages", "Genre", "Language"]
My_Dict = []
# galat hai

with open(File, 'w') as CSVFile :
  MyWriter = csv.writer(CSVFile, fieldnames = fields)
  MyWriter.writeheader()
  MyWriter.writerows(My_Dict)
