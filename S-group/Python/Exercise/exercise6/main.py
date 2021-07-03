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



# img = cv2.imread('./image/2.jpg')
# imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, bw = cv2.threshold(imgray, 125, 255, cv2.THRESH_BINARY_INV)
# contours, hierarchy = cv2.findContours(image=bw, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)                                    
# cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA)
# crop_img = None
# cv2.imshow('3', img)
# listcons = []
# for cnt in contours:
#     listcons.append(cv2.contourArea(cnt))
# listcons.sort(reverse=True)
# for cnt in contours:
#     (x,y,w,h) = cv2.boundingRect(cnt)
#     if  cv2.contourArea(cnt)==listcons[2] :
#         cv2.rectangle(img, (x,y), (x+w,y+h), (223,0,41), 2)
#         crop_img = img[y:y+h, x:x+w]    
# s = np.array(contours)
# print(s.shape)
# cv2.imshow('origin', img)
# cv2.imshow('bw', bw)
# # cv2.imshow('crop_img', crop_img)
# cv2.waitKey()


# import cv2
# import numpy


# #initial function for the callin of the trackbar
# def hello(x):
# 	#only for referece
# 	print("")

# #initialisation of the camera
# cap = cv2.VideoCapture(0)
# bars = cv2.namedWindow("bars")

# cv2.createTrackbar("upper_hue","bars",110,180,hello)
# cv2.createTrackbar("upper_saturation","bars",255, 255, hello)
# cv2.createTrackbar("upper_value","bars",255, 255, hello)
# cv2.createTrackbar("lower_hue","bars",68,180, hello)
# cv2.createTrackbar("lower_saturation","bars",55, 255, hello)
# cv2.createTrackbar("lower_value","bars",54, 255, hello)

# #Capturing the initial frame for creation of background
# while True:
# 	cv2.waitKey(1000)
# 	ret,init_frame = cap.read()
# 	#check if the frame is returned then brake
# 	if ret:
# 		break

# # Start capturing the frames for actual magic!!
# while True:
# 	ret,frame = cap.read()
# 	inspect = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# 	#getting the HSV values for masking the cloak
# 	upper_hue = cv2.getTrackbarPos("upper_hue", "bars")
# 	upper_saturation = cv2.getTrackbarPos("upper_saturation", "bars")
# 	upper_value = cv2.getTrackbarPos("upper_value", "bars")
# 	lower_value = cv2.getTrackbarPos("lower_value","bars")
# 	lower_hue = cv2.getTrackbarPos("lower_hue","bars")
# 	lower_saturation = cv2.getTrackbarPos("lower_saturation","bars")

# 	#Kernel to be used for dilation
# 	kernel = numpy.ones((3,3),numpy.uint8)

# 	upper_hsv = numpy.array([upper_hue,upper_saturation,upper_value])
# 	lower_hsv = numpy.array([lower_hue,lower_saturation,lower_value])

# 	mask = cv2.inRange(inspect, lower_hsv, upper_hsv)
# 	mask = cv2.medianBlur(mask,3)
# 	mask_inv = 255-mask 
# 	mask = cv2.dilate(mask,kernel,5)
	
# 	#The mixing of frames in a combination to achieve the required frame
# 	b = frame[:,:,0]
# 	g = frame[:,:,1]
# 	r = frame[:,:,2]
# 	b = cv2.bitwise_and(mask_inv, b)
# 	g = cv2.bitwise_and(mask_inv, g)
# 	r = cv2.bitwise_and(mask_inv, r)
# 	frame_inv = cv2.merge((b,g,r))

# 	b = init_frame[:,:,0]
# 	g = init_frame[:,:,1]
# 	r = init_frame[:,:,2]
# 	b = cv2.bitwise_and(b,mask)
# 	g = cv2.bitwise_and(g,mask)
# 	r = cv2.bitwise_and(r,mask)
# 	blanket_area = cv2.merge((b,g,r))

# 	final = cv2.bitwise_or(frame_inv, blanket_area)

# 	cv2.imshow("Harry's Cloak",final)

# 	if cv2.waitKey(3) == ord('q'):
# 		break

# cv2.destroyAllWindows()
# cap.release()
