import os
import win32gui
import win32con

def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

def getWindows(name):
    windows = []
    appwindows = get_app_list()
    for i in appwindows:
        if name in i[1]:
            windows.append(i)

    return windows

def focusWindow(name):
    windowsList = getWindows(name)

    for x in windowsList:
        try:
            win32gui.SetForegroundWindow(x[0])
        except Exception as e:
            print('Erro ao focar janela')

if __name__ == '__main__':
    os.system('cls')
    
    print('Focando Parsec')
    focusWindow('Parsec Soda')
    print('---')
    print('Focando yuzu')
    focusWindow('yuzu')
    print('---')
    pass