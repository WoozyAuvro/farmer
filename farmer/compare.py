import os
import cv2
import datetime
import pandas as pd

# Install necessary packages if not installed
try:
    import pyautogui
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'pyautogui'])
    import pyautogui

try:
    import face_recognition
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'face-recognition'])
    import face_recognition

try:
    import pandas as pd
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', '-r requirements.txt'])
    import pandas as pd

# Function to get registration time from CSV
def get_registration_time(name):
    new_name = name.replace(" ", "-")
    df = pd.read_csv('registry.csv')
    if name in str(df['name']):
        row = df.loc[df['name'] == new_name]
        reg_time = str(row.iloc[0, 1])
        return reg_time

# Function to generate HTML and display user info
def display_user_info(name, path):
    print(name)
    pathi = r'../images/a.png'
    shepherd = pathi
    reg_time = get_registration_time(name)
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    * {{text-align: center;}}
    body
    {{
    text-align: center;
    font-family: 'Lexend Deca', sans-serif;
    background-color: lightblue;
    text-shadow: aquamarine;
    }}
    </style>
    </head>
    <body>
    <h1>Welcome Back! {name}</h1>
    <p></p>
    <img src="{path}">
    <p style="background-color:cyan;">This user registered their application at: {reg_time}</p>
    </body>
    </html>
    """
    with open('index.html', 'w') as f:
        f.write(html_content)
    os.system("index.html")

# Function to save intruder image
def save_intruder_image():
    from PIL import Image
    date_time = datetime.datetime.now()
    image1 = Image.open('Image.png')
    image1copy = image1.copy()
    image1copy.save(f'intruder/intruder-{date_time.strftime("%H-%M-%S")}.png')

# Main block
try:
    path = r"images"
    imgs = []
    classNames = []
    imgDir = []
    myList = os.listdir(path)

    for cl in myList:
        curImg = cv2.imread(f"{path}/{cl}")
        imgs.append(curImg)
        imgDir.append(cl)
        classNames.append(os.path.splitext(cl)[0])

    for i in myList:
        img1 = cv2.imread('Image.png')
        rgb_1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        enc1 = face_recognition.face_encodings(rgb_1)[0]

        img2 = cv2.imread(f"{path}/{i}")
        rgb_2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        enc2 = face_recognition.face_encodings(rgb_2)[0]

        result = face_recognition.compare_faces([enc1], enc2)
        if str(result) == "[True]":
            y = os.path.splitext(i)[0]
            x = i[3:]
            display_user_info(y, f"{path}/{i}")
            break
        elif str(result) == "[False]":
            print("ok", result)

    if str(result) == "[False]":
        save_intruder_image()
        os.system("unauthorized.html")

except IndexError:
    print("Couldn't find a face. Run main.py again")
