import requests

from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from app.data.model.user.user import User


class Auth(Resource):
    def post(self):
        payload = request.json

        headers = {"Authorization": f"Bearer {payload['token']}"}
        user_inform = requests.get("https://www.googleapis.com/oauth2/v3/userinfo", headers=headers)
        if user_inform.status_code != 200:
            return {
                "debug": True,
                "error_message": user_inform.text,
                "error_status": user_inform.status_code
            }, 401

        user_data = user_inform.json()

        id = f"{payload['auth_type']}@{user_data['sub']}"
        if not User.find_by_id(id): User.signup(id, user_data['name'], user_data['picture'])

        return {"access_token": create_access_token(identity=id)}, 200
