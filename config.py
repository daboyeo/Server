import os
from datetime import timedelta


class Config:
    SERVICE_NAME = 'DABOYEO'
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(weeks=2)
    SQLALCHEMY_DATABASE_URI = os.getenv('DABOYEO_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False



class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config = {
    'develop': DevelopmentConfig,
    'production': ProductionConfig
}