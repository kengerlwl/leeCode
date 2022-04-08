from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np



# 绘制圆形
def drawCircle(x0, y0,sections,radius,z=0):
    """
    x0,y0是圆的圆心，z是圆所在的z轴位置
    section是这个圆的精度，精度越大越接近圆
    radius是圆的半径
    """
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x0, y0)
    for count in range(0, sections+1):

        alpha = count * 2 * 3.1415926 / sections;
        glVertex3f(x0 + radius * np.cos(alpha), y0 + radius * np.sin(alpha), z);

    glEnd()



def drawSphere():

    glBegin(GL_SPHERE_MAP)
    pass


