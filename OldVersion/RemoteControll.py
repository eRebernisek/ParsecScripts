import pyautogui
import time
from pyscreeze import pixel
import win32gui,win32con

   # 550 -680 controle
    # 850 -570 A
    # 820 -540 B

def avanca():
    focaParsec() 
    time.sleep(0.2)
    #ativa controle virtual
    pyautogui.mouseDown(550,-680,pyautogui.PRIMARY,0.5)
    pyautogui.mouseUp()
    #avança
    time.sleep(0.3)
    pyautogui.mouseDown(850,-570)
    pyautogui.mouseUp()
    time.sleep(0.3)
    pyautogui.mouseDown(850,-570)
    pyautogui.mouseUp()
    #destiva controle
    pyautogui.mouseDown(550,-680,pyautogui.PRIMARY,0.5)
    pyautogui.mouseUp()
    time.sleep(0.3)
    pyautogui.moveTo(900,1000)

def retorna():
    #ativa controle virtual
    pyautogui.mouseDown(550,-680,pyautogui.PRIMARY,0.5)
    pyautogui.mouseUp()
    # volta
    time.sleep(0.5)
    pyautogui.mouseDown(820,-540)
    time.sleep(2)
    pyautogui.mouseUp()
    time.sleep(2)
    pyautogui.mouseDown(820,-540)
    pyautogui.mouseUp()
    time.sleep(2)
    pyautogui.mouseDown(850,-570)
    pyautogui.mouseUp()
    #destiva controle
    pyautogui.mouseDown(550,-680,pyautogui.PRIMARY,0.5)
    pyautogui.mouseUp()
    time.sleep(0.3)
    pyautogui.moveTo(900,1000)

def focaParsec():
    toplist = []
    winlist = []
    parsecWindow = []
    def enum_callback(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_callback, toplist)
    for iten in winlist:
        isParsec = iten[1].__contains__("Parsec Soda")
        if isParsec:
            parsecWindow = iten
            break

    win32gui.ShowWindow(parsecWindow[0],win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(parsecWindow[0])

if __name__ == '__main__':
    pass
    avanca()
    # retorna()