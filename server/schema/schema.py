import json

from marshmallow import Schema, fields, post_load, pre_dump, post_dump

from tic_tac_toe.board import Board


class RequestSchema(Schema):
    board = fields.List(fields.List(fields.String()), required=True)

    @post_load
    def make_request(self, data, **kwargs):
        return Board.from_request(data["board"])


class ResponseSchema(Schema):
    winner = fields.String(required=True)

    @pre_dump
    def serialize_response(self, result, **kwargs):
        return {"winner": result}

    @post_dump
    def to_json(self, data, **kwargs):
        return json.dumps(data)

