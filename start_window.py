import pygame_widgets
import pygame
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from check_ports import get_ports
from main import main

pygame.init()
win = pygame.display.set_mode((1920, 1080))

slider = Slider(win, 760, 350, 400, 40, min=0, max=180, step=1)
label_slider = TextBox(win, 1200, 350, 200, 50, fontSize=30, textVAlign='centre', textHAlign='centre', placeholderText='Выберите шаг', font=pygame.font.SysFont('Times New Roman', 18, 5))
output = TextBox(win, 915, 430, 100, 50, fontSize=30, textHAlign='centre')

#output.disable()

button_start = Button(
    win,
    710,
    550,
    500,50, border=100, text='СТАРТ',  onClick=main, font=pygame.font.SysFont('Times New Roman', 18, 5), inactiveColour=(0, 0, 255), textColour='white'
)


# Act as label instead of textbox

dropdown = Dropdown(
    win, 760, 100, 200, 50, name='Выберите COM-порт',
    choices=get_ports(),
    borderRadius=3, colour=pygame.Color(0, 0, 255), values=get_ports(), direction='down', textHAlign='centre', textColour='white', font=pygame.font.SysFont('Times New Roman', 18, 5)
)


def print_value():
    print(dropdown.getSelected())


button = Button(
    win, 990, 100, 100, 50, text='Выбрать',
    margin=20, inactiveColour=(255, 0, 0), colour=(0, 0, 255),
    radius=5, onClick=print_value, textColour='white',
    textHAlign='centre', font=pygame.font.SysFont('Times New Roman', 18, 5)
)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    output.setText(slider.getValue())

    pygame_widgets.update(events)
    pygame.display.update()