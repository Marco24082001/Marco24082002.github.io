import cv2
import numpy as np 

def crop_Plate(img):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 125, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)                                    
    listcons = []
    for cnt in contours:
        listcons.append(cv2.contourArea(cnt))
    listcons.sort(reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        if  cv2.contourArea(cnt)==listcons[1] :
            cv2.rectangle(img, (x,y), (x+w,y+h), (223,0,41), 2)
            crop_img = img[y:y+h, x:x+w]
    return crop_img

def crop_Number(img):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=cv2.contourArea,reverse=True)
    num = 0
    for contour in contours:
        area =cv2.contourArea(contour)
        if area <= 4000 and area >= 900:
            x,y,w,h = cv2.boundingRect(contour)
            number = img[y:y+h, x:x+w]
            img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.imwrite('./number/Num_{}.png'.format(num), number)
            num += 1

img = cv2.imread('./image/1.jpg')
crop_plate = crop_Plate(img)
crop_Number(crop_plate)
cv2.imshow('crop', crop_plate)
cv2.imwrite('./number/crop.png',crop_plate)
cv2.waitKey(5000)


