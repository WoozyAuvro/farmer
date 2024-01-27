import os
import cv2

try:
    # Install necessary packages if not installed
    try:
        import face_recognition
    except ImportError:
        from pip._internal import main as pip
        pip(['install', '--user', '-r requirements.txt'])
        import face_recognition

    try:
        import numpy as np
    except ImportError:
        from pip._internal import main as pip
        pip(['install', '--user', 'numpy'])
        import numpy

    try:
        import cv2
    except ImportError:
        from pip._internal import main as pip
        pip(['install', '--user', 'opencv-python opencv-python-headless'])
        import cv2

    # Load Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Region of Interest (ROI) for the detected face
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # Save the detected face as an image
            img_item = f"Image.png"
            cv2.imwrite(img_item, roi_color)

            # Draw a rectangle around the detected face
            color = (0, 50, 250)  # BGR format
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + w
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

            # Release the camera and close the OpenCV windows
            cap.release()
            cv2.destroyAllWindows()

            # Execute the comparison script
            os.system('python compare.py')

            # Break the loop
            break

    # Handle OpenCV errors
except cv2.error:
    pass
    # os.system('compare.py')
