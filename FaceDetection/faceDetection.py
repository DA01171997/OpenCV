import cv2
import numpy as np

#Create video capturing object
#and faceCascade must load
#haarcascade_frontalface_default.xml
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
videoCaptrObj= cv2.VideoCapture(0)

while videoCaptrObj.isOpened():
        
        #break video into frame
        #convert frame into grayFrame
        #analyze face from grayFrame
        ret, frame = videoCaptrObj.read()
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = faceCascade.detectMultiScale(grayFrame, 1.3, 5)
        

        #face is returned as rectangle
        #draw rectangle object (xTop,yTop,width,height)
        #color B=255 G=255 R =0, pen front = 2 pixels
        
        for(xTop,yTop,width,height) in face:
                cv2.rectangle(frame, (xTop,yTop), (xTop+width, yTop+height), (255, 255, 0), 2)


        #Display frame
        #if Esc==27 key is pressed
        #break the loop
        cv2.imshow('frame', frame)      
        key = cv2.waitKey(10) 
        if key == 27:
                break
			
videoCaptrObj.release()
cv2.destroyAllWindows()

