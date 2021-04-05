from flask import Flask

from config import config


def register_extension(flask_app: Flask):
    from app import extension
    extension.db.init_app(flask_app)
    extension.jwt.init_app(flask_app)
    extension.cors.init_app(flask_app)


def register_blueprint(flask_app: Flask):
    # from srs_server.view.apply import apply_blueprint
    # flask_app.register_blueprint(apply_blueprint)
    pass


def create_app(config_name: str) -> Flask:
    flask_app = Flask("DABOYEO")
    flask_app.config.from_object(config[config_name])

    register_extension(flask_app)
    register_blueprint(flask_app)

    return flask_app
