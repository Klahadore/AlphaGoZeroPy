# Naive implementation in python. Maybe later I'll try to make this faster with a Cython extension or something

from typing_extensions import Self
import numpy as np
import hashlib


class Game_Node():
    def __init__(self, state, parent=None, p=0, u=0, n=0):
        self.parent = parent
        self.state = state
        self.p = p
        self.u = u
        self.n = n
        self.children = []

        self.state_hash = self._get_state_hash(state)

    def add_child(self, state, p=0, u=0, n=0):
        # Create a new child node with the current node as its parent
        child = Game_Node(state, parent=self, p=p, u=u, n=n)
        self.children.append(child)
        return child

    def clear_children_and_parent_and_reset_stats(self):
        self.children = []
        self.parent = None
        self.p = 0
        self.u = 0
        self.n = 0

    def _get_state_hash(self, state):
        state.flags.writeable = False
        return hashlib.blake2b(state.tobytes(), digest_size=16).hexdigest()





# Fairly generic MCTS, I'm not trying to make it specific to go or anything.
class MCTS():
    def __init__(self, root_node: Game_Node, exploration_constant=4):
        self.root_node = root_node
        self.exploration_constant = exploration_constant


    def simulate(self, evaluation_func, get_next_state_func):
        # for i in available_moves():
        #     next_state = get_next_state_func(i)
        #     p, v = evaluation_func(next_state)

        current_node = self.root_node
        while current_node.state.is_terminal() == False:
            available_moves = current_node.state.legal_actions()
            p, v = evaluation_func(current_node.state)
            next_move = UCT(current_node, available_moves)
            if new_state =


    def backprpagate(self):
        pass

    # Return move, no, return distribution for things.
    def select(self):

        return

    # Calculates upper confidence bound for all next moves
    # evaluation_func is the neural network that returns a vector of length 360 (probabilities for each move), and scalar value prediction iof current state
    def _UCT(self, node, available_moves):

        sum_of_children_n = lambda node: sum(child.n for child in node.children)
        uct = lambda node: node.q + self.exploration_constant * ((node.p * sum_of_children_n(node)) / (1 + node.n))

        uct_scores = {}
        for i in available_moves(node):
            uct_scores[i] = uct(i)

        return max(uct_scores, key=uct_scores.get)
