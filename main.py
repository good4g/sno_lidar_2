import copy
import threading

import pygame
import serial
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

from get_data import get_data_from_rangefinder


def draw_vector(x, y, z):
    """Рисует вектор от начала координат до заданной точки."""
    glColor3f(1.0, 1.0, 1.0)  # Белый цвет
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(x, y, z)
    glEnd()


def draw_line(data1, data2):
  """Рисует линию от (x1, y1, z1) до (x2, y2, z2)."""
  x1, y1, z1, = data1
  x2, y2, z2 = data2
  glBegin(GL_LINES)
  glVertex3f(x1, y1, z1)  # Начальная точка
  glVertex3f(x2, y2, z2)  # Конечная точка
  glEnd()



def main():
    uart = serial.Serial(port='COM3', baudrate=115200)
    angle_lidar = 180
    if uart.is_open:
        step = 5

        # 1 х0, х конечное, шаг
        st = f"$LDESP,0,0,0,0,{angle_lidar},{step},0,"
        uart.write(st.encode())
    #threading.Thread(target=get_data_from_rangefinder).start()

    pygame.init()
    display = (1920, 1080)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D lidar")

    glEnable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()

    get_xyz = []
    theta = 0.0  # Угол вращения вокруг оси Y
    phi = 180  # Угол вращения вокруг оси X

    #clean_data = [[0, 88], [5, 92], [10, 64], [15, 44], [20, 36], [25, 30], [30, 28], [35, 25], [40, 23], [45, 24], [50, 19], [55, 18], [60, 18], [65, 17], [70, 17], [75, 17], [80, 16], [85, 16], [90, 16], [95, 17], [100, 17], [105, 17], [110, 18], [115, 19], [120, 20], [125, 20], [130, 22], [135, 25], [140, 27], [145, 31], [150, 38], [155, 50], [160, 66], [165, 83], [170, 128], [175, 116], [180, 116]]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                phi += 1
            if keys[pygame.K_s]:
                phi -= 1
            if keys[pygame.K_a]:
                theta += 1
            if keys[pygame.K_d]:
                theta -= 1

            # Ограничения углов (чтобы не было проблем)
            #phi = max(-89, min(89, phi))
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()  # Сбрасываем матрицу
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -2.3)  # Отводим камеру назад

        glRotatef(phi, 1.0, 0.0, 0.0)  # Вращение вокруг оси X
        glRotatef(theta, 0.0, 1.0, 0.0)  # Вращение вокруг оси Y

        clean_data = get_data_from_rangefinder(uart)
        for i in range(len(clean_data)):
            alpha = clean_data[i][0]
            if alpha == 0:
                x = (clean_data[i][1] / 100)
                z = 0
                y = 0
            elif alpha == 180:
                x = (clean_data[i][1] / 100) * -1
                y = 0
                z = 0
            elif alpha == 90:
                x = 0
                y = 0
                z = (clean_data[i][1] / 100) * math.sin(math.radians(alpha))
            else:
                x = (clean_data[i][1] / 100) * math.cos(math.radians(alpha))
                z = (clean_data[i][1] / 100) * math.sin(math.radians(alpha))
                y = 0

            #draw_vector(x, y, z)
            get_xyz += [[x, y, z]]
            if 0 < alpha < 180:

                draw_line(get_xyz[-2], get_xyz[-1])
                x2y2z2 = copy.copy(get_xyz[-2])
                x2y2z2[1] = 0.3
                draw_line(get_xyz[-2], x2y2z2)
                x3y3z3 = copy.copy(get_xyz[-1])
                x3y3z3[1] = 0.3
                draw_line(get_xyz[-1], x3y3z3)
                pygame.display.flip()





        clock.tick(60)


