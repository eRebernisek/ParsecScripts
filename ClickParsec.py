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

def skipScreen():
    icon = 'Images/icon.png'
    panel = 'Images/panel.png'

    focusWindow('Parsec Soda')
    time.sleep(0.5)
    iconPos = findImg(icon)
    clickPos(iconPos)
    panelPos = findImg(panel)
    panelPos = [panelPos[0]+140,panelPos[1]+30]
    clickPos(panelPos)
    clickPos(panelPos)
    clickPos(iconPos)

# Metodo melhor documentado em ReadScreen
# Modificado para achar icone do Parsec e retorna coordenadas
def findImg(img):

    tempRect = [0, 0, 2560, 1080]
    yuzuDisplay = scrn.getRectAsImage(tempRect)

    yuzuDisplay.save('screen.png', format='png')
    image= cv2.imread('screen.png')
    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Procura imagem na tela
    template= cv2.imread(img,0)
    result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

    # Marca Retangulo no que foi encontrado
    height, width= template.shape[:2]
    top_left= max_loc
    bottom_right= (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)

    if max_val>0.8:
        # Display Image for debbug purposes
        # showImg(image,max_val)
        imgx = (bottom_right[0] + top_left[0])//2

        y1=bottom_right[1]
        y2=top_left[1]
        imgy = (y1+y2)//2

        x = imgx
        y = imgy
        
        return x,y
    else:
        # Display Image for debbug purposes
        showImg(image,max_val)
        print('Erro ao encontrar controle do Parsec')
        return 0,0

# Display Image for debbug purposes
def showImg(img,max_val):
    os.system('cls')
    print(max_val)
    cv2.imshow('Tittle Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def clickPos(xy):
    pyautogui.mouseDown(xy)
    pyautogui.mouseUp(xy)
  

if __name__ == '__main__':
    os.system('cls')
    skipScreen()
    pass