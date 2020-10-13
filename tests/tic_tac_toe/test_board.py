from server.tic_tac_toe.board import Board


def test_board_init():
    """It should initialize a board"""

    test_board = ["x", "x", "o", "x", "", "o", "", "", "o"]
    instance = Board(test_board)
    assert len(instance.board) == 9


def test_board_from_request():
    """It should initialize a board from request body"""

    test_board = [["x", "x", "o"], ["x", "", "o"], ["", "", "o"]]
    instance = Board.from_request(test_board)
    assert len(instance.board) == 9
