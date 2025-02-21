import pygame_widgets
import pygame
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from check_ports import get_ports
from main import main

pygame.init()
win = pygame.display.set_mode((1920, 1050))
pygame.display.set_caption("3D LIDAR")

slider_x_min = Slider(win, 760, 350, 400, 40, min=0, max=180, step=1, initial=10)
slider_x_max = Slider(win, 760, 350, 400, 40, min=0, max=180, step=1, initial=170)
#label_slider = TextBox(win, 1200, 350, 200, 50, fontSize=30, textVAlign='centre', textHAlign='centre', placeholderText='Выберите шаг', font=pygame.font.SysFont('Times New Roman', 18, 5))
output1 = TextBox(win, 650, 350, 70, 50, fontSize=30, textHAlign='centre')
output2 = TextBox(win, 1200, 350, 70, 50, fontSize=30, textHAlign='centre')


slider_y_min = Slider(win, 1300, 170, 40, 400, min=0, max=180, step=1, initial=10, vertical=True)
slider_y_max = Slider(win, 1300, 170, 40, 400, min=0, max=180, step=1, initial=50, vertical=True)

output3 = TextBox(win, 1300, 80, 70, 50, fontSize=30, textHAlign='centre')
output4 = TextBox(win, 1300, 620, 70, 50, fontSize=30, textHAlign='centre')


button_start = Button(
    win,
    710,
    550,
    500,50, border=100, text='СТАРТ',  onClick=main, font=pygame.font.SysFont('Times New Roman', 18, 5), inactiveColour=(0, 0, 255), textColour='white'
)



dropdown = Dropdown(
    win, 760, 100, 200, 50, name='Выберите COM-порт',
    choices=get_ports(),
    borderRadius=3, colour=pygame.Color(0, 0, 255), values=get_ports(), direction='down', textHAlign='centre', textColour='white', font=pygame.font.SysFont('Times New Roman', 18, 5)
)


def print_value_x():
   print(dropdown.getSelected())


def get_value():
    val_x = dropdown.getSelected()
    import main
    main.port = val_x


button = Button(
    win, 990, 100, 100, 50, text='Выбрать',
    margin=20, inactiveColour=(255, 0, 0), colour=(0, 0, 255),
    radius=5, onClick=get_value, textColour='white',
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

    output1.setText(slider_x_min.getValue())
    output2.setText(slider_x_max.getValue())

    output3.setText(slider_y_min.getValue())
    output4.setText(slider_y_max.getValue())

    pygame_widgets.update(events)
    pygame.display.update()