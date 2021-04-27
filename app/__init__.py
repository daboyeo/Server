from flask import Flask

from config import config


def register_extension(flask_app: Flask):
    from app import extension
    extension.db.init_app(flask_app)
    extension.jwt.init_app(flask_app)
    extension.cors.init_app(flask_app)


def register_blueprint(flask_app: Flask):
    from app.view.user import user_blueprint
    flask_app.register_blueprint(user_blueprint)

    from app.view.report import report_blueprint
    flask_app.register_blueprint(report_blueprint)


def create_table(flask_app):
    from app.extension import db
    with flask_app.app_context():
        db.create_all()


def create_app(config_name: str) -> Flask:
    flask_app = Flask("DABOYEO")
    flask_app.config.from_object(config[config_name])

    register_extension(flask_app)
    register_blueprint(flask_app)
    create_table(flask_app)

    return flask_app
