import numpy as np


# For now, to make it easier on myself, the coordinates will be counted from matrix coordinates.
# So everything starts from top left.
class Go_Move():
    def __init__(self, x_coordinate, y_coordinate, player):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        # Player is -1 for black, 1 for white.
        self.player = player

    def __repr__(self):
        return "x:{0} y:{1} player:{2}".format(
            self.x_coordinate,
            self.y_coordinate,
            self.player
        )

class Go_State():
    def __init__(self, size=19):
        self.board = np.zeros(shape=(size, size), dtype=np.int8)


    def play_move(self, move):
        """
        Takes move, returns new game state that reflects move.
        """
        if not self.is_valid_move(move):
            return None

        new_state = Go_State()
        new_state.board = self.board

        new_state.board[move.y_coordinate][move.x_coordinate] = move.player
        return new_state


    def is_valid_move(self, move):
        """
        Takes Go_Move and checks if it is valid.
        """

        pass

    def get_valid_moves(self):
        """
        Returns a list of valid moves.
        """


        pass

    def __repr__(self):
        return np.array2string(self.board)
