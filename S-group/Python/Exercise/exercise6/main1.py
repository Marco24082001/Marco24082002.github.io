import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread('./image/2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 1)

contours, hierarchy = cv2.findContours(thresh,1,2)
largest_rectangle = [0,0]
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        area = cv2.contourArea(cnt)
        if area > largest_rectangle[0]:
            largest_rectangle = [cv2.contourArea(cnt), cnt, approx]

x,y,w,h = cv2.boundingRect(largest_rectangle[1])
image = img[y:y+h, x:x+w]

# cv2.imshow('origin', thresh)
# cv2.imshow('odsdf', img)
# cv2.imshow('bien so xe', image)
pytesseract.pytesseract.tesseract_cmd = '   '
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
# invert = 255 - opening
# data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
# print("THONG TIN NHAN DIEN:")
# print(data)
contours, hierarchy = cv2.findContours(thresh,1,2)
cv2.drawContours(image=image, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA)

crop_img = None
listcons = []
for cnt in contours:
    listcons.append(cv2.contourArea(cnt))
listcons.sort(reverse=True)
for cnt in contours:
    (x,y,w,h) = cv2.boundingRect(cnt)
    if  cv2.contourArea(cnt)==listcons[0] :
        cv2.rectangle(image, (x,y), (x+w,y+h), (223,0,41), 2)
        crop_img = image[y:y+h, x:x+w]



image = image[y:y+h, x:x+w]

cv2.imshow('crop', opening)
cv2.imshow('cro1p', crop_img)
cv2.waitKey()   
cv2.destroyAllWindows()