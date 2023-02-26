#!/usr/bin/python3

# import the opencv library
import cv2
   
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame by frame
    ret, data = vid.read()
  
    # Display the resulting frame
    cv2.imshow('Python openCV Camera', data)
      
    # the 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
