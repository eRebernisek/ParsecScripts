import pyautogui
import os
import sys
import time

os.system('cls')

def resetControllers():
    pyautogui.moveTo(0,100)
    pyautogui.moveTo(-100,120)
    # foca o Yuzu
    time.sleep(0.3)
    pyautogui.click(-600,300)
    # sai da tela cheia
    time.sleep(2)
    pyautogui.press("f11")
    # clica na aba emulation
    time.sleep(0.5)
    pyautogui.click(-1200,55)
    # clica nas config
    time.sleep(0.5)
    pyautogui.click(-1200,195)
    # clica nos controles
    time.sleep(0.5)
    pyautogui.click(-1100,157)
    # desconecta controles
    time.sleep(0.5)
    pyautogui.click(-603,689)
    # reconecta controles
    time.sleep(0.5)
    pyautogui.click(-455,689)
    # clica ok
    time.sleep(0.5)
    pyautogui.click(-406,738)
    # volta tela cheia
    time.sleep(0.5)
    pyautogui.press("f11")
    time.sleep(0.3)
    pyautogui.click(900,1000)
    time.sleep(0.3)
    pyautogui.click(-600,300)
    time.sleep(0.3)
    pyautogui.moveTo(900,1000)

if __name__ == '__main__':
    resetControllers()
    pass
