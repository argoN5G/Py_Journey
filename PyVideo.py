#!/usr/bin/python3
##

#import sys
#from os import system
import cv2
import time

def play_video():
    #system("mpv %s &"%vid)
    vid = "video_Pycamera.mp4"
    cap = cv2.VideoCapture(vid)
    
    while True:
        try:
            ret , data = cap.read()
            cv2.imshow("PyImage", data)
            time.sleep(0.05)
            if cv2.waitKey(1) & 0xFF==ord('q') or ret==False:
                break
        except:
            #keep running the video till q
            time.sleep(1)
            cap = cv2.VideoCapture(vid)
    
    cap.release()
    cv2.destroyAllWindows()


play_video()

