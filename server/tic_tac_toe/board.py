import abc
import itertools
from collections import defaultdict
from typing import Optional, Union

WINNING_CASES = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)}

PLAYERS = ["x", "o"]


class TwoWinnersException(Exception):
    pass


class Cell:

    def __init__(self, _id: int, player: str) -> None:
        self.id = _id
        self.player = player


class BaseBoard:

    @abc.abstractmethod
    def check_winner_by_player(self, player: Union[str, tuple]) -> bool:
        pass

    @abc.abstractmethod
    def calculate_winner(self) -> Optional[str]:
        pass

    @classmethod
    @abc.abstractmethod
    def from_request(cls, board: list):
        pass


class Board(BaseBoard):

    def __init__(self, board: list):
        self.board = [Cell(i, player) for i, player in enumerate(board)]

    def check_winner_by_player(self, player: str):
        player_cells = sorted((cell.id for cell in self.board if cell.player and cell.player == player))
        if len(player_cells) < 3:
            return False
        player_sets = set(itertools.combinations(player_cells, 3))
        return player_sets.intersection(WINNING_CASES)

    def calculate_winner(self):
        winner = None
        counter = 0
        for player in PLAYERS:
            if self.check_winner_by_player(player):
                counter += 1
                winner = player
        if counter > 1:
            raise TwoWinnersException("Two winners are not allowed")
        return winner

    @classmethod
    def from_request(cls, board):
        return cls([cell for row in board for cell in row])


class BoostedBoard(BaseBoard):

    def __init__(self, board: dict):
        self.board = {k: tuple(v) for k, v in board.items()}

    def check_winner_by_player(self, positions: tuple):
        if len(positions) < 3:
            return False
        return positions in WINNING_CASES

    def calculate_winner(self):
        winner = None
        for player, positions in self.board.items():
            if self.check_winner_by_player(positions):
                winner = player
        return winner

    @classmethod
    def from_request(cls, board):
        players = defaultdict(list)
        for i, row in enumerate(board):
            for j, symbol in enumerate(row):
                if symbol:
                    players[symbol].append(3 * i + j)

        return cls(players)
