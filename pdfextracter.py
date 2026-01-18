from PyPDF2 import *

# Add the path to your pdf here
reader = PdfReader("path_to_your.pdf")
writer = PdfWriter()

# Select the number of pages
for i in range(10, 138):
    writer.add_page(reader.pages[i])

with open("name of the file", "wb") as f:
    writer.write(f)