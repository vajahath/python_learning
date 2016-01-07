import cv2
import numpy as np
import colorsys

cap=cv2.imread("doodle.jpg")
cv2.imshow("original", cap)

while True:
	#ret, frame = cap.read()

	frame = cap

	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	mask= cv2.inRange(hsv, lower_blue, upper_blue)

	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('mask', mask)
	cv2.imshow('frame', frame)
	cv2.imshow('res', res)

	k= cv2.waitKey(0) &0xFF
	if k==27:
		break

cv2.destroyAllWindows()
