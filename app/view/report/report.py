from flask import request, abort
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.data.model.user.user import User


class Report(Resource):
    def post(self):
        payload = request.json