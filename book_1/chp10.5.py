import os
import copy
from PyPDF2 import  PdfFileReader, PdfFileWriter

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp11/practice_files'

input_file_name = os.path.join(path, 'half and half.pdf')

input_file = PdfFileReader(open(input_file_name, 'rb'))

output_PDF = PdfFileWriter()

for page_num in range(input_file.getNumPages()):
    page_left = input_file.getPage(page_num)
    page_right = copy.copy(page_left)
    upper_right = page_left.mediaBox.upperRight
    page_left.mediaBox.upperRight = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_left)
    page_right.mediaBox.upperLeft = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_right)

output_file_name = os.path.join(path, 'Output/the little mermaid.pdf')
output_file = open(output_file_name, 'wb')
output_PDF.write(output_file)
output_file.close()
