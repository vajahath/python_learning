#error in the prog

import cv2
import numpy as np

img=cv2.imread("doodle.jpg")

px=img[100,100]
print "px: ", px

red=img[100,100]
print "red: ", red

print "img.shape: ", img.shape
print "img.size", img.size

b,g,r=cv2.split(img)

img1=cv2.merge((b,g,r))

cv2.imshow("red", r)
cv2.imshow("blue", b)
cv2.imshow("green", g)

cv2.imshow("merge", img1)

cv2.waitKey(0)

cv2.destroyAllWindows()
