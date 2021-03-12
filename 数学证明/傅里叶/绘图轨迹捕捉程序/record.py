import keyboard
import datetime
import time
import threading
import math
import pyautogui
import time
from matplotlib import pyplot
from 变量存储与加载 import varLD

print('请确保输入文字后 按enter建是发送消息。\n如果不是，请修改成是\n\n 按S建stop或者start')

points = []
limit = 2  # 两点的间隔距离


stop_time = input('请输入每次得间隔时间')
limit = 2



flag = False



for i in range(5):
    print('剩余时间：' + str(5-i) + " s")
    time.sleep(1)


# 判断两点的距离是否大于限制值
def judgeDis(x1,y1, x2,y2, limit):
    dis = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
    return dis > limit

def main():
    count = 0
    while True:

        if flag:
            time.sleep(2)
            continue

        x, y = pyautogui.position()
        if len(points) == 0:
            points.append([x, y])
        else:
            lx,ly = points[-1]
            if judgeDis(x, y, lx, ly, limit=limit):
                points.append([x, -1 * y])

        time.sleep(float(stop_time))

        print('执行脚本'+ str(count))
        count += 1

# 判断事件类型，是否暂停脚本
def judgeEvent(x):

    a = keyboard.KeyboardEvent('down', 28, 's')
    #按键事件a为按下enter键，第二个参数如果不知道每个按键的值就随便写，
    #如果想知道按键的值可以用hook绑定所有事件后，输出x.scan_code即可
    global  flag
    if x.event_type == 'down' and x.name == a.name:
        if flag:
            flag = False
            print('开启脚本')

        else:
            flag = True
            print('关闭脚本')
            x = []
            y = []
            for a, b in points:
                x.append(a)
                y.append(b)
            n =2
            x = x[n:-1]
            y = y[n:-1]
            varLD.saveData([x, y], 'date')
            pyplot.plot(x, y)
            pyplot.show()
            time.sleep(2)


    #当监听的事件为enter键，且是按下的时候

def listen():

    keyboard.hook(judgeEvent)

    # keyboard.hook_key('enter', bcd)

    # recorded = keyboard.record(until='esc')
    keyboard.wait()


t1 = threading.Thread(target=listen)  # 创建多线程实例，Thread中target是需要子线程执行的函数
t2 = threading.Thread(target=main)
t1.start()
t2.start()


