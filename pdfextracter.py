from PyPDF2 import *

# Add the path to your pdf here
reader = PdfReader("path_to_your.pdf")
writer = PdfWriter()

# Select the start and finishing pages
for i in range(10, 138):
    writer.add_page(reader.pages[i])

# Add the path you want to save it too 
with open("name of the file", "wb") as f:
    writer.write(f)