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
        self.children = dict()

        self.position_hash = state.get_position_hash(state)

    def add_child(self, state, p, n, q):
        # Create a new child node with the current node as its parent
        child = Game_Node(state, p, n, q, parent=self)
        self.children[child.position_hash] = child
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



        while not self.tree.is_terminal():

            pass


    def backprpagate(self):
        pass

    # Return move, no, return distribution for things.
    def select(self):

        return


    # Returns the move with the highest UCT score
    def _one_layer_simulate(self, start_node: Game_Node) -> int:
        N_b = 0
        for child in start_node.children.values():
            N_b += child.N

        uct_func = lambda p, q, n: q + self.exploration_constant * (p * math.sqrt(N_b)) / (1 + n)

        available_moves = start_node.get_legal_moves()
        move_UCT_map = {}
        for move in available_moves:
            state = go.apply_move(start_node.state, move)
            hash = go.get_position_hash(state.position)
            if hash in start_node.children:
                child = start_node.children[hash]
                move_UCT_map[move] = uct_func(child.p, child.q, child.n)
            else:
                p, _ = self.nn(state)
                move_UCT_map[move] = uct_func(p, 0, 0)


        return max(move_UCT_map, key=move_UCT_map.get)
