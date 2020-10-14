import pytest
from flask import url_for
from werkzeug.exceptions import BadRequest


def test_bad_request_missing_key(client):
    bad_request_body = {
        "not expected key": []
    }
    response = client.post(url_for('api.boost-tic-tac-toe'), json=bad_request_body)
    assert response.status_code == BadRequest.code


def test_bad_request_wrong_body(client):
    bad_request_body = {
        "board": "not a valid list"
    }
    response = client.post(url_for('api.boost-tic-tac-toe'), json=bad_request_body)
    assert response.status_code == BadRequest.code


@pytest.mark.parametrize("board_input, expected", [
    ({"board": [["x", "x", "x"], ["o", "o", ""], ["", "", ""]]}, {"winner": "x"}),
    ({"board": [["o", "", ""], ["x", "o", "x"], ["", "", "o"]]}, {"winner": "o"}),
    ({"board": [["x", "", "x"], ["o", "o", ""], ["", "", ""]]}, {"winner": None})])
def test_winner(board_input, expected, client):
    response = client.post(url_for('api.boost-tic-tac-toe'), json=board_input)
    assert response.status_code == 200
    assert response.json == expected
