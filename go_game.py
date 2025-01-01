# I'm just using pyspiel to check game rules, and to get available rules given a state.
# Everything else I am handling myself.
# PySpiel can handle all state for me, but I am choosing to implement it myself.
# Unfortunately though, this is necessarily much slower than the pyspiel version.

import pyspiel
import numpy as np

BOARD_SIZE = 19

def get_initial_state():
    game = pyspiel.load_game("go", {"board_size": BOARD_SIZE})
    state = game.new_initial_state()

    return convert_spiel_state_to_numpy(state)


def is_terminal(state_numpy):



def state_to_numpy(state_spiel):


def numpy_state_to_spiel():
    pass

def convert_spiel_state_to_numpy(spiel_state):
    board = np.array(spiel_state.observation_tensor()) #.reshape(BOARD_SIZE, BOARD_SIZE)
    return board
