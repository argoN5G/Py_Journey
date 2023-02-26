#!/usr/bin/python3
###
import cv2
from time import time, sleep
from os import system
from sys import exit

# read camera from /dev/video"index=0"
vid = cv2.VideoCapture(0)
# record to file
record  = cv2.VideoWriter_fourcc(*'XVID')
record_file = cv2.VideoWriter("video_Pycamera.mp4", record, 20.0, (640,480))

# record 10 second video you can set more or countinouisly
cond = time()
cond +=10
while cond > time():
    ret, data = vid.read()
    record_file.write(data)


vid.release()
record_file.release()
cv2.destroyAllWindows()

try:
    # dispaly the file video 
    system("./PyVideo.py")
except:
    print("error")
    exit(0)
