import os
import PyPDF2


# Set the path to the PDF file, the password, and the output folder
pdf_path = "<locked_pdf_path>"
pdf_password = "<pdf_password_here>"
output_folder = os.path.expanduser("~\\Desktop\\PDF_Screenshots")

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


pdf_file = open(pdf_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

if pdf_reader.is_encrypted:
    pdf_reader.decrypt(pdf_password)  # Replace 'password' with the actual password for the PDF file

pdf_writer = PyPDF2.PdfWriter()

for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

new_pdf_file = open('unprotected.pdf', 'wb')
pdf_writer.write(new_pdf_file)

pdf_file.close()
new_pdf_file.close()



