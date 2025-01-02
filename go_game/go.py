from dataclasses import dataclass
from enum import Enum

import numpy as np


BOARD_SIZE = 9


"""
Player A is 1, plays black pieces, on matrix marked by 1
Player B is 2, plays white pieces, on matrix marked by 2
If no player has played on position, marked by 0
"""
@dataclass
class State():
    def __init__(self, position: np.ndarray, A_prisoners: int, B_prisoners: int, turn: int):
        self.position = position
        self.A_prisoners = A_prisoners
        self.B_prisoners = B_prisoners
        self.turn = turn


def initialize_state() -> State:
    return State(np.zeros([BOARD_SIZE,BOARD_SIZE]), A_prisoners=0, B_prisoners=0, turn=0)

# I append the move at the end for the pass move. That is always BOARD_SIZE squared, because indexing starts at 0.
def get_legal_moves(state:State) -> np.ndarray:
    flattened_board = state.position.flatten()
    return np.append(np.where(flattened_board == 0)[0], BOARD_SIZE*BOARD_SIZE)


def move_to_index(move: int) -> tuple[int, int]:
    i = move // BOARD_SIZE
    j = move % BOARD_SIZE
    return (i, j)


class pass_move(Enum):
    terminal = False
    new_state = State
# Apply move must assumes player will only play legal move.
def apply_move(state: State, move: int) -> :
    if
    i, j = move_to_index(move)
    pass

def is_terminal(player, state, move):
    pass

def scoring(state):
    pass
