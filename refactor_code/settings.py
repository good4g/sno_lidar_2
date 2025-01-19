import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

display: tuple = (1920, 1080)
theta: int = 0  # Угол вращения вокруг оси Y
phi: int = 180 # Угол вращения вокруг оси X

clock: pygame.time.Clock = pygame.time.Clock()


def set_up_engines() -> None:

    """Настройка движков"""

    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D lidar")

    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)


def set_up_engine_window():
    pygame.init()
    win = pygame.display.set_mode((1920, 1080))
    win.fill((255, 255, 255))
    return win