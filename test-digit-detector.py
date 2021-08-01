import cv2
import pytesseract

img = cv2.imread('0.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#custom_config = r'--oem 3 --psm 6'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#pytesseract.image_to_string(img, config=custom_config)
print (pytesseract.image_to_string(img))
cv2.imshow('Result',img)
cv2.waitKey(0)