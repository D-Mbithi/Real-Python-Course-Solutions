import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp11/practice_files'

cover_file_name = os.path.join(path, 'Emperor cover sheet.pdf')

cover_file = PdfFileReader(open(cover_file_name, 'rb'))

book_file_name = os.path.join(path, 'The Emperor.pdf')

book_file = PdfFileReader(open(book_file_name, 'rb'))

output_PDF = PdfFileWriter()

for page_num in range(0, cover_file.getNumPages()):
    page = cover_file.getPage(page_num)
    output_PDF.addPage(page)

for page_num in range(0, book_file.getNumPages()):
    page = book_file.getPage(page_num)
    output_PDF.addPage(page)

output_file_name = os.path.join(path, 'Output/The Covered Emporer.pdf')
output_file = open(output_file_name, 'wb')
output_PDF.write(output_file)
output_file.close()

