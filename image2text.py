import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("tmp/bw.jpg")
text = pytesseract.image_to_string(img)
print(text)