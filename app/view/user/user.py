import requests

from flask import request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource

from app.data.model.user.user import User


class UserView(Resource):
    @jwt_required()
    def get(self):
        id = request.args.get("id")

        if id is None:
            user = User.find_by_id(get_jwt_identity())
        else:
            user = User.find_by_id(id)
            if user is None:
                abort(404)

        return {
            "name": user.name,
            "profile_uri": user.profile_uri
        }

    @jwt_required()
    def put(self):
        payload = request.json
        User.update_profile(get_jwt_identity(), payload["name"], payload["profile_uri"])
        return {}, 200
