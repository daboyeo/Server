from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.data.model.report.sympathy import Sympathy


class SympathyView(Resource):
    @jwt_required()
    def put(self):
        payload = request.json
        sympathy = Sympathy.sympathy(get_jwt_identity(), payload["report_id"])
        return {
            "result": bool(sympathy)
        }, 200
