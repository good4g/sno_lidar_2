from refactor_code1.main_window import MainApp
from settings import *

import pygame_widgets
import pygame

from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox


class Menu:

    def __init__(self, instance):

        self.win = set_up_settings_menu()

        self.instance = instance

        font = pygame.font.SysFont('Times New Roman', 18, 5)

        self.slider_x_min = Slider(self.win, SL_X_X, SL_X_Y, SL_X_WIDTH, SL_X_HEIGHT, **KWARGS_SL_X_MIN)
        self.slider_x_max = Slider(self.win, SL_X_X, SL_X_Y, SL_X_WIDTH, SL_X_HEIGHT, **KWARGS_SL_X_MAX)

        self.slider_y_min = Slider(self.win, SL_Y_X, SL_Y_Y, SL_Y_WIDTH, SL_Y_HEIGHT, **KWARGS_SL_Y_MIN)
        self.slider_y_max = Slider(self.win, SL_Y_X, SL_Y_Y, SL_Y_WIDTH, SL_Y_HEIGHT, **KWARGS_SL_Y_MAX)

        self.slider_step_x = Slider(self.win, SL_STEP_X_X, SL_STEP_X_Y, SL_STEP_X_WIDTH, SL_STEP_X_HEIGHT, **KWARGS_STEP_X)
        self.slider_step_y = Slider(self.win, SL_STEP_Y_X, SL_STEP_Y_Y, SL_STEP_Y_WIDTH, SL_STEP_Y_HEIGHT, **KWARGS_STEP_Y)

        self.output_x_min = TextBox(self.win, OUTPUT_X_X_MIN, OUTPUT_X_Y_MIN, **KWARGS_OUTPUT).disable()
        self.output_x_max = TextBox(self.win, OUTPUT_X_X_MAX, OUTPUT_X_Y_MAX, **KWARGS_OUTPUT).disable()

        self.output_y_min = TextBox(self.win, OUTPUT_Y_X_MIN, OUTPUT_Y_Y_MIN, **KWARGS_OUTPUT).disable()
        self.output_y_max = TextBox(self.win, OUTPUT_Y_X_MAX, OUTPUT_Y_Y_MAX, **KWARGS_OUTPUT).disable()

        self.output_step_x = TextBox(self.win, OUTPUT_STEP_X_X, OUTPUT_STEP_X_Y, **KWARGS_OUTPUT).disable()
        self.output_step_y = TextBox(self.win, OUTPUT_STEP_Y_X, OUTPUT_STEP_Y_Y, **KWARGS_OUTPUT).disable()

        self.output_error = TextBox(self.win, OUTPUT_ERRORS_X, OUTPUT_ERRORS_Y, **KWARGS_ERRORS_OUTPUT).disable().hide()


        self.dropdown_ports = Dropdown(
            self.win, font=font, **KWARGS_DROPDOWN
        )

        self.button_start = Button(
            self.win,
            font=font, onClick=self.collect_all, **KWARGS_BUTTON_START
        )


    def run_menu(self):
        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()
                if pygame.key.get_pressed()[pygame.K_r]:
                    self.__init__(self.instance)


            self.win.fill(FILL_MENU)
            self.output_x_min.setText(self.slider_x_min.getValue())
            self.output_x_max.setText(self.slider_x_max.getValue())

            self.output_y_min.setText(self.slider_y_min.getValue())
            self.output_y_max.setText(self.slider_y_max.getValue())

            self.output_step_x.setText(self.slider_step_x.getValue())
            self.output_step_y.setText(self.slider_step_y.getValue())

            pygame_widgets.update(events)
            pygame.display.update()

    def show_errors(self, error: str):
        reset = "Нажмите R для перезагрузки"
        self.output_error.setText(f"{error} {reset}")
        self.output_error.show()

    def check_errors(self):
        if not ports:
            self.show_errors("ПОДКЛЮЧИТЕ COM-ПОРТЫ.")
            return False
        if self.dropdown_ports.getSelected() is None and not ports:
            self.show_errors("Выберите COM-ПОРТ.")
            return False
        return True

    def edit_values(self):
        import settings

        settings.PORT_FOR_OPEN = self.dropdown_ports.getSelected()
        settings.X_MIN = self.slider_x_min.getValue()
        settings.X_MAX = self.slider_x_max.getValue()
        settings.Y_MIN = self.slider_y_min.getValue()
        settings.Y_MAX = self.slider_y_max.getValue()
        settings.STEP_X = self.slider_step_x.getValue()
        settings.STEP_Y = self.slider_step_y.getValue()

    def collect_all(self):
        if self.check_errors():

            self.edit_values()
            self.memorize_data()

            self.instance().run_main_app()



    def memorize_data(self):

        data = {
            "PORT": self.dropdown_ports.getSelected(),
            "X_MIN": self.slider_x_min.getValue(),
            "X_MAX": self.slider_x_max.getValue(),
            "Y_MIN": self.slider_y_min.getValue(),
            "Y_MAX": self.slider_y_max.getValue(),
            "STEP_X": self.slider_step_x.getValue(),
            "STEP_Y": self.slider_step_y.getValue(),
        }

        from utilites import create_memorize_json

        create_memorize_json(**data)


