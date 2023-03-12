import PyPDF2

my_file = open('US_Declaration.pdf', mode='rb')

# -------------- reading a PDF file -------------- #
pdf_reader = PyPDF2.PdfReader(my_file)

# getting hold of first page
page_one = pdf_reader.pages[0]
my_text = page_one.extract_text()

# printing page one
# print(my_text)
my_file.close()

# ----------------- Writing a PDF file ----------------- #
f = open('US_Declaration.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)

# getting hold of page one
first_page = pdf_reader.pages[0]

# creating a writer object
pdf_writer = PyPDF2.PdfWriter()

# storing what to write in writer object
pdf_writer.add_page(first_page)

# creating new PDF
pdf_output = open('MY_BRAND_NEW_PDF.pdf', 'wb')

# writing what we stored into pdf_output
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()

# checking if the operation is successful
brand_new = open('MY_BRAND_NEW_PDF.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(brand_new)
# print(len(pdf_reader.pages))


# ----------------- Writing all contents of a PDF to another PDF ----------------- #
f = open('US_Declaration.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)

# an empty list to store contents of a page from PDF
pdf_text = []

# looping all pages in PDF
for p in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[p]
    pdf_text.append(page.extract_text())
f.close()

print(type(pdf_text))