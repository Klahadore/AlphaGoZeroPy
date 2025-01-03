import numpy as np

from go import State, get_legal_moves, move_to_index, dfs_for_liberties, apply_move
import go

def test_move_to_index():
    go.BOARD_SIZE = 9
    assert move_to_index(0) == (0, 0)  # top left
    assert move_to_index(8) == (0, 8)  # top right (9x9 board)
    assert move_to_index(9) == (1, 0)  # start of second row
    assert move_to_index(80) == (8, 8)  # bottom right

def test_get_legal_moves():
    go.BOARD_SIZE = 3
    position = [[0, 0, 1],
                [2, 1, 0],
                [0, 1, 2]]
    test_state = State(np.asarray(position), 0, 0, move_num=30)
    legal_moves = get_legal_moves(test_state)
    expected_moves = np.asarray([0, 1, 5, 6, 9])
    assert np.array_equal(legal_moves, expected_moves), f"expected moves: {expected_moves}, got: {legal_moves}"

def test_dfs_for_liberties():
    go.BOARD_SIZE = 5

    position = [[0, 0, 1, 2, 2],
                [0, 1, 2, 2, 2],
                [0, 0, 1, 2, 2],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1]]

    evaluation, indices = dfs_for_liberties(0, 3, np.asarray(position), 2, None)
    assert evaluation == False
    assert indices == {(0,3), (0,4), (1,2), (1,3), (1,4), (2,3), (2,4)}

    evaluation, indices = dfs_for_liberties(1,1, np.asarray(position), 1, None)
    assert evaluation == True
    assert indices == {(1,1)}

    evaluation, indices = dfs_for_liberties(4,4, np.asarray(position), 1, None)
    assert evaluation == True

def test_apply_move():
    go.BOARD_SIZE = 5

    position = [[0, 0, 1, 2, 2],
                [0, 1, 2, 2, 2],
                [0, 0, 0, 2, 2],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1]]
    expected_position = [[0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1],
                        [0, 0, 0, 1, 1]]
    state = State(np.asarray(position), 0, 0, 3)
    apply_move(state, 12)
    assert np.array_equal(np.asarray(expected_position), state.position)
    assert state.A_prisoners == 7
    assert state.move_num == 4
