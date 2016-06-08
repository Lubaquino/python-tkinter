from pyautogui import *
from time import sleep

FAILSAFE = True
PAUSE = 2.5

def findImage(image):
    try:
        sleep(3)
        x, y = locateCenterOnScreen('C:\\Users\\guyfieri\\Pictures\\' + image)
        moveTo(x, y)
        print("Found " + image + " at X=" + str(x) + ", Y=" + str(y))
    except:
        print("Couldn't find " + image + ".")
