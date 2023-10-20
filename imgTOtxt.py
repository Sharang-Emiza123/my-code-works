from PIL import Image
import pytesseract

# Path to the Tesseract executable (update this path if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Emiza\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Open an image using Pillow (PIL)
image_path = r"C:\Users\Emiza\OneDrive\Desktop\test1.jpg"  # Replace with the path to your image file
img = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)