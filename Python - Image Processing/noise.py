import cv2
import numpy as np
 
# Read image
img = cv2.imread("capture.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   
rows,cols = gray.shape

for i in range(0,rows):
	for j in range(0,cols):
		if (gray [i,j] > 125 and gray [i,j] < 150):  #125 and 150 are the threshold values.
			gray[i,j] = 255
		else:
			gray[i,j] = 0


invert = cv2.bitwise_not(gray)

# Display image
cv2.imshow('harris.jpg', gray)
cv2.waitKey(0)

#Morphing Section
kernel = np.ones((8,5),np.uint8)
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
out = cv2.morphologyEx(closing,cv2.MORPH_CLOSE,se2)


cv2.imshow('opening', opening)
cv2.waitKey(0)
cv2.imshow('closing', closing)
cv2.waitKey(0)
cv2.imshow('output', out)
cv2.waitKey(0)
cv2.imshow('output3',mask)
cv2.waitKey(0)
