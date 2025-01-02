from dataclasses import dataclass

import numpy as np


BOARD_SIZE = 19


"""
Player A is -1, plays black pieces, on matrix marked by -1
Player B is 1, plays white pieces, on matrix marked by 1
If no player has played on position, marked by 0
"""
@dataclass
class State():
    def __init__(self, position: np.ndarray, A_prisoners: int, B_prisoners: int, turn: int):
        self.position = position
        self.A_prisoners = A_prisoners
        self.B_prisoners = B_prisoners
        self.turn = turn

"""
For use in map reduce on the position matrix.
If the position is unnocupied, it stays 0
If the position has
"""
def has_liberties(index: tuple[int, int], state: State) -> int:
    i, j = index
    piece = state.position[i][j]

    if piece == 0:
        return 0
    # Up direction
    if i > 0 and state.position[i-1][j] == 0:
        return piece
    # Down direction
    if i < BOARD_SIZE - 1 and state.position[i + 1][j] == 0:
        return 0
    # Left direction
    if j > 0 and state.position[i][j] == 0:
        return 0
    # Right direction
    if j < BOARD_SIZE - 1 and state.position[i][j+1] == 0:
        return 0
    return piece






def initialize_state() -> State:
    return State(np.zeros([19,19]), A_prisoners=0, B_prisoners=0, turn=0)

def get_legal_moves(player, state):
    pass

def apply_move(player, state, move):
    pass

def is_terminal(player, state, move):
    pass

def scoring(state):
    pass
