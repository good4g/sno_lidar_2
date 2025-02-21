import pygame
from pygame import Surface
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import glEnable, GL_DEPTH_TEST, glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, glLoadIdentity


from refactor_code.utility import get_ports

from utilites import check_memorize_json

# CONSTANT SETTINGS

#GENERAL SETTINGS
RESOLUTION: tuple = (1920, 1030)

# MENU SETTINGS
FILL_MENU: tuple = (255, 255, 255)


def set_up_settings_menu() -> Surface:
    pygame.init()
    win: Surface = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("MENU")
    pygame.display.set_icon(win)
    win.fill(FILL_MENU)
    return win


# MENU SETTINGS ELEMENTS

# DROPDOWN SETTINGS
ports = get_ports()

KWARGS_DROPDOWN = {
    "x": 760,
    "y": 100,
    "width": 200,
    "height": 50,
    "name": "Выберите COM-порт",
    "choices": ports,
    "borderRadius": 3,
    "colour": pygame.Color(0, 0, 255),
    "values": ports,
    "direction": "down",
    "textHAlign": "centre",
    "textColour": "white",
}

#SLIDERS SETTINGS
SL_X_X: int = 760
SL_X_Y: int = 350
SL_X_WIDTH: int = 400
SL_X_HEIGHT: int = 40

KWARGS_SL_X_MIN: dict = {
    "min": 0,
    "max": 180,
    "step": 1,
    "initial": 10,
    "vertical": False
}

KWARGS_SL_X_MAX: dict = KWARGS_SL_X_MIN.copy()
KWARGS_SL_X_MAX["initial"]: int = 170
KWARGS_SL_X_MAX["draw_line"]: bool = False
KWARGS_SL_X_MAX["curved"]: bool = False

SL_Y_X: int = 1300
SL_Y_Y: int = 170
SL_Y_WIDTH: int = SL_X_HEIGHT
SL_Y_HEIGHT: int = SL_X_WIDTH

KWARGS_SL_Y_MIN: dict = KWARGS_SL_X_MIN.copy()
KWARGS_SL_Y_MIN["vertical"]: bool = True


KWARGS_SL_Y_MAX: dict = KWARGS_SL_Y_MIN.copy()
KWARGS_SL_Y_MAX["initial"]: int = 50
KWARGS_SL_Y_MAX["draw_line"]: bool = False
KWARGS_SL_Y_MAX["curved"]: bool = False


SL_STEP_X_X: int = 870
SL_STEP_X_Y: int = 430

SL_STEP_X_WIDTH: int = 180
SL_STEP_X_HEIGHT: int = SL_X_HEIGHT

KWARGS_STEP_X: dict = KWARGS_SL_X_MIN.copy()
KWARGS_STEP_X["min"]: int = 1
KWARGS_STEP_X["initial"]: int = 1
KWARGS_STEP_X["max"]: int = 90


SL_STEP_Y_X: int = 1390
SL_STEP_Y_Y: int = 280

SL_STEP_Y_WIDTH: int = SL_STEP_X_HEIGHT
SL_STEP_Y_HEIGHT: int = SL_STEP_X_WIDTH


KWARGS_STEP_Y: dict = KWARGS_STEP_X.copy()
KWARGS_STEP_Y["min"]: int = 1
KWARGS_STEP_Y["max"]: int = 180
KWARGS_STEP_Y["vertical"]: bool = True


#TEXTBOX SETTINGS
OUTPUT_X_X_MIN: int = 640
OUTPUT_X_Y_MIN: int = 350
OUTPUT_X_X_MAX: int = 1210
OUTPUT_X_Y_MAX: int = OUTPUT_X_Y_MIN

OUTPUT_Y_X_MIN: int = 1300
OUTPUT_Y_Y_MIN: int = 620
OUTPUT_Y_X_MAX: int = OUTPUT_Y_X_MIN
OUTPUT_Y_Y_MAX: int = 70

OUTPUT_STEP_X_X: int = 1100
OUTPUT_STEP_X_Y: int = SL_STEP_X_Y

OUTPUT_STEP_Y_X: int = 1490
OUTPUT_STEP_Y_Y: int = 320

OUTPUT_ERRORS_X: int = 710
OUTPUT_ERRORS_Y: int = 700



KWARGS_OUTPUT = {
    "width": 70,
    "height": 50,
    "fontSize": 30,
    "textHAlign": "centre"
}

KWARGS_ERRORS_OUTPUT = KWARGS_OUTPUT.copy()
KWARGS_ERRORS_OUTPUT["width"] = 500
KWARGS_ERRORS_OUTPUT["height"] = 150
# BUTTON SETTINGS

KWARGS_BUTTON_START = {
    "x": 710,
    "y": 550,
    "width": 500,
    "height": 50,
    "border": 100,
    "text": "СТАРТ",
    "inactiveColour": (0, 0, 255),
    "textColour": "white"
}

#MAIN WINDOW SETTINGS
def set_up_settings_main_window():
    pygame.init()
    pygame.display.set_mode(RESOLUTION, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D lidar")

    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

CUT: int = 100
STEP_WASD: int = 1
STEP_MOUSE: float = 0.3
#CHANGEABLE SETTINGS
from utilites import check_memorize_json

check_json = check_memorize_json()

if check_json:
    X_MIN = KWARGS_SL_X_MIN["initial"] = check_json["X_MIN"]
    X_MAX = KWARGS_SL_X_MAX["initial"] = check_json["X_MAX"]
    Y_MIN = KWARGS_SL_Y_MIN["initial"] = check_json["Y_MIN"]
    Y_MAX = KWARGS_SL_Y_MAX["initial"] = check_json["Y_MAX"]

    STEP_X = KWARGS_STEP_X["initial"] = check_json["STEP_X"]
    STEP_Y = KWARGS_STEP_Y["initial"] = check_json["STEP_Y"]

    if check_json["PORT"] in ports:
        PORT_FOR_OPEN: str = check_json["PORT"]
    else:
        PORT_FOR_OPEN: str
else:
    X_MIN: int
    X_MAX: int
    Y_MIN: int
    Y_MAX: int

    STEP_X: int
    STEP_Y: int

    PORT_FOR_OPEN: str
