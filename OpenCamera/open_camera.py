import cv2
import numpy as np

#Create video capturing object
videoCaptrObj= cv2.VideoCapture(0)
#While video capturing is open
while videoCaptrObj.isOpened():
        #Read video object and break into frame
        ret, frame = videoCaptrObj.read()
        #Convert frame into gray color
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Display regular captured Object in window name 'frame'
        cv2.imshow('frame', frame)
        #Display converted captured Object in window name 'grayframe'
        cv2.imshow('gray', grayFrame)
        #Event function that waits every 10 miliseconds for a key input
        key = cv2.waitKey(10) 
        #if Esc==27 key is pressed, break the loop
        if key == 27:
                break
#release capturing video
videoCaptrObj.release()
cv2.destroyAllWindows()
