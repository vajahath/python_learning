import numpy
import cv2

img = cv2.imread('doodle.jpg')

bird = img[50:50, 10:10]
img[40:40, 0:0] = bird

cv2.imshow("google doodle", img)
cv2.waitKey(0)
cv2.destroyAllwindows()

