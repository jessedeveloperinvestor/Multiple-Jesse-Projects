import pyautogui
import time

p = pyautogui.position()
s = pyautogui.size()
b = pyautogui.onScreen(130, 200)

print(p)
print(s)
print(b)

pyautogui.move(100, 50)
time.sleep(1)

pyautogui.moveTo(100, 100, 0.5, pyautogui.easeInQuad)
pyautogui.moveTo(500, 500, 0.5, pyautogui.easeOutQuad)
pyautogui.moveTo(900, 700, 0.5, pyautogui.easeInOutQuad)
pyautogui.moveTo(500, 500, 0.5, pyautogui.easeInBounce)
pyautogui.moveTo(100, 100, 0.5, pyautogui.easeInElastic)
time.sleep(1)

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 2
pyautogui.moveTo(0, 0)

pyautogui.sleep(3)
pyautogui.drag(20, 20)
pyautogui.dragTo(100, 100, button='middle')

pyautogui.sleep(2)
pyautogui.click(x=200,y=400)

pyautogui.sleep(2)
pyautogui.doubleClick()
pyautogui.tripleClick()
pyautogui.rightClick()

pyautogui.sleep(1)
pyautogui.moseDown()

pyautogui.scroll(-150)
pyautogui.hscroll()
pyautogui.vscroll()

pyaautogui.write('https://youtybe.com')

pyautogui.press('enter', presses=3)

pyautogui.keyDown('shift')
pyautogui.keyDown('shift')

pyauyogui.hotkey('ctrl', 'a')

pyautogui.alert(text='Alert', title='alert box', button='ok')
pyautogui.confirm(text='Alert', title='alert box', buttons=['ok', 'cancel'])

pyautogui.prompt(text='input', title='input box', default='username')
pyautogui.password(text='input', title='input box', default='username', mask='*')

pyautogui.PAUSE = 2
pyautogui.moveTo(1350, 750)

d = ('hi')
pyautogui.screenshot(f'{d}.png' region=(10,10,700,500))

h = 3
while h > 0:
    pyautogui.moveTo(100, 100, 0.4, pyautogui.easeInOutQuad)
    pyautogui.moveTo(1350, 750, 0.4, pyautogui.easeInOutQuad)
    h = h - 1

while True:
    x,y = pyautogui.position()
    print(f"X:{x} , Y:{y}")
    pyautogui.sleep(0.1)
