from PyPDF2 import *

reader = PdfReader("path_to_your.pdf")
writer = PdfWriter()

for i in range(10, 138):
    writer.add_page(reader.pages[i])

with open("name of the file", "wb") as f:
    writer.write(f)