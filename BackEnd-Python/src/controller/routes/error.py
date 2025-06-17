from werkzeug.exceptions import HTTPException
from flask import json

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        response = e.get_response()
        response.data = json.dumps({
            'code': e.code,
            'name': e.name,
            'message': e.description,
        })
        response.content_type = "application/json"
        return response