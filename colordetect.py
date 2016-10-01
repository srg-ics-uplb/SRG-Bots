import numpy as np
import cv2

#Contact: jachermocilla@gmail.com

#for drone
#cap = cv2.VideoCapture("rtp://0.0.0.0:1234")

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')

#for drone
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (160,120))

out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret==True:
        out.write(frame);
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
