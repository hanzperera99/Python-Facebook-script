import pyautogui
import time

comments = ["nice","wow","oya thamai dinanne","I love you","patta","summa","gindara"]

time.sleep(5)

for i in range (10):
    pyautogui.typewrite(comments[i%7])
    pyautogui.typewrite("\n")
    time.sleep(3)