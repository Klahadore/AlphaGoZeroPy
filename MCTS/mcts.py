# Naive implementation in python. Maybe later I'll try to make this faster with a Cython extension or something

import typing

class Game_Node():
    def __init__(self, state, parent, p, u, n):
        self.parent = parent
        self.state = state
        self.p = p
        self.u = u
        self.n = n

        self.children = []

    def add_child(self, state):
        pass

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    # Update Node Statistics

# Fairly generic MCTS, I'm not trying to make it specific to go or anything.
class MCTS():
    def __init__(self, root_state: Game_Node):
        pass

    def simulate(self, available_moves, evaluation_func):
        pass

    def backprpagate(self):
        pass

    def select(self):
        pass
