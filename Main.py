import os
import time

from ReadScreen import scanImages

running = True

def checkScreen(comando):
    scanImages()

def mainLoop():
    while running:
        print('Lendo Tela')
        scanImages()
        print('------')
        time.sleep(5)
        
def mainLoopDebug():
    pass


if __name__ == '__main__':
    os.system('cls')
    # Clean Logs
    files = os.listdir('Logs')
    for x in files:
        path = 'Logs/'+x
        os.remove(path)
    mainLoop()
    # mainLoopDebug()
    # getLog()