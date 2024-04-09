import pytesseract
from PIL import Image

archivo = Image.open("jpg/texto.jpg")
print(pytesseract.image_to_string(archivo))
