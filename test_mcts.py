from mcts import Game_Node

import numpy as np
from go_game.go import State

def create_mock_game_tree():
    # Create initial state with a 5x5 board for simplicity
    initial_position = np.zeros((5, 5), dtype=np.int8)
    root_state = State(initial_position, A_prisoners=0, B_prisoners=0, move_num=0)

    # Create root node
    root = Game_Node(root_state, p=1.0, n=10, q=0.5)

    # Create some example moves/states
    moves = [
        (0, 0), (1, 1), (0, 1), (1, 0), (2, 2)
    ]

    # Create first level children
    for i, move in enumerate(moves[:2]):
        new_position = root_state.position.copy()
        new_position[move[0], move[1]] = root_state.color()
        new_state = State(new_position,
                         A_prisoners=root_state.A_prisoners,
                         B_prisoners=root_state.B_prisoners,
                         move_num=root_state.move_num + 1)

        # Add child with varying statistics
        child = root.add_child(new_state,
                             p=0.8 - i*0.3,  # Decreasing prior
                             n=5 - i*2,       # Decreasing visit count
                             q=0.6 + i*0.1)   # Increasing Q-value

        # Add second level children to first child only
        if i == 0:
            for j, move2 in enumerate(moves[2:4]):
                new_position2 = new_state.position.copy()
                new_position2[move2[0], move2[1]] = new_state.color()
                new_state2 = State(new_position2,
                                 A_prisoners=new_state.A_prisoners,
                                 B_prisoners=new_state.B_prisoners,
                                 move_num=new_state.move_num + 1)

                # Add grandchild with varying statistics
                child.add_child(new_state2,
                              p=0.7 - j*0.2,  # Decreasing prior
                              n=3 - j,        # Decreasing visit count
                              q=0.4 + j*0.15) # Increasing Q-value

    return root

def print_game_tree(node, level=0):
    """Helper function to visualize the game tree"""
    indent = "  " * level
    print(f"{indent}Node: P={node.P:.2f}, N={node.N}, Q={node.Q:.2f}")
    print(f"{indent}Position:\n{indent}" +
          "\n{indent}".join(str(node.state.position).split('\n')))

    for child in node.children.values():
        print_game_tree(child, level + 1)

# Example usage:
if __name__ == "__main__":
    root = create_mock_game_tree()
    print("Mock Game Tree Structure:")
    print_game_tree(root)
