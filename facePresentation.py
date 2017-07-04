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

waitTime = 2
hasSeenFace = False
facesSeen = 0
firstFrameTime = 0
state = 0

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

time.sleep(0.5)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    faces = faceCascade.detectMultiScale(gray, 1.3, 5, minSize = (200, 250))
    
    if hasSeenFace == False and len(faces) == 1 and facesSeen == 0 and state == 0:
        firstFrameTime = time.time()
        hasSeenFace = True
        rawCapture.truncate(0)
        state = 1
        continue
    if time.time() - firstFrameTime > waitTime and facesSeen == 0 and len(faces) == 1 and state == 1:
        os.system("sudo libreoffice --show AlanTuring.pptx")
        facesSeen = 1
        state = 2

    if hasSeenFace == True and len(faces) == 1 and facesSeen == 1 and state == 2:
        firstFrameTime = time.time()
        rawCapture.truncate(0)
        state = 3
    if time.time() - firstFrameTime > waitTime and facesSeen == 1 and len(faces) == 1 and state == 3:
        os.system("sudo libreoffice --show HomerWarner.pptx")
        facesSeen = 2
        state = 4

    if hasSeenFace == True and len(faces) == 1 and facesSeen == 2 and state == 4:
        firstFrameTime = time.time()
        rawCapture.truncate(0)
        state = 5
    if time.time() - firstFrameTime > waitTime and facesSeen == 2 and len(faces) == 1 and state == 5:
        os.system("sudo libreoffice --show MargaretHamilton.pptx")
        facesSeen = 3
        state = 6

    if hasSeenFace == True and len(faces) == 1 and facesSeen == 3 and state == 6:
        firstFrameTime = time.time()
        rawCapture.truncate(0)
        state = 7
    if time.time() - firstFrameTime > waitTime and facesSeen == 3 and len(faces) == 1 and state == 7:
        os.system("sudo libreoffice --show LarryRoberts.pptx")
        state = 8

    print ("found {0} faces".format(len(faces)))
    print (facesSeen)
    print (firstFrameTime)
    print (hasSeenFace)
        
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
    
    if key == ord("q"):
        break

#NOTE:to run you must have an open cv virtual environment. After in cv virtual environment,
#run with haarcascade_frontalface_default.xml in file execution.
#Ex: (cv) pi@raspberrypi: ~ $ python faces.py haarcascade_frontalface_default.xml
#haarcascade_frontalface_default.xml must be in the same file location as this file.
