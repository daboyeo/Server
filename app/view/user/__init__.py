from flask import Blueprint
from flask_restful import Api

user_blueprint = Blueprint('user', __name__, url_prefix='/user')
api = Api(user_blueprint)

from .auth import Auth
api.add_resource(Auth, '/auth')