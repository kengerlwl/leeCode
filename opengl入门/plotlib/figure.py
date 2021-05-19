from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def drawCircle(x0, y0,sections,radius,z=0):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x0, y0)
    for count in range(0, sections+1):

        alpha = count * 2 * 3.1415926 / sections;
        glVertex3f(x0 + radius * np.cos(alpha), y0 + radius * np.sin(alpha), z);

    glEnd()
