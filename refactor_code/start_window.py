import pygame_widgets
import pygame

from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from refactor_code.ref_main import App
from refactor_code.utility import get_ports
from refactor_code.settings import set_up_engine_window

class Menu:
    def __init__(self):

        main_app = App()

        self.win = set_up_engine_window()
        self.slider = Slider(self.win, 760, 350, 400, 40, min=0, max=180, step=1)

        self.label_slider = TextBox(self.win, 1200, 350, 200, 50, fontSize=30, textVAlign='centre', textHAlign='centre',
                                    placeholderText='Выберите шаг', font=pygame.font.SysFont('Times New Roman', 18, 5))

        self.output = TextBox(self.win, 915, 430, 100, 50, fontSize=30, textHAlign='centre')

        self.button_start = Button(
            self.win,
            710,
            550,
            500, 50, border=100, text='СТАРТ', onClick=main_app.run, font=pygame.font.SysFont('Times New Roman', 18, 5),
            inactiveColour=(0, 0, 255), textColour='white'
        )

        # Act as label instead of textbox

        self.dropdown = Dropdown(
            self.win, 760, 100, 200, 50, name='Выберите COM-порт',
            choices=get_ports(),
            borderRadius=3, colour=pygame.Color(0, 0, 255), values=get_ports(), direction='down', textHAlign='centre',
            textColour='white', font=pygame.font.SysFont('Times New Roman', 18, 5)
        )

        def print_value():
            print(self.dropdown.getSelected())

        self.button = Button(
            self.win, 990, 100, 100, 50, text='Выбрать',
            margin=20, inactiveColour=(255, 0, 0), colour=(0, 0, 255),
            radius=5, onClick=print_value, textColour='white',
            textHAlign='centre', font=pygame.font.SysFont('Times New Roman', 18, 5)
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

            self.output.setText(self.slider.getValue())

            pygame_widgets.update(events)
            pygame.display.update()



if __name__ == '__main__':
    Menu().run_menu()