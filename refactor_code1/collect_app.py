from refactor_code1.main_window import MainApp
from start_window import Menu

main_app = MainApp

menu = Menu(main_app)

if __name__ == '__main__':
    menu.run_menu()