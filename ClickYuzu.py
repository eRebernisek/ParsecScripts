from ast import parse
from operator import iconcat
import os
import time

from WindowHandler import focusWindow
import pyautogui

import cv2
import desktopmagic.screengrab_win32 as scrn
import win32gui
import win32con

def reconnectControllers():
    focusWindow('yuzu')
    pyautogui.click(3370,670)
    time.sleep(0.2)
    pyautogui.press('f11')
    time.sleep(0.5)
    pyautogui.click(2625,32)
    time.sleep(0.5)
    pyautogui.click(2650,138)
    time.sleep(0.5)
    pyautogui.click(2940,260)
    time.sleep(0.5)
    pyautogui.click(3370,670)
    time.sleep(0.5)
    pyautogui.click(3490,670)
    time.sleep(0.5)
    pyautogui.click(3540,710)
    time.sleep(0.2)
    pyautogui.press('f11')



if __name__ == '__main__':
    os.system('cls')
    # Display Mouse Position For Debbug Purposes
    # pyautogui.displayMousePosition()
    reconnectControllers()