from flask import Blueprint

from api.tic_tac_toe import TicTacToe
from server.api.status import Status

v1 = Blueprint('api', __name__, url_prefix='/api')

v1.add_url_rule('/status', view_func=Status.as_view('get-status'))
v1.add_url_rule('/tic-tac-toe', view_func=TicTacToe.as_view('tic-tac-toe'))
