import pytest
from flask import url_for
from werkzeug.exceptions import BadRequest


def test_bad_request_missing_key(client):
    bad_request_body = {
        "not expected key": []
    }
    response = client.post(url_for('api.tic-tac-toe'), json=bad_request_body)
    assert response.status_code == BadRequest.code


def test_bad_request_wrong_body(client):
    bad_request_body = {
        "board": "not a valid list"
    }
    response = client.post(url_for('api.tic-tac-toe'), json=bad_request_body)
    assert response.status_code == BadRequest.code


def test_bad_request_not_three_by_three_board(client):
    bad_request_body = {
        "board": [["x", "x", "x"], ["o", "o", ""]]
    }
    response = client.post(url_for('api.tic-tac-toe'), json=bad_request_body)
    assert response.status_code == BadRequest.code


def test_bad_request_bad_symbol(client):
    """It should respond with 400 and body winner: None"""
    bad_request_body = {
        "board": [["x", "x", "x"], ["o", "o", ""], [42, "", ""]]
    }
    response = client.post(url_for('api.tic-tac-toe'), json=bad_request_body)
    assert response.json == {"winner": None}


def test_two_winners_on_board(client):
    bad_request_body = {
        "board": [["x", "x", "x"], ["o", "o", "o"], ["", "", ""]]
    }
    response = client.post(url_for('api.tic-tac-toe'), json=bad_request_body)
    assert response.status_code == 400
    assert response.json == {"winner": None}


@pytest.mark.parametrize("board_input, expected", [
    ({"board": [["x", "x", "x"], ["o", "o", ""], ["", "", ""]]}, {"winner": "x"}),
    ({"board": [["o", "", ""], ["x", "o", "x"], ["", "", "o"]]}, {"winner": "o"}),
    ({"board": [["x", "", "x"], ["o", "o", ""], ["", "", ""]]}, {"winner": None})])
def test_winner(board_input, expected, client):
    response = client.post(url_for('api.tic-tac-toe'), json=board_input)
    assert response.status_code == 200
    assert response.json == expected
