import os
from PyPDF2 import PdfFileReader

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp11/practice_files'

input_file_name = os.path.join(path, 'half and half.pdf')

input_file = PdfFileReader(open(input_file_name, 'rb'))

page = input_file.getPage(0)

print('Document cordinates', page.mediaBox)

print('Document Top Right Corner:', page.mediaBox.upperRight)
print('Document Bottom Right Corner:', page.mediaBox.lowerRight)
print('Document Top Left Corner:', page.mediaBox.upperLeft)
print('Document Bottom Left Corner:', page.mediaBox.lowerLeft)
