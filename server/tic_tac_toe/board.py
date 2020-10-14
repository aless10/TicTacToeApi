import itertools

WINNING_CASES = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)}

PLAYERS = ["x", "o"]


class Cell:

    def __init__(self, _id, player):
        self.id = _id
        self.player = player


class Board:

    def __init__(self, board):
        self.board = [Cell(i, player) for i, player in enumerate(board)]

    def check_winner_by_player(self, player):
        player_cells = sorted((cell.id for cell in self.board if cell.player and cell.player == player))
        if len(player_cells) < 3:
            return False
        player_sets = set(itertools.combinations(player_cells, 3))
        return player_sets.intersection(WINNING_CASES)

    def calculate_winner(self):
        winner = None
        for player in PLAYERS:
            if self.check_winner_by_player(player):
                winner = player
        return winner

    @classmethod
    def from_request(cls, board):
        return cls([cell for row in board for cell in row])


class BoostedBoard:

    def __init__(self, board):
        self.board = [Cell(i, player) for i, player in enumerate(board)]

    def check_winner_by_player(self, player):
        player_cells = sorted((cell.id for cell in self.board if cell.player and cell.player == player))
        if len(player_cells) < 3:
            return False
        player_sets = set(itertools.combinations(player_cells, 3))
        return player_sets.intersection(WINNING_CASES)

    def calculate_winner(self):
        winner = None
        for player in PLAYERS:
            if self.check_winner_by_player(player):
                winner = player
        return winner

    @classmethod
    def from_request(cls, board):
        return cls([cell for row in board for cell in row])
