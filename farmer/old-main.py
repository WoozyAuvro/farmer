from tkinter import W
from turtle import width
import os

try:

    try:
        import face_recognition
    except:
        from pip._internal import main as pip
        pip(['install', '--user', '-r requirements.txt'])
        import face_recognition

    try:
        import numpy as np 
    except:
        from pip._internal import main as pip
        pip(['install', '--user', 'numpy'])
        import numpy
        
    try:
        import cv2
    except:
        from pip._internal import main as pip
        pip(['install', '--user', 'opencv-python opencv-python-headless'])
        import cv2
    print("script started")
    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
    cap = cv2.VideoCapture(0)
    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer.read("trainer.yml")
    print("cap initiated")
    while True:
        print("loop started")
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        print("ffaace started")
        for(x,y,w,h) in faces:
            print(x,y,w,h)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # id_, conf = recognizer.predict(roi_gray)
            # if conf>=45 and conf <= 85:
            print("searching for faces")
    
            img_item = f"Image.png"
            cv2.imwrite(img_item, roi_color)
                

            color = (0, 50, 250)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + w
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

            print('face found...')
            
            cap.release()
            cv2.destroyAllWindows()
        #cv2.imshow('video', frame)
            os.system('python compare.py')
        #if cv2.waitKey(20) == ord('q'):
            break

except cv2.error:
    pass
    # os.system('compare.py')