import win32api
from time import sleep
import numpy as np
import json as j

def emoDi(prevAngle, json):
    if len(json) == 0:
        return None
    else:
        emos = json[0]["faceAttributes"]["emotion"]
        happy, sad = emos["happiness"], emos["sadness"]
        newAngle = (prevAngle + (happy - sad)/30)
        return newAngle

with open("example.json") as file:
    data = j.load(file)
angle = 0
x, y = win32api.GetCursorPos()

while True:
    angle = emoDi(angle, data)
    dx,dy = (200*np.cos(angle),200*np.sin(angle))
    win32api.SetCursorPos((int(x+dx),int(y+dy)))
    sleep(0.005)
    x,y = win32api.GetCursorPos()
    x -= dx -(x+dx)%1
    y -= dy -(y+dy)%1
    if (win32api.GetAsyncKeyState(27)) != 0:
        break

