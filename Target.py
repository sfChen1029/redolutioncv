import cv2
import math

class Target:

	def firstImage(self, approx):
		maxX = approx[0][0][0] 
		minX = 200000.0
		maxY = 0.0
		minY = 200000.0

		for i in approx:
			if (i[0][0] > maxX):
				#global maxX
				maxX = i[0][0]
			elif i[0][0]<minX:
				#global minX
				minX = i[0][0]
			if i[0][1]>maxY:
				#global maxY
				maxY = i[0][1]
			elif i[0][1]<minY:
				#global minY
				minY = i[0][1]
		self.width1 = maxX - minX
		self.height1 = maxY - minY
	def secondImage(self, approx):
		maxX = approx[0][0][0]
		minX = 200000.0
		maxY = 0.0
		minY = 200000.0

		for i in approx:
			if (i[0][0] > maxX):
				maxX = i[0][0]
			elif i[0][0]<minX:
				minX = i[0][0]
			if i[0][1]>maxY:
				maxY = i[0][1]
			elif i[0][1]<minY:
				minY = i[0][1]
		self.width2 = maxX - minX
		self.height2 = maxY - minY
	def getOrientation1(self):
		orientation1 = "NONE"
		if self.width1 > self.height1:
			orientation1 = "HORIZONTAL"
		elif self.height1 > self.width1:
			orientation1 = "VERTICAL"
		else:
			orientation = "SPINNING"
		return orientation1
	def getOrientation2(self):
		orientation2 = "NONE"
		if self.width2 > self.height2:
			orientation2 = "HORIZONTAL"
		elif self.height2 > self.width2:
			orientation2 = "VERTICAL"
		else:
			orientation2 = "SPINNING"
		return orientation2
	def finalOrientation(self):
		orientationfin = "NONE"
		if orientation1 == orientation2:
			return orientation1
		else:
			return "SPINNING"
