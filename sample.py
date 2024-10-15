from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_="Screenshot 2024-07-27 212103.png"
img=Image.open(image_)

text=pytesseract.image_to_string(img)
print("The following is the extract text/n",text)