from time import time
import cv2
import os
import datetime
date_time = datetime.datetime.now()
try:
        import pyautogui
except:
    from pip._internal import main as pip
    pip(['install', '--user', 'pyautogui'])
    import pyautogui

try:
    import face_recognition
except:
    # if doesnt work, install cmake > wheel > dlib then run this again
    from pip._internal import main as pip
    pip(['install', '--user', 'face-recognition'])
    import face_recognition

try:
    import pandas as pn
except:
    from pip._internal import main as pip
    pip(['install', '--user', '-r requirements.txt'])
    import pandas

def siesvi(name):
    newname = name.replace(" ", "-")
    df = pn.read_csv('registry.csv')
    if name in str(df['name']):
        row = df.loc[df['name'] == newname]
        regTime = str(row.iloc[0, 1])
        return regTime

def men(name, path):
  import os
  print(name)
  pathi = r'../images/a.png'
  shepherd = pathi
  RegTime = siesvi(name)
  wrote = """
  <!DOCTYPE html>
  <html>
  <head>
  <style>
  * {text-align: center;}
  body
  {
  text-align: center;
  font-family: 'Lexend Deca', sans-serif;
  background-color: lightblue;
  text-shadow: aquamarine;
  }
  </style>
  </head>
  <body>
  <h1>Welcome Back! %s</h1>
  <p></p>
  <img src="%s">
  <p style="background-color:cyan;">this user registered their application at: %s</p>
  </body>
  </html>
  """ % (name, path, RegTime)

  with open('index.html', 'w') as f:
      f.write(wrote)
  os.system("index.html")
  
def intruder_save():
    from PIL import Image
    date_time = datetime.datetime.now()
    Image1 = Image.open('Image.png')
    Image1copy = Image1.copy()
    Image1copy.save(f'intruder\intruder-{date_time.strftime("%H-%M-%S")}.png')


    

try:
    path = r"images"

    imgs = []
    classNames = []
    imgDir = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImg = cv2.imread(f"{path}\{cl}")
        imgs.append(curImg)
        imgDir.append(cl)
        classNames.append(os.path.splitext(cl)[0])

    for i in myList:

        img1 = cv2.imread('Image.png')
        # img1 = cv2.imread('Image.png')
        rgb_1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        enc1 = face_recognition.face_encodings(rgb_1)[0]

        img2 = cv2.imread(f"{path}\{i}")
        rgb_2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        enc2 = face_recognition.face_encodings(rgb_2)[0]

        result = face_recognition.compare_faces([enc1], enc2)
        if str(result) == "[True]":
            print(result)
            #os.system('Image.png')
            #os.system(f'{path}\{i}')
            y = os.path.splitext(i)[0]
            x = i[3:]
            men(y,f"{path}\{i}")
            break

        elif str(result) == "[False]":
            print("ok", result)

    print(type(result))
    if str(result) == "[False]":
        #reg()
        intruder_save()
        os.system("unauthorized.html") 

except IndexError:
    print("Coudn't find a face. Run main.py again")
    # os.system('main.py')