# Naive implementation in python. Maybe later I'll try to make this faster with a Cython extension or something

import math
from typing_extensions import Self
import numpy as np
import hashlib

from go_game import go

class Game_Node():
    def __init__(self, state, p, n, q, parent=None):
        self.parent = parent
        self.state = state
        self.P = p
        self.N = n
        self.Q = q
        self.children = []

        self.position_hash = state.get_position_hash(state)

    def add_child(self, state, p, n, q):
        # Create a new child node with the current node as its parent
        child = Game_Node(state, p, n, q, parent=self)
        self.children.append(child)
        return child

    def clear_children_and_parent_and_reset_stats(self):
        self.children = []
        self.parent = None
        self.p = 0
        self.u = 0
        self.n = 0

    def get_legal_moves(self) -> np.ndarray:
        return go.get_legal_moves(self.state.position)

    def is_terminal(self) -> bool:
        pass


# Fairly generic MCTS, I'm not trying to make it specific to go or anything.
class MCTS():
    def __init__(self, tree: Game_Node, nn,  exploration_constant=4):
        self.tree = tree
        self.exploration_constant = exploration_constant

        self.nn = nn # neural network function
    def simulate(self, evaluation_func, get_next_state_func):

        available_moves = self.tree.get_legal_moves()
        while not self.tree.is_terminal():



    def backprpagate(self):
        pass

    # Return move, no, return distribution for things.
    def select(self):

        return

    def _UCT(self, node: Game_Node, moves: np.ndarray) -> np.ndarray:
        # we need the sum of n from all other moves
        N_b = 0
        for i in node.children:
            N_b += i.N

        uct_func = lambda p, q, n: q + self.exploration_constant * (p * math.sqrt(N_b-n)) / (1 + n)

        move_to_uct = {}
        for move in moves:
            new_state = go.apply_move(node.state, move)
            state_hash = get_state_hash()

            move_to_uct[move] = uct_func(new_state.p)
