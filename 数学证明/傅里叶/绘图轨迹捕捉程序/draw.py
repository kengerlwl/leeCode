
import keyboard
import datetime
import time
import threading
import math
import pyautogui
import pyperclip
import time
from matplotlib import pyplot
from 变量存储与加载 import varLD



x, y = varLD.loadData('date')
n = 2
pyplot.plot(x[n:-1], y[n:-1])
pyplot.show()
time.sleep(2)
