from dataclasses import dataclass
import numpy as np
from enum import Enum
from typing import Optional

BOARD_SIZE = 9


"""
Player A is 1, plays black pieces, on matrix marked by 1
Player B is 2, plays white pieces, on matrix marked by 2
If no player has played on position, marked by 0
"""

class Turn(Enum):
    A = 1
    B = 2

@dataclass
class State():
    def __init__(self, position: np.ndarray, A_prisoners: int, B_prisoners: int, turn: Turn):
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


# recursive helper function for liberties
def dfs_for_liberties(i: int, j: int, position: np.ndarray, color: int, visited: Optional[set[tuple[int, int]]]) -> tuple[int, set[tuple[int,int]]]:
    # we store a set of all the indices we visit
    if color not in [1,2]:
        raise Exception("color must either be 1 or 2")

    if visited is None:
        visited = set()

    if (i,j) in visited:
        return False, visited
    elif i < 0 or i >= BOARD_SIZE or j < 0 or j >= BOARD_SIZE:
        return False, visited
    elif position[i][j] == 0:
        return True, visited
    elif position[i][j] != color:
        return False, visited

    visited.add((i,j))

    # then we continue exploring. In all 4 directions

    hl1, visited = dfs_for_liberties(i+1,j, position, color, visited)
    hl2, visited = dfs_for_liberties(i-1, j, position, color, visited)
    hl3, visited = dfs_for_liberties(i, j+1, position, color, visited)
    hl4, visited = dfs_for_liberties(i, j-1, position, color, visited)


    # By the end, if it doesn't have liberty, then it is set to 0.
    has_liberty = hl1 or hl2 or hl3 or hl4
    if not has_liberty:
        position[i][j] = 0

    return has_liberty, visited

# Apply move must assumes player will only play legal moves.
def apply_move(state: State, move: int):
    # This is to check if its the pass move.
    # If it is, we do nothing except change whose
    if move == BOARD_SIZE * BOARD_SIZE:
        if state.turn == Turn.A:
            state.turn = Turn.B
        else:
            state.turn = Turn.A
        return state

    i, j = move_to_index(move)

    # sanity check to make sure its not already taken
    assert state.position[i][j] == 0




def is_terminal(player, state, move):
    pass

def scoring(state):
    pass
