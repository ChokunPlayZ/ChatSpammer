# Code By ChokunPlayZ
# Completely Open-Sorce Edit it to whatever you want

import time
import pyautogui

def SendScript():
    print("Starting")
    time.sleep(2)
    print("Fuck em")
    with open('text.txt') as f:
        lines = f.readlines()
    for line in lines:
        pyautogui.typewrite(line.strip())
        pyautogui.press('enter')
        print("sent : " + line)

SendScript()