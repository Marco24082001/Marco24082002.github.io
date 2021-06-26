import numpy as np
import cv2 
image = cv2.imread("image.png", 1)
def grayScale(img):
    # img[:] = np.sum(img,axis=-1,keepdims=1)/3
    formula = [0.07, 0.72, 0.21]
    img = np.dot(img, formula).astype(np.uint8)
    return img

def Black_White(img):
    img = np.where(img < 95, img, 255)
    img = np.where(img >= 95, img, 0)
    return img


cv2.imshow("Origin", image)
cv2.imshow("Grayscale", grayScale(image))
cv2.imshow("Black & White", Black_White(grayScale(image)))

cv2.waitKey(10000)  
hist = np.zeros((256), np.uint8)
[a, b] = image.shape[:2]
print(a)
print(b)
print(image[100][15])
hist[(2,4)] += 1
print(hist)