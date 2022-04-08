from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


# 绘制三角形
def drawTriangle(x0,y0,a,theta=90):
    '''

    :param x0: 三角形中心x坐标
    :param y0: 三角形中心y坐标
    :param a: 三角形边长
    :param theta: 三角形的角度
    :return:
    '''
    z =0
    glPushMatrix()

     # 从点(x0,y0,0)绕方向（0，0，1）旋转theta度
    glTranslatef(x0,y0,0)
    glRotate(theta ,0,0,1)  # 围绕y轴旋转90度
    glTranslatef(-1*x0,-1*y0,0)

    glBegin(GL_TRIANGLES)
    glVertex3f(x0,y0 + a * np.sqrt(3)/ 3,z)
    glVertex3f(x0 +a /2,y0 - a / 2/ np.sqrt(3),z)
    glVertex3f(x0 -a /2,y0 - a / 2/ np.sqrt(3),z)

    glEnd()

    glPopMatrix()







# 绘制坐标轴
def drawAxis(xmin,xmax, ymin, ymax):
    z = 0
    glLineStipple(1, 0xFFFF);  # 设置线型,直线

    glBegin(GL_LINES)  # 开始绘制线段（世界坐标系）

    xmid = (xmin + xmax) /2
    xlength = xmax - xmin
    ymid = (ymin  + ymax)/2
    ylength = ymax - ymin

    step = 0.1

    # 以黑色绘制x，y轴
    glColor4f(0.0, 0.0, 0.0, 1.0)  # 设置当前颜色为红色不透明
    glVertex3f(xmin, ymid, z)  # 设置x轴顶点（x轴负方向）
    glVertex3f(xmax, ymid, z)  # 设置x轴顶点（x轴正方向）
    glVertex3f(xmid, ymin, z)  # 设置y轴顶点（y轴负方向）
    glVertex3f(xmid, ymax, z)  # 设置y轴顶点（y轴正方向）

    # 绘制间隔
    for i in range(1,int(xlength /step)+1):
        tmpx = xmin + i * step
        glVertex3f(tmpx, ymid, z)
        glVertex3f(tmpx, ymid+0.02, z)

    for i in range(1,int(ylength /step)+1):
        tmpy = ymin + i * step
        glVertex3f(xmid,tmpy , z)
        glVertex3f(xmid+0.02, tmpy, z)





    glEnd()  # 结束绘制线段


    # 绘制xy箭头
    drawTriangle(xmax, ymid,0.05, theta=-90)
    drawTriangle(xmid, ymax,0.05, theta=0)


