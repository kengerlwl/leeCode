# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # 设置画布背景色。注意：这里必须是4个参数
    # glClear(GL_COLOR_BUFFER_BIT)  # 将上面的颜色赋值给窗口, 只要有这个先后顺序就行


    #
    glMatrixMode(GL_MODELVIEW)  #设置投影模式
    gluLookAt(0,0,0,  #相机在世界坐标的位置
              0,0,1,  #相机镜头对准的物体在世界坐标的位置
              1,0,0  #相机向上的方向在世界坐标中的方向
              )


    glMatrixMode(GL_PROJECTION)  #设置投影模式
    # 设置投影变换视景体参数
    glFrustum(-1,1,-1,1, 0.3,2)

    # glOrtho(-1,1,-1,1, -1,1)  # 设置视景体

    glDisable(GL_BLEND)  # 关闭颜色混合

    glEnable(GL_LINE_STIPPLE)  #启用线型，可以绘制虚线之类的了

    glEnable(GL_DEPTH_TEST)  # 深度测试


def drawCircle(x0, y0,sections,radius, z=0):
    glBegin(GL_TRIANGLE_FAN)
    for count in range(0, sections+1):

        alpha = count * 2 * 3.1415926 / sections;
        glVertex3f(x0 + radius * np.cos(alpha), y0 + radius * np.sin(alpha), z);

    glEnd()





# 绘制图像函数
def drawFunc():
    # 清除屏幕及深度缓存
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


    glColor4f(1,0,0,1)
    drawCircle(0,0,100,0.5,z=0.5)


    glColor4f(0,0,1,1)
    drawCircle(0,0,100, 1, z=0.9)



    # 刷新显示图像，保证前面的OpenGL命令立即执行，而不是让它们在缓冲区中等待。
    glFlush()


# 主函数
if __name__ == "__main__":
    # 使用glut库初始化OpenGL
    glutInit()
    # 显示模式 GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    # 设置窗口位置及大小
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(400, 400)
    # 创建窗口
    glutCreateWindow("test")

    init()


    # 调用display()函数绘制图像
    glutDisplayFunc(drawFunc)
    # 设置全局的回调函数
    # 当没有窗口事件到达时,GLUT程序功能可以执行后台处理任务或连续动画
    glutIdleFunc(drawFunc)
    # 进入glut主循环
    glutMainLoop()

