""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')

cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()
	
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
	
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))

		#Create white Eye backgrounds
		cv2.circle(frame, ((x + w / 2) - 30, (y + h / 2) - 10), 15, (255,255,255), thickness =-1)
		cv2.circle(frame, ((x + w / 2) + 30, (y + h / 2) - 10), 15, (255,255,255), thickness =-1)

		#Create black pupils
		cv2.circle(frame, ((x + w / 2) - 30, (y + h / 2) - 10), 5, (0,0,0), thickness =-1)
		cv2.circle(frame, ((x + w / 2) + 30, (y + h / 2) - 10), 5, (0,0,0), thickness =-1)

		#Create scary looking mouth
		cv2.ellipse(frame, ((x + w / 2), (y + h / 2 + 10)), (50,50), 180, 180, 360, (255,0,0), thickness = 10) 


	 # Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()