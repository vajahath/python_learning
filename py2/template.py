#template! what's that heck is it?

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('doodle.jpg')
img2 = img.copy()
template = cv2.imread('image.jpeg')

w, h = template.shape[1], template.shape[0]

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
min_val, max_val; min_loc, max_loc=cv2.minMaxLoc(res)
top_left= max_loc
bottom_right = (top_left[0]+w,top_left[1]+h)

cv2.rectangle(img, top_left, bottom_right, 255, 2)
cv2.imshow('original', img2)
cv2.imshow('template', template)
cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyallWindows()
