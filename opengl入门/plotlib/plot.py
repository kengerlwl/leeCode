from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import opengl入门.plotlib.StateMachine as Stm


def drawLine(X, Y, rgb=(0,0,0), ltype =None,lwidth=1,z=0):
    '''

    :param X:
    :param Y:
    :param rgb: 线段颜色
    :param z: z的坐标
    :param ltype 是线的类型，默认线性，说就是虚线
    :return:
    '''

    s = Stm.StateArg() # 参数栈状态机
    dic =[1] # 默认的线宽为1
    s.pushState(glLineWidth, *dic)



    maxV = max(max(X), max(Y))



    glLineWidth(lwidth)  # 设置线的宽度，单位是像素

    if ltype == None:
        glLineStipple(1, 0xFFFF);  # 设置线型,直线
    else:
        glLineStipple(1, 0x00FF);  # 设置线型,虚线


    glShadeModel(GL_SMOOTH)  # 开启对颜色的线性插值

    if len(X) == len(Y):
        glBegin(GL_LINE_STRIP)  # 绘制连续线段
        glColor4f(rgb[0], rgb[1], rgb[2], 1)
        for i in range(len(X)):
            glVertex3f(X[i], Y[i], z)

        glEnd()
        s.popState()
    else:
        s.popState()
        assert '数据错误xy数据维度不一样'
        return False


def drawPoints(X, Y, Z,rgb=(0,0,0), size =1):
    """
    x,y,z是点的位置
    rgb是颜色
    size是点的大小
    """

    s = Stm.StateArg() # 参数栈状态机
    dic =[1] # 默认的点大小为1
    s.pushState(glPointSize, *dic)

    maxV = max(max(X), max(Y),max(Z))
    # print(maxV)
    # 对x和y的数据进行放缩[0-1]之间
    X= X
    Y = Y
    Z = Z


    glPointSize(size)  # 设置点的大小



    glShadeModel(GL_SMOOTH)  # 开启对颜色的线性插值

    if len(X) == len(Y):

        glBegin(GL_POINTS)  # 绘制点
        glColor4f(rgb[0], rgb[1], rgb[2], 1)
        for i in range(len(X)):
            glVertex3f(X[i], Y[i], Z[i])

        glEnd()
        s.popState()
    else:
        s.popState()
        assert '数据错误xy数据维度不一样'
        return False