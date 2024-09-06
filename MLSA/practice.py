import numpy as np
import cv2 as cv

#Shape Cutter
img= cv.imread('sample.jpg')
img=cv.resize(img,(600,600),interpolation=cv.INTER_AREA)


cv.rectangle(img,(280,300),(380,400),color=(0,0,255),thickness=5) #blue green red
cv.imshow("JAI HIND",img)

cv.waitKey(0)

#Green Light Red Light
capture = cv.VideoCapture(0)

while (True):
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)

    if(cv.waitKey(0) & 0xFF==ord('q')):
        break

capture.release()
cv.destroyAllWindows()