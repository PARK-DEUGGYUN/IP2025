import numpy as np
import cv2
# Create a black image
img = cv2.imread('rabbit.jpg')
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(1200,673),(255,155,155),17)
img = cv2.rectangle(img,(384,0),(510,128),(225,255,0),3)
img = cv2.circle(img,(447,63), 63, (255,155,155),10)
img = cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 3,(255,155,155),12,cv2.LINE_AA)

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()