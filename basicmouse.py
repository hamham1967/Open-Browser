import pyautogui


def Rectangle(x,y,size):
    pyautogui.click(335,73)
    #353,73 คือตำแหน่งปุม
    pyautogui.click()
    #1
    pyautogui.moveTo(x,y,duration=1)
    pyautogui.click()
    pyautogui.dragTo(x+size,y,duration=1)
    #2
    pyautogui.dragTo(x+size,y+size,duration=1)
    #3
    pyautogui.dragTo(x,y+size,duration=1)
    #4
    pyautogui.dragTo(x,y,duration=1)
    pyautogui.click()
