import numpy as np
import cv2

cap = cv2.VideoCapture("rtp://0.0.0.0:1234")

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (160,120))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    out.write(frame);

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
