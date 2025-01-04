from dataclasses import dataclass
import numpy as np
from typing import Optional

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

# Apply move must assumes player will only play legal moves.
def apply_move(state: State, move: int):
    # This is to check if its the pass move.
    # If it is, we do nothing except change whose
    if move == BOARD_SIZE * BOARD_SIZE:
        state.move_num += 1
        return state


    i, j = move_to_index(move)
    # sanity check to make sure its not already taken
    assert state.position[i][j] == 0, "cannot play move when there already is a piece there"

    # This changes the state
    state.position[i][j] = state.color()

    # This modifies state.position matrix
    # and modifies prisoner count in place
    def remove_prisoners(state: State, i: int, j: int):
        # something to do with other color, if the piece next to is the same color, doing other_color is the same color, when you need it to be the same color
        if state.position[i][j] == state.color():
            return
        has_liberties, indices = dfs_for_liberties(i, j, state.position, state.other_color(), visited=None)

        if not has_liberties:
            rows, cols = zip(*indices)
            state.position[rows, cols] = 0
            state.add_prisoners(len(indices))
        else:
            return

    # We check if the move caused any pieces in the 4 directions to stop having liberties.
    # If they do, then the state gets modified in place to remove them
    if i-1 > 0:
        remove_prisoners(state, i-1, j)
    if i+1 <= BOARD_SIZE:
        remove_prisoners(state, i+1, j)
    if j-1 > 0:
        remove_prisoners(state, i, j-1)
    if j+1 <= BOARD_SIZE:
        remove_prisoners(state, i, j+1)

    state.move_num += 1



def is_terminal(player, state, move):
    pass

def scoring(state):
    pass
