from PIL import Image
import pytesseract
import pyttsx3
from googletrans import Translator


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_="Screenshot 2024-07-27 212103.png"
img=Image.open(image_)

text=pytesseract.image_to_string(img)
with open('abc.txt',mode ='w') as file:      
                 file.write(text) 
print("The following is the extract text/n",text)
translator =Translator()
k=translator.translate(text,dest='german')
engine = pyttsx3.init() 

engine.say(k)                              
engine.runAndWait()
