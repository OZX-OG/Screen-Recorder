# Code Changed, Optimized And Commented By: OZX-OG
#import libraries

import time
import cv2
import numpy as np
from pyautogui import screenshot
import colorama
from keyboard import is_pressed
from os import name, system
from win32api import GetSystemMetrics
from colorama import Fore

#Color
colorama.init(autoreset=True)

#You Know ;)
print(f"{Fore.YELLOW}--{Fore.GREEN} Screen Recorder By: OZX-OG {Fore.YELLOW} --")

#var
STOP = "s"
file_name = ""
fps = 120
prev = 0

#input file name
file_name = input("Enter File Name: ")

#Screen resolution 
screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))

#settings
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(F"{file_name}.mp4", fourcc, 20.0, (screen_size))


#clear cmd
if name == 'nt': system('cls')
else: system("clear") 

print(f"You can stop recording by Pressing: {STOP}")
print(f"{Fore.YELLOW}-{Fore.GREEN} iS Recording... {Fore.YELLOW}-")

#rec
while True:
    
    time_elpsed = time.time() - prev
    
    #pyautogui
    img = screenshot()
    
    
    if time_elpsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output.write(frame)

    if is_pressed(STOP.lower()):
        #end rec
        cv2.destroyAllWindows()
        output.release()
        print(f"{Fore.RED}- End Record -")
        time.sleep(0.5)
        break
        
