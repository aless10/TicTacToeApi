import logging

from server.api.tic_tac_toe import TicTacToe
from server.schema.schema import BoostRequestSchema

log = logging.getLogger(__name__)


class BoostTicTacToe(TicTacToe):

    request_schema = BoostRequestSchema
