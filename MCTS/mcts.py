# Naive implementation in python. Maybe later I'll try to make this faster with a Cython extension or something

from typing_extensions import Self
import numpy as np
# I added my own Stack implementation for performance when moving to Cython
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



class Game_Node():
    def __init__(self, state, parent=None, p=0, u=0, n=0):
        self.parent = parent
        self.state = state
        self.p = p
        self.u = u
        self.n = n
        self.children = []

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


    def backprpagate(self):
        pass

    def select(self):
        pass

    # Calculates upper confidence bound for all next moves
    # evaluation_func is the neural network that returns a vector of length 360 (probabilities for each move), and scalar value prediction iof current state
    def _UCT(self, node, available_moves, evaluation_func):
        uct = lambda node: node.q + self.exploration_constant * (node.p / (1 + node.n))

        p, v = evaluation_func(node.state)
        uct_scores = []
        for i in available_moves():
            uct_scores.append((i, uct(node)))

        return uct_scores
