import logging

from flask import request, Response
from flask.views import MethodView
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest, InternalServerError

from server.schema.schema import RequestSchema, ResponseSchema

log = logging.getLogger(__name__)


class TicTacToe(MethodView):

    def post(self):
        request_body = request.get_json(force=True)
        log.info("A new board has come: %s", request_body)
        result = {"winner": None}
        try:
            board_model = RequestSchema().load(request_body)
        except ValidationError as e:
            log.error('Failed Schema Validation: %s', e)
            status_code = BadRequest.code
        except Exception as e:
            log.error('Error while validating schema: %s', e)
            status_code = InternalServerError.code
        else:
            try:
                result = board_model.calculate_winner()
                log.info("Winner calculation result: %s", result)
                status_code = 200
            except Exception as e:
                log.exception("Exception occurred in task: %s", e)
                status_code = InternalServerError.code
        response = ResponseSchema().dump(result)
        return Response(response, status=status_code, mimetype='application/json')
