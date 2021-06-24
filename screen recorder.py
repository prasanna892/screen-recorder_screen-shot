import time
import datetime
import cv2                                # pip install opencv-python
import keyboard                           # pip install keyboard
import pyautogui as gui                   # pip install pyautogui
import numpy as np                        # pip install numpy
from PIL import ImageGrab                 # pip install Pillow
from win32api import GetSystemMetrics
import win32api 


inp=input("enter 'v' for video record or 's' for screen shot : ")

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') #video foramt
width = GetSystemMetrics(0) #getting mointer screen width
height = GetSystemMetrics(1) #getting mointer screen height

if inp=='s':
    print("press 'shift+f' for full screen shot")
    print("press 'shift+m' for custom screen shot")


if inp=='v':
    print("press 'shift+f' for full screen recording")
    print("press 'shift+m' for custom screen recording")
    print("press 'f8' for pause")
    print("press 'f9' for resume")
    print("press 'f10' for stop")

while True:
    # logic for full screan record
    if keyboard.is_pressed('shift')==True and keyboard.is_pressed('f')==True:
        left=0
        top=0
        right = GetSystemMetrics(0)
        bottom = GetSystemMetrics(1)
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %I-%M-%S')
        file_name = f'{time_stamp}'
        break
        
    # logic for custom screan record
    if keyboard.is_pressed('shift')==True and keyboard.is_pressed('m')==True:
        state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128 
        state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128 

        print("move your mouse pointer at left top side of your image and steadily hold and then press 'LMB' button")
        print("move your mouse pointer at right bottom side of your image and steadily hold and then press 'RMB' button")
        print("press 'shift+r' to start")
        while True: 
            a = win32api.GetKeyState(0x01)
            b = win32api.GetKeyState(0x02)
            
            if a != state_left:  # Button state changed 
                state_left = a 
                if a<0:
                    mpos1=gui.position()
                    mpos1=str(mpos1).replace("Point(x=",'')
                    mpos1=str(mpos1).replace(" y=",'')
                    mpos1=str(mpos1).replace(")",'')
        
            if b != state_right:  # Button state changed 
                state_right = b 
                if b<0: 
                    mpos2=gui.position()
                    mpos2=str(mpos2).replace("Point(x=",'')
                    mpos2=str(mpos2).replace(" y=",'')
                    mpos2=str(mpos2).replace(")",'')

            if keyboard.is_pressed('shift')==True and keyboard.is_pressed('r')==True:
                [left,top]=mpos1.split(",")
                [right,bottom]=mpos2.split(",")
                width=abs(int(left)-int(right))
                height=abs(int(top)-int(bottom))
                time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %I-%M-%S')
                file_name = f'{time_stamp}.mp4'
                break

            time.sleep(0.010)
        break

if inp=='v':    
    # setting file path, format, fps, height and width
    captured_video = cv2.VideoWriter(f'enter your save location{file_name}.mp4', fourcc,20,(width,height)) 
    start=True

    #printing current time
    print(datetime.datetime.now().strftime('%Y-%m-%d %I-%M-%S'))
    while True:
        if start==True:
            # grapping image from screen
            img=ImageGrab.grab(bbox=(int(left),int(top),int(right),int(bottom)))
        img=img
        img_np = np.array(img) # save image in numpy arry
        img_final=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB) # converting colour BGR2RGB
        img_dis=cv2.resize(img_final,(460,280)) # resizing the image
        cv2.imshow('screen recorder',img_dis) # showing image on screen
        if start==True:
            captured_video.write(img_final) # writing graped image to video
        cv2.waitKey(1) # wait for 1ms
        if keyboard.is_pressed('f10')==True:
            print(datetime.datetime.now().strftime('%Y-%m-%d %I-%M-%S')) # printing current time
            break
        if keyboard.is_pressed('f8')==True:
            start=False
        if keyboard.is_pressed('f9')==True:
            start=True
    
if inp=='s':
    # take a screenshot of the screen and store it in memory, then
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    # and finally write the image to disk
    image = ImageGrab.grab(bbox=(int(left),int(top),int(right),int(bottom)))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'enter your save location{file_name}.png', image)
