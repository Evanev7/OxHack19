import win32api
from time import sleep
import numpy as np

for i in np.linspace(0,2*np.pi,1000):
    win32api.SetCursorPos((960+int(np.floor(200*np.cos(i))),540+int(np.floor(200*np.sin(i)))))
    sleep(0.05)