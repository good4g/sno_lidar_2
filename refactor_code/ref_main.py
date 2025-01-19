import math

import serial

from get_data import get_data_from_rangefinder
from utility import get_ports, get_ports2, open_connection
from settings import *
from draw import draw_line

class App:

    def __init__(self):

        """
        В конструкторе класса происходит настройка движков
         и открывается соединение с дальномером, так же
         создаются переменные для настройки дальномера:
         максимальный угол, на который повернется лидар,
         минимальный угол, шаг с которым лидар будет перемещаться
         """
        self.phi = phi
        self.theta = theta
        self.get_xyz = []

        max_angle: int = 180
        step: int = 1

        self.uart: serial.Serial = open_connection(max_angle, step)
        set_up_engines()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.phi += 1
                if keys[pygame.K_s]:
                    self.phi -= 1
                if keys[pygame.K_a]:
                    self.theta += 1
                if keys[pygame.K_d]:
                    self.theta -= 1
            clean_data = get_data_from_rangefinder(self.uart)
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
                self.get_xyz += [[x, y, z]]
                if 0 < alpha < 180:
                    draw_line(self.get_xyz[-2], self.get_xyz[-1])
                    pygame.display.flip()

            clock.tick(60)


