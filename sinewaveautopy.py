import pyautogui, math, time, autopy

screenx, screeny= pyautogui.size()
x, y = pyautogui.position()
screenymid = screeny/2
screenxmid = screenx/2
screenxmidmid = screenxmid/2

run = True
frame = 0

while run:

  time.sleep(.002)
  x, y = pyautogui.position()
  frame += 1

  if not x > screenx-5:
    
    movey = screenxmidmid*math.sin(0.002*x)+screenymid
    autopy.mouse.move(x+1,movey)
  else:
    autopy.mouse.move(1,y)
