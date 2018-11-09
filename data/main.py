__author__ = 'Dai Kieu, Trong To, Carlos Serna'

from . import setup,tools
from .states import main_menu,load_screen, game_functions
from . import settings as s


def main():
    """Add states to control here."""
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {s.MAIN_MENU: main_menu.Menu(),
                  s.LOAD_SCREEN: load_screen.LoadScreen(),
                  s.TIME_OUT: load_screen.TimeOut(),
                  s.GAME_OVER: load_screen.GameOver(),
                  s.LEVEL1: game_functions.Level1()}

    run_it.setup_states(state_dict, s.MAIN_MENU)
    run_it.main()



