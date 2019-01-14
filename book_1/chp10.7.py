import os
import copy
from PyPDF2 import PdfFileReader, PdfFileWriter

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp11/practice_files'

input_file_name = os.path.join(path, 'Walrus.pdf')

input_file = PdfFileReader(open(input_file_name, 'rb'))

input_file.decrypt('IamtheWalrus')

output_PDF = PdfFileWriter()

new_input_file = copy.copy(input_file)

for page_num in range(0, new_input_file.getNumPages()):
    page = new_input_file.getPage(page_num)
    page.rotateClockwise(270)

    page_copy = copy.copy(page)
    upper_right = page.mediaBox.upperRight

    page.mediaBox.upperRight = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page)

    page_copy.mediaBox.upperLeft = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_copy)



output_file_name = os.path.join(path, 'Output/New Warlus.pdf')
output_file = open(output_file_name, 'wb')
output_PDF.write(output_file)
output_file.close()
