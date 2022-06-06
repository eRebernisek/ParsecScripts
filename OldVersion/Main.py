from PIL.Image import Image
import pyautogui
import os
import pytesseract
import time

from wmi import connect
from RemoteControll import avanca
from RemoteControll import retorna
from ControllerConfig import resetControllers
from ResetYuzu import reset
from desktopmagic.screengrab_win32 import (
	getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
	getRectAsImage, getDisplaysAsImages)

running = True

def getLog():
    im = getRectAsImage((15,-66, 400, 0))
    # im=pyautogui.screenshot(region=(50,-185, 400, 40))
    # Image.show(im)
    return im

def readText():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = path_to_tesseract

    imgLog = getLog()
    # imgRead = cv2.imread(imgLog)
    text = pytesseract.image_to_string(imgLog)
    return text

def checkCommand():
    comando = readText()

    crash = str.__contains__(comando,"Emulador, aguarde")
    go = str.__contains__(comando,"Pulando Tela Final")
    back = str.__contains__(comando,"Retornando ao menu")
    conecta = str.__contains__(comando,"Reconectando Controles")

    if(crash):
        return "crash"
    elif(go):
        return "go"
    elif(back):
        return "back"
    elif(conecta):
        return "conecta"
    else:
        return "none"

def runCommand(comando):
    if comando=="crash":
        print("Comando Crash")
        reset()
    elif comando=="conecta":
        print("Comando conecta")
        resetControllers()
    elif comando=="go":
        print("Comando avanca")
        avanca()
    elif comando=="back":
        print("Comando back")
        retorna()
    elif comando == "none":
        print("none")

def runCommandDebug(comando):
    if comando=="crash":
        print("Comando Crash")
    elif comando=="conecta":
        print("Comando conecta")
    elif comando=="go":
        print("Comando avanca")
    elif comando=="back":
        print("Comando back")
    elif comando == "none":
        print("none")

def mainLoop():
    comando=""
    lastComand=""
    while running:
        comando = checkCommand()

        if lastComand!=comando:
            runCommand(comando)
       
        lastComand = comando
        time.sleep(0.5)
        
def mainLoopDebug():
    comando=""
    lastComand=""
    while running:
        time.sleep(0.3)
        comando = checkCommand()

        if lastComand!=comando:
            runCommandDebug(comando)
       
        lastComand = comando


if __name__ == '__main__':
    os.system('cls')
    mainLoop()
    # mainLoopDebug()
    # getLog()