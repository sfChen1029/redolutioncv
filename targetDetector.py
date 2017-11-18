import cv2
import numpy as np
import math
from Target import Target
global camera
camera = cv2.VideoCapture(0)
global targetFound
targetFound = False
target = Target()
#outputs livefeed image
def getImage():
	global camera
	ret, image = camera.read()
	return image

#outputs angle of three points
def getContour(image):
	img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	#thresholding
	THRESHOLD_MIN = np.array([70,0,0],np.uint8)
	THRESHOLD_MAX = np.array([90,255,100],np.uint8)

	threshed_img = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)

	cv2.imshow("threshed", threshed_img)
	#cv2.waitKey(0)

	#contours
	_, contours, _ = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for cont in contours: #for each contour
		epsilon = 0.02*cv2.arcLength(cont,True)
		approx = cv2.approxPolyDP(cont, epsilon, True)
		if (cv2.contourArea(approx) > 75 and len(approx) == 4): #the contour should be reasonably large and have 4 corners
			global targetFound
			targetFound = True
			cv2.drawContours(image,[approx],-1, (255,255,255), 10)
			return approx
while True:
	image = getImage() #get image from live feed
	global targetFound
	targetFound = False
	contours = getContour(image)
	cv2.imshow("hi",image)
	if targetFound:
		target.firstImage(contours)
		print(target.getOrientation1())

	key = cv2.waitKey(10)
	if key == 27:
		cv2.destroyAllWindows()
		break
