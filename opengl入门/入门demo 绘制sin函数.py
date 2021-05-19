# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # 设置画布背景色。注意：这里必须是4个参数
    # glClear(GL_COLOR_BUFFER_BIT)  # 将上面的颜色赋值给窗口, 只要有这个先后顺序就行

    glMatrixMode(GL_PROJECTION)  #设置投影模式
    gluOrtho2D(0,200,0,200)  # 设置画布x，y的范围
    glDisable(GL_BLEND)  # 关闭颜色混合

    glEnable(GL_LINE_STIPPLE)  #启用线型，可以绘制虚线之类的了



# 绘制图像函数
def drawFunc():
    global x
    global y

    # 清除屏幕
    glClear(GL_COLOR_BUFFER_BIT)

    glLineWidth(3.0)  # 设置线的宽度

    glLineStipple(1, 0xFFFF);  # 设置线型,直线


    glBegin(GL_LINE_STRIP)  # 绘制连续线段

    glColor4f(1.0, 0.0, 0.0, 1.0)        # 设置当前颜色为红色不透明

    for i in range(len(x)):
        glVertex2f(x[i]*100,y[i])

    glEnd()



    glLineStipple(1, 0x00FF);  # 设置线型,虚线


    glBegin(GL_LINE_STRIP)  # 绘制连续线段

    glColor4f(0.0, 1.0, 0.0, 1.0)        # 设置当前颜色为红色不透明

    for i in range(len(x)):
        glVertex2f(x[i]*100,y[i] -20)

    glEnd()

    # 刷新显示图像，保证前面的OpenGL命令立即执行，而不是让它们在缓冲区中等待。
    glFlush()


# 主函数
if __name__ == "__main__":
    # 使用glut库初始化OpenGL
    glutInit()
    # 显示模式 GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    # 设置窗口位置及大小
    glutInitWindowPosition(0, 0)  # 位置是指在屏幕的位置
    glutInitWindowSize(400, 400)
    # 创建窗口
    glutCreateWindow("myTest1")
    global x
    global y
    x = np.linspace(0,2* np.pi,num=1000)
    y = np.sin(x)* 200


    init()


    # 调用display()函数绘制图像
    glutDisplayFunc(drawFunc)


    # 进入glut主循环
    glutMainLoop()
