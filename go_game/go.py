from dataclasses import dataclass
import numpy as np
from typing import Optional, Self

BOARD_SIZE = 9


"""
Player A is 1, plays black pieces, on matrix marked by 1
Player B is 2, plays white pieces, on matrix marked by 2
If no player has played on position, marked by 0
"""

@dataclass
class State():
    def __init__(self, position: np.ndarray, A_prisoners: int, B_prisoners: int, move_num: int):
        self.position = position
        self.A_prisoners = A_prisoners
        self.B_prisoners = B_prisoners
        self.move_num = move_num
        self.previous_move = 0

    def __repr__(self) -> str:
        return f"Position: {self.position} \n A_prisoners: {self.A_prisoners} B_prisoners: {self.B_prisoners} Move_num: {self.move_num}"
    # doesn't change value of move_num
    def color(self) -> int:
        if self.move_num % 2 == 0:
            return 1
        return 2
    # doesn't change value of move_num
    def other_color(self):
        if self.color() == 2:
            return 1
        return 2

    def add_prisoners(self, num: int) -> int:
        if self.color() == 1:
            self.A_prisoners += num
            return self.A_prisoners
        else:
            assert self.color() == 2
            self.B_prisoners += num
            return self.B_prisoners

    def copy(self):
        return State(np.copy(self.position), self.A_prisoners, self.B_prisoners, self.move_num)


def other_color(color: int) -> int:
    if color == 2:
        return 1
    return 2

def initialize_state() -> State:
    return State(np.zeros([BOARD_SIZE,BOARD_SIZE]), A_prisoners=0, B_prisoners=0, move_num=0)

# I append the move at the end for the pass move. That is always BOARD_SIZE squared, because indexing starts at 0.
def get_legal_moves(state:State) -> np.ndarray:
    flattened_board = state.position.flatten()
    return np.append(np.where(flattened_board == 0)[0], BOARD_SIZE*BOARD_SIZE)

def move_to_index(move: int) -> tuple[int, int]:
    i = move // BOARD_SIZE
    j = move % BOARD_SIZE
    return (i, j)

# recursive helper function for liberties
# This does not modify the state
def dfs_for_liberties(i: int, j: int, position: np.ndarray, color: int, visited: Optional[set[tuple[int, int]]]) -> tuple[int, set[tuple[int,int]]]:
    # we store a set of all the indices we visit
    if color not in [1,2]:
        raise Exception("color must either be 1 or 2")


    if visited is None:
        visited = set()
    # Base cases
    if (i,j) in visited:
        return False, visited
    elif i < 0 or i >= BOARD_SIZE or j < 0 or j >= BOARD_SIZE:
        return False, visited
    elif position[i][j] == 0:
        return True, visited
    elif position[i][j] == other_color(color):
        return False, visited

    visited.add((i,j))

    # then we continue exploring. In all 4 directions

    hl1, visited = dfs_for_liberties(i+1,j, position, color, visited)
    hl2, visited = dfs_for_liberties(i-1, j, position, color, visited)
    hl3, visited = dfs_for_liberties(i, j+1, position, color, visited)
    hl4, visited = dfs_for_liberties(i, j-1, position, color, visited)
    # By the end, if it doesn't have liberty, then it is set to 0.
    has_liberty = hl1 or hl2 or hl3 or hl4

    return has_liberty, visited


def apply_move(state: State, move: int) -> State:
    new_state = state.copy()

    if move == BOARD_SIZE * BOARD_SIZE:
        return new_state

    i, j = move_to_index(move)
    assert new_state.position[i][j] == 0,  "Error: Cannot play move if there already is a piece there"

    new_state.position[i][j] = new_state.color()

    def remove_prisoners(new_state: State, i: int, j: int):
        if new_state.position[i][j] == new_state.color():
            return

        has_liberties, indices = dfs_for_liberties(i, j, new_state.position, new_state.other_color(), visited=None)
        if not has_liberties:
            rows, cols = zip(*indices)
            new_state.position[rows, cols] = 0
            new_state.add_prisoners(len(indices))
        else:
            return

    if i-1 > 0:
        remove_prisoners(new_state, i-1, j)
    if i+1 <= BOARD_SIZE:
        remove_prisoners(new_state, i+1, j)
    if j-1 > 0:
        remove_prisoners(new_state, i, j-1)
    if j+1 <= BOARD_SIZE:
        remove_prisoners(new_state, i, j+1)

    new_state.move_num += 1
    return new_state


def is_terminal(player, state, move):
    pass

def scoring(state):
    pass
