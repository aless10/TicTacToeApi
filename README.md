# TicTacToeServer Challenge

## Version

0.0.1.dev

## Description

Write a webserver that can take in tic tac toe boards and return a winner.
It should accept a POST request with a JSON payload. The payload should look like the following:

    {'board': [[0, 1, 2], [3, 4, 5], [6, 7, 8]]}

Each number should be either "x", "o", or "" for an empty square. The numbers correspond to the following positions:

## Examples

Some example curl calls to this endpoint along with the expected returns are as follows:
    
    $ curl -d '{"board": [["x","x","x"],["o","o", ""],["","",""]]}' -H 'Content-Type: application/json' 127.0.0.1:5000
    {"winner": "x"}

    $ curl -d '{"board": [["o","",""],["x","o", "x"],["","","o"]]}' -H 'Content-Type: application/json' 127.0.0.1:5000
    {"winner": "o"}
    
    $ curl -d '{"board": [["x","","x"],["o","o", ""],["","",""]]}' -H 'Content-Type: application/json' 127.0.0.1:5000
    {"winner": null}