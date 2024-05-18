import cv2
import numpy as np
import pytesseract

# Read input image
img = cv2.imread("hbh.webp")
 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# read haarcascade for number plate detection
cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
# Detect license number plates
plates = cascade.detectMultiScale(gray, 1.2, 5)

for (x,y,w,h) in plates:   
   cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
   gray_plates = gray[y:y+h, x:x+w]
   color_plates = img[y:y+h, x:x+w]

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

predicted_result = pytesseract.image_to_string(gray_plates, lang ='eng') 
print(predicted_result)

cv2.imwrite('Numberplate.jpg', gray_plates)
cv2.imshow('Number Plate', gray_plates)
cv2.imshow('Number Plate Image', gray)
cv2.waitKey(0)
