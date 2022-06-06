from PIL import ImageGrab
from PIL.Image import Image
import pyautogui
import time
import wmi
from  ControllerConfig import resetControllers
import os
import cv2
from desktopmagic.screengrab_win32 import (
	getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
	getRectAsImage, getDisplaysAsImages)

def reset():
    yuzuFechado = True
    
    encerraYuzu()
    pyautogui.moveTo(0,100)
    pyautogui.moveTo(-100,100)
    # clica no atalho do Yuzu
    xy=findPosition('Images/yuzu.png')
    pyautogui.doubleClick(xy)
    # espera abrir o Yuzu
    while yuzuFechado:
        xy=findPosition('Images/smash.png')
        if xy[0]!=0:
            yuzuFechado=False
        time.sleep(0.2)
    #abre o smash
    pyautogui.doubleClick(xy)    
    # deixa tela cheia
    time.sleep(2)
    pyautogui.click(-600,300)
    pyautogui.press("f11")
    #reseta os controles
    time.sleep(25)
    # resetControllers()

def encerraYuzu():
    f = wmi.WMI()
    processList = f.Win32_Process()
    for process in processList:
        if process.name == "yuzu.exe":
            process.Terminate()

def findPosition(img):
    os.system('cls')

    entireScreen = getScreenAsImage()
    entireScreen.save('screen.png', format='png')

    image= cv2.imread('screen.png')
    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    template= cv2.imread(img,0)

    result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

    if max_val>0.99:
        height, width= template.shape[:2]

        top_left= max_loc
        bottom_right= (top_left[0] + width, top_left[1] + height)
        cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)
        
        # cv2.imshow('Rainforest', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        imgx = (bottom_right[0] + top_left[0])//2

        y1=bottom_right[1]-768
        y2=top_left[1]-768
        imgy = (y1+y2)//2

        x = imgx - 1280
        y = imgy

        return x,y
    else:
        return 0,0

    # print(start)

if __name__ == '__main__':
    pass
    # reset()
    # pyautogui.displayMousePosition()