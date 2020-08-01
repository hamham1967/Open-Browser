#openbrowser.py

import pyautogui
import time
import webbrowser
import pyperclip as cp


url = 'https://www.google.com'
webbrowser.open(url)
time.sleep(2)
pyautogui.write('Thailand')
pyautogui.hotkey('enter')

###
def Search(word):
    time.sleep(3)
    for i in range(7):
        pyautogui.press('tab')
        
    pyautogui.press('backspace')
    pyautogui.write(word)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.screenshot(word + '.png')

Search('Singapore')
Search('USA')
Search('China')
    

                        
