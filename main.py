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
  x1, y1, z1, _ = data1
  x2, y2, z2, _ = data2
  glBegin(GL_LINES)
  glVertex3f(x1, y1, z1)  # Начальная точка
  glVertex3f(x2, y2, z2)  # Конечная точка
  glEnd()


def check_data(clean_data, uart):
    alpha = clean_data[1]
    betta = clean_data[0]

    x = (clean_data[2] / 100.0) * math.cos(math.radians(betta)) * math.cos(math.radians(alpha))
    y = (clean_data[2] / 100.0) * math.cos(math.radians(betta)) * math.sin(math.radians(alpha))
    z = (clean_data[2] / 100.0) * math.sin(math.radians(betta))
    if betta == 50:
        uart.close()
    return x, y, z, alpha


port = ''

def main():
    global port
    print(port)
    uart: serial.Serial = serial.Serial(port=port, baudrate=115200)
    angle_lidar = 180
    if uart.is_open:
        step = 5

        # 1 х0, х конечное, шаг
        st = f"$LDESP,0,90,1,0,{angle_lidar},{step},0,"
        uart.write(st.encode())
    #threading.Thread(target=get_data_from_rangefinder).start()

    pygame.init()
    display = (1920, 1080)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D lidar")

    glEnable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()

    get_xyz = []
    m = -2.3
    theta = 0.0  # Угол вращения вокруг оси Y
    phi = 0  # Угол вращения вокруг оси X
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
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    m += 0.3
                else:
                    m -= 1

            # Ограничения углов (чтобы не было проблем)
            #phi = max(-89, min(89, phi))
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()  # Сбрасываем матрицу
        gluPerspective(45, (display[0] / display[1]), 0.1, 500)
        glTranslatef(0.0, 0.0, m)  # Отводим камеру назад

        glRotatef(phi, 1.0, 0.0, 0.0)  # Вращение вокруг оси X
        glRotatef(theta, 0.0, 1.0, 0.0)  # Вращение вокруг оси Y

        # print('вгувт скувт')
        if uart.is_open:
            clean_data = get_data_from_rangefinder(uart)
            x, y, z, alpha  = check_data(clean_data[0], uart)
            x1, y1, z1, alpha1  = check_data(clean_data[1], uart)

            get_xyz += [[x, y, z, alpha], [x1, y1, z1, alpha]]
            # print(get_xyz)


        for i in range(len(get_xyz) - 1):
            first = get_xyz[i]
            last = get_xyz[i + 1]
            if first[3] < 180 and last[3] > 0:
                print(first, last)
                draw_line(first, last)
        pygame.display.flip()
        clock.tick(60)





