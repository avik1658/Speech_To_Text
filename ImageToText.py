import pytesseract
from PIL import Image

# Path to your image file
img_file_path = "/home/bs-00594/Downloads/quote2.jpg"

# Open the image using PIL
image = Image.open(img_file_path)

# Extract text from image
extracted_text = pytesseract.image_to_string(image)

# Print extracted text
print(extracted_text)
