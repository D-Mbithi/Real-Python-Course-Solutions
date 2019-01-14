import os
from PyPDF2 import  PdfFileReader, PdfFileWriter

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp11/practice_files'

current_path = os.getcwd()

input_file_name = os.path.join(path, 'ugly.pdf')

input_file = PdfFileReader(open(input_file_name, 'rb'))

output_PDF = PdfFileWriter()

output_file_name = os.path.join(current_path, 'output/ugly.pdf')

for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    if page_num % 2 == 0:
        page.rotateClockwise(90)
    output_PDF.addPage(page)
output_file = open(output_file_name, 'wb')
output_PDF.write(output_file)
output_file.close()


