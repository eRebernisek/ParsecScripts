import os
import time
import pyautogui

import cv2
import desktopmagic.screengrab_win32 as scrn

from ClickParsec import skipScreen
from ClickYuzu import reconnectControllers

madeCommand = False
imageLog = ""
logCount = 0

# Will look for every image in 'Images' folder
def scanImages():
    global madeCommand
    tempFiles = [(x[2]) for x in os.walk('Images')]
    imageNames = [(x) for x in tempFiles[0]]
    for x in imageNames:
        if (('ctrl' in x) or ('win' in x)) and not madeCommand:
            path = 'Images/'+x
            findImg(path)
    madeCommand = False

# Localize Image on screen
def findImg(img):
    global imageLog

    # Para pegar a tela inteira
    # entireScreen = scrn.getScreenAsImage()

    # Pega a tela de cada monitor separado
    # monitorsScreen = scrn.getDisplaysAsImages()

    # Pega as coordenadas de cada monitor
    # monitorRects = scrn.getDisplayRects

    # Pega coordenadas HARD CODED por causa de BUG no desktopMagic
    tempRect = [2560, 0, 4480, 1080]
    # tempRect = [0, 0, 2560, 1080]
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
    cv2.rectangle(gray, top_left, bottom_right, (0,0,255),5)
    cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)

    imageLog = image
    customCommand(img,max_val)
    # Display Image for debbug purposes
    # showImg(image,max_val)
    
# Display Image for debbug purposes
def showImg(img,max_val):
    os.system('cls')
    print(max_val)
    cv2.imshow('Tittle Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def saveLog(type):
    global imageLog
    global logCount

    logCount += 1
    tempName = type.split('/')[1]
    name = 'Log' + str(logCount) + tempName
    cv2.imwrite('Logs/'+name,imageLog)

def customCommand(imgName,max_val):
    global madeCommand
    if 'ctrl' in imgName:
        if max_val > 0.6:
            print('Reconectando Controle')
            saveLog(imgName)
            reconnectControllers()
            madeCommand = True
    elif 'win' in imgName:
        if max_val > 0.85:
            print('Pulando tela de vitória')
            saveLog(imgName)
            skipScreen()
            madeCommand = True

if __name__ == '__main__':
    os.system('cls')
    # Display Mouse Position For Debbug Purposes
    # pyautogui.displayMousePosition()
    while True:
        time.sleep(1)
        print('Lendo Tela')
        scanImages()
        print('------')