import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (15, 20), (100, 20), (230,30,96),3)

#outer
cv2.circle(img, (256,256), 200, (255,255,255), 3)

#lEYE
cv2.circle(img, (181,310), 10, (255,255,255), 3)

#rEYE
cv2.circle(img, (331,310), 10, (255,255,255), 3)



#cv2.rectangle(img, (78,100), (320,390), (200,15,115), 5)

#cv2.rectangle(img, (400,100), (450,150), (200,15,115), -1)

#font = cv2.FONT_HERSHEY_SIMPLEX

#cv2.putText(img, "hi there..:)", (10,256), font, 3, (255,0,0), 2)

cv2.imshow("wow, see this", img)

cv2.waitKey(0)
cv2.destroyAllWindows()