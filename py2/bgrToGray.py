#rgb to gray :)

import cv2
import numpy as np

img=cv2.imread("doodle.jpg")


cv2.imshow("original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("converted", gray)

cv2.waitKey(0)

cv2.destroyAllWindows()
