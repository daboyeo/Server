import requests

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

        headers = {"Authorization": f"Bearer {payload['token']}"}
        user_inform = requests.get("https://www.googleapis.com/plus/v1/people/me", headers=headers)
        if user_inform.status_code != 200: abort(401)

        user_data = user_inform.json()

        id = f"{payload['auth_type']}@{user_data['id']}"
        if not User.find_by_id(id): User.signup(id, user_data['displayName'], user_data['image']['url'])

        return {"access_token": create_access_token(identity=id)}, 200

    @jwt_required()
    def put(self):
        payload = request.json
        User.update_profile(get_jwt_identity(), payload["name"], payload["profile_uri"])
        return {}, 200
