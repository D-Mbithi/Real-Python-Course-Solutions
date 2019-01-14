import os
from PyPDF2 import PdfFileReader

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp11/practice_files'

input_file_name = os.path.join(path, "Pride and Prejudice.pdf")

input_file = PdfFileReader(open(input_file_name, 'rb'))

print('Number of pages', input_file.getNumPages())

print('Title:', input_file.getDocumentInfo().title)

print(input_file.getDocumentInfo())

print(input_file.getPage(0).extractText())

