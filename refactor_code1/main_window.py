import pygame
import serial
from OpenGL.GL import *
import math

from get_data import get_data_from_rangefinder


class MainApp:
    def __init__(self):
        from settings import PORT_FOR_OPEN, Y_MIN, Y_MAX, X_MIN, X_MAX, STEP_X, STEP_Y, CUT, STEP_WASD, STEP_MOUSE
        self.PORT_FOR_OPEN, self.Y_MIN, self.Y_MAX, self.X_MIN, self.X_MAX, self.STEP_X, self.STEP_Y, self.CUT, self.STEP_WASD, self.STEP_MOUSE = PORT_FOR_OPEN, Y_MIN, Y_MAX, X_MIN, X_MAX, STEP_X, STEP_Y, CUT, STEP_WASD, STEP_MOUSE
        self.uart = serial.Serial(port=PORT_FOR_OPEN, baudrate=115200)
        self.clock = pygame.time.Clock()

        if self.uart.is_open:

            setting_for_rangefinder = f"$LDESP,{Y_MIN},{Y_MAX},{STEP_Y},{X_MIN},{X_MAX},{STEP_X},0,"
            self.uart.write(setting_for_rangefinder.encode())
            self.get_xyz = []
            self.m = -2.3
            self.theta = 0
            self.phi = 0

        self.open = self.uart.is_open

    def run_main_app(self):
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.phi += self.STEP_WASD
                if keys[pygame.K_s]:
                    self.phi -= self.STEP_WASD
                if keys[pygame.K_a]:
                    self.theta += self.STEP_WASD
                if keys[pygame.K_d]:
                    self.theta -= self.STEP_WASD
                if event.type == pygame.MOUSEWHEEL:
                    if event.y > 0:
                        self.m += self.STEP_MOUSE
                    else:
                        self.m -= self.STEP_MOUSE

            if self.open:
                clean_data = get_data_from_rangefinder(self.uart)
                x, y, z, alpha, betta = self.create_xyz(clean_data[0])
                x1, y1, z1, alpha1, betta1 = self.create_xyz(clean_data[1])

                self.get_xyz += [[x, y, z, alpha], [x1, y1, z1, alpha]]

                self.check_uart(alpha1, betta1)

            for i in range(len(self.get_xyz) - 1):
                first = self.get_xyz[i]
                last = self.get_xyz[i + 1]
                if first[3] < self.X_MAX and last[3] > self.X_MIN:

                    MainApp.draw_line(first, last)

            pygame.display.flip()
            self.clock.tick(60)


    def check_uart(self, alpha: int, betta: int):
        if alpha == self.X_MAX and betta == self.Y_MAX:
            self.uart.close()


    def create_xyz(self, clean_data: list | tuple):
        alpha = clean_data[1]
        betta = clean_data[0]
        dist = clean_data[2]

        x = (dist / self.CUT) * math.cos(math.radians(betta)) * math.cos(math.radians(alpha))
        y = (dist / self.CUT) * math.cos(math.radians(betta)) * math.sin(math.radians(alpha))
        z = (dist / self.CUT) * math.sin(math.radians(betta))
        return x, y, z, alpha, betta

    @staticmethod
    def draw_line(data1, data2):
        """Рисует линию от (x1, y1, z1) до (x2, y2, z2)."""
        x1, y1, z1, _ = data1
        x2, y2, z2, _ = data2
        glBegin(GL_LINES)
        glVertex3f(x1, y1, z1)  # Начальная точка
        glVertex3f(x2, y2, z2)  # Конечная точка
        glEnd()
