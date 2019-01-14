import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = '/home/dennis/Desktop/All/Real Python Course/book1/chp11/practice_files'

input_file_name = os.path.join(path, "The Emperor.pdf")

input_file = PdfFileReader(open(input_file_name, 'rb'))

output_PDF = PdfFileWriter()

watermark_file_name = os.path.join(path, "top secret.pdf")

watermark_file = PdfFileReader(open(watermark_file_name, 'rb'))

for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    page.mergePage(watermark_file.getPage(0))
    output_PDF.addPage(page)

output_PDF.encrypt("good2Bking")
output_file_name = os.path.join(path, 'Output/New Suit.pdf')
output_file = open(output_file_name, 'wb')
output_PDF.write(output_file)
output_file.close()
