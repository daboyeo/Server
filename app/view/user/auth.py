from flask import request, abort
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from app.data.model.user.user import User


class Auth(Resource):
    def post(self):
        payload = request.json

        # TODO GET USER INFORM BY TOKEN

        id = f"{payload['auth_type']}@{'temporary_id'}"
        if not User.find_by_id(id): User.signup(id)

        return {
            "access_token": create_access_token(identity=id)
               }, 200