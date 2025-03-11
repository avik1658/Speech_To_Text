from pdf2image import convert_from_path
import pytesseract

# Path to your PDF file
pdf_file_path = "/home/bs-00594/Downloads/testPdf.pdf"

# Convert PDF to images
images = convert_from_path(pdf_file_path)

# Extract text from images
extracted_text = ""
for img in images:
    extracted_text += pytesseract.image_to_string(img) + "\n"

# Print or save the extracted text
print(extracted_text)

