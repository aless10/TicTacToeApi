from flask import Blueprint

from server.api.boost_tic_tac_toe import BoostTicTacToe
from server.api.tic_tac_toe import TicTacToe
from server.api.status import Status

v1 = Blueprint('api', __name__, url_prefix='/api')

v1.add_url_rule('/status', view_func=Status.as_view('get-status'))
v1.add_url_rule('/tic-tac-toe', view_func=TicTacToe.as_view('tic-tac-toe'))
v1.add_url_rule('/boost-tic-tac-toe', view_func=BoostTicTacToe.as_view('boost-tic-tac-toe'))
