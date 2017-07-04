from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import timeit
import time
import cv2
import sys
import os

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

firstFrameTime = 0

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

time.sleep(0.5)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5, minSize = (50, 80))
        
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    if len(faces) >= 1:
        print ("found {0} faces".format(len(faces)))

    rawCapture.truncate(0)
    
    if key == ord("q"):
        break

#NOTE:to run you must have an open cv virtual environment. After in cv virtual environment,
#run with haarcascade_frontalface_default.xml in file execution.
#Ex: (cv) pi@raspberrypi: ~ $ python faces.py haarcascade_frontalface_default.xml
#haarcascade_frontalface_default.xml must be in the same file location as this file.
