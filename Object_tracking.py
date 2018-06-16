import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1) :
	
	#take each frame
	_, frame = cap.read()

	#Convert BGR to HSV
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	#define range of blue color in hsv
	lower_blue = np.array([100,100,100])
	upper_blue = np.array([150,255,255])

	#Threshold the HSV image to get only blue colors 
	mask = cv2.inRange(hsv,lower_blue,upper_blue)

	#Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame,mask = mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	k = cv2.waitKey(5) & 0xFF
	if k == 27 :
		break

cv2.destroyAllWindows()

#green = np.uint8([[[0,255,0 ]]])
#hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
#print hsv_green
#[[[ 60 255 255]]]
#Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and 
#upper bound respectively.