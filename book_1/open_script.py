import os

from PyPDF2 import PdfFileReader, PdfFileWriter

path  = '/home/dennis/Desktop/All/Real Python Course/book1/chp11/practice_files'

input_file_name = os.path.join(path, 'The Whistling Gypsy.pdf')

input_file = PdfFileReader(open(input_file_name, 'rb'))

# get the title of the book, the author and number of pages
print('Title:', input_file.getDocumentInfo().title)

print('Author:', input_file.getDocumentInfo().author)

print('Number of pages:', input_file.getNumPages())

# extract all the text information in the pdf

text = ""

for page_num in range(input_file.getNumPages()):
    text = text + input_file.getPage(page_num).extractText()

print(text)

# create a new pdf file without cover page
current_path = os.getcwd()

output_file_name = os.path.join(current_path, 'output/New The Whistling Gypsy.pdf')

output_pdf = PdfFileWriter()

for page_num in range(1, input_file.getNumPages()):
    output_pdf.addPage(input_file.getPage(page_num))
    output_file = open(output_file_name, 'wb')
    output_pdf.write(output_file)

output_file.close()
