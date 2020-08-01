Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.size()
Size(width=1920, height=1080)
>>> pyautogui.position()
Point(x=1223, y=310)
>>> pyautogui.position()
Point(x=1140, y=226)
>>> pyautogui.position()
Point(x=0, y=0)
>>> pyautogui.moveTo(640,151)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    pyautogui.moveTo(640,151)
  File "C:\Python37\lib\site-packages\pyautogui\__init__.py", line 587, in wrapper
    failSafeCheck()
  File "C:\Python37\lib\site-packages\pyautogui\__init__.py", line 1672, in failSafeCheck
    "PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED."
pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.
>>> pyautogui.moveTo(640,151)
>>> pyautogui.moveTo(640,200)
>>> pyautogui.moveTo(640,900)
>>> def Move():
	pyautogui.click(500,500)
	pyautofui.moveTo(500,800,duration=10)

	
>>> Move()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Move()
  File "<pyshell#12>", line 3, in Move
    pyautofui.moveTo(500,800,duration=10)
NameError: name 'pyautofui' is not defined
>>> def Move():
	pyautogui.click(500,500)
	pyautogui.moveTo(500,800,duration=10)

	
>>> 
>>> move()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    move()
NameError: name 'move' is not defined
>>> def Kayab():
	pyautogui.click(500,500)
	pyautofui.moveTo(500,800,duration=10)

	
>>> Kayab()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Kayab()
  File "<pyshell#21>", line 3, in Kayab
    pyautofui.moveTo(500,800,duration=10)
NameError: name 'pyautofui' is not defined
>>> def Kayab():
	pyautogui.click(500,500)
	pyautogui.moveTo(500,800,duration=10)

	
>>> Kayab()
>>> def Kayab():
	pyautogui.click(500,500)
	pyautogui.moveTo(500,800,duration=2)

	
>>> Kayab()
>>> Kayab()
>>> pyau=uto
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    pyau=uto
NameError: name 'uto' is not defined
>>> def Move():
	pyautogui.click()

	
>>> Move
<function Move at 0x0000019C67328BF8>
>>> def Mbve():
	pyautogui.position()

	
>>> Mbve
<function Mbve at 0x0000019C673289D8>
>>> pyautogui.position()
Point(x=436, y=61)
>>> def Regtangle():
	pyautogui.moveTo(436,61)
	pyautogui.click()
	pyautogui.moveTo(436,200)
	pyautogui.click()
	pyautogui.dragTo(636,400)
	pyautogui.click()

	
>>> Regtangle()
>>> def Regtangle():
	pyautogui.moveTo(436,61)
	pyautogui.click()
	pyautogui.moveTo(436,200)
	pyautogui.click()
	pyautogui.dragTo(636,400)
	pyautogui.click()
	pyautogui.dragTo(639,400)
	pyautogui.click()

	
>>> def Rectangle():
	pyautogui.moveTo(436,61)
	pyautogui.click()
	pyautogui.moveTo(436,200)
	pyautogui.click()
	pyautogui.dragTo(636,400)
	pyautogui.click()
	pyautogui.dragTo(639,400)
	pyautogui.click()

	
>>> Rectangle()


>>> Rectangle()
>>> def Rectangle():
	pyautogui.moveTo(436,61)
	pyautogui.click()
	pyautogui.moveTo(436,200)
	pyautogui.click()
	pyautogui.dragTo(636,400)
	pyautogui.click()
	pyautogui.dragTo(670,400)
	pyautogui.click()

	
>>> Rectangle()
>>> Rectangle()
>>> Rectangle()
>>> def Rectangle():
	pyautogui.moveTo(436,61)
	pyautogui.click()
	pyautogui.moveTo(436,200)
	pyautogui.click()
	pyautogui.dragTo(636,400)
	pyautogui.moveTo(670,400)
	pyautogui.click()

	
>>> Rectangle()
>>> def Rectangle():
	pyautogui.moveTo(436,61)
	pyautogui.click()
	pyautogui.moveTo(436,200)
	pyautogui.click()
	pyautogui.dragTo(736,400)
	pyautogui.moveTo(670,400)
	pyautogui.click()

	
>>> Rectangle()
>>> Rectangle()
>>> def Rectangle():
	pyautogui.moveTo(436,61)
	pyautogui.click()
	pyautogui.moveTo(436,200)
	pyautogui.click()
	pyautogui.dragTo(736,400)
	pyautogui.moveTo(770,400)
	pyautogui.click()

	
>>> Rectangle()
>>> Rectangle()
>>> def Rectangle(x,y,size)
SyntaxError: invalid syntax
>>> def Rectangle(x,y,size):
	pyautogui.clcik(331,168)
	pyautogui.click()

	
>>> pyautogui.position()
Point(x=335, y=73)
>>> def Rectangle(x,y,size):
	pyautogui.clcik(335,73)
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

	
>>> Rectangle(160,337,100)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    Rectangle(160,337,100)
  File "<pyshell#99>", line 2, in Rectangle
    pyautogui.clcik(335,73)
AttributeError: module 'pyautogui' has no attribute 'clcik'
>>> def Rectangle(x,y,size):
	pyautogui.click(335,73)
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

	
>>> Rectangle(160,337,100)
>>> 
