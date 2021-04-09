from flask import request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource

from app.data.model.user.user import User


class Auth(Resource):
    @jwt_required()
    def get(self):
        user = User.find_by_id(get_jwt_identity())
        return {
            "name": user.name,
            "profile_uri": user.profile_uri
        }

    def post(self):
        payload = request.json

        # TODO GET USER INFORM BY TOKEN

        id = f"{payload['auth_type']}@{'temporary_id'}"
        if not User.find_by_id(id): User.signup(id)

        return {"access_token": create_access_token(identity=id)}, 200

    @jwt_required()
    def put(self):
        payload = request.json
        User.update_profile(get_jwt_identity(), payload["name"], payload["profile_uri"])
        return {}, 200
