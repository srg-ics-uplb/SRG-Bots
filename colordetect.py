import numpy as np
import cv2

#Contact: jachermocilla@gmail.com

#for drone
cap = cv2.VideoCapture("rtp://0.0.0.0:1234")

#for netbook
#cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')

#for drone
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (320,120))

#for netbook
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# define the list of boundaries
boundaries = [
    ([17, 15, 100], [50, 56, 200])  #red
]


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret==True:
        # loop over the boundaries
        for (lower, upper) in boundaries:
            # create NumPy arrays from the boundaries
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
 
            # find the colors within the specified boundaries and apply
            # the mask
            mask = cv2.inRange(frame, lower, upper)
            output = cv2.bitwise_or(frame, frame, mask = mask)

        #out.write(frame);

        h1, w1 = frame.shape[:2]
        h2, w2 = output.shape[:2]

        #create empty matrix
        vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

        #combine 2 images
        vis[:h1, :w1,:3] = frame
        vis[:h2, w1:w1+w2,:3] = output

        out.write(vis);
        cv2.imshow('frame',vis)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
