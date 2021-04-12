from app.data.model.base import BaseMixin
from app.extension import db


class User(db.Model, BaseMixin):
    __tablename__ = 'tbl_user'
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(4), nullable=False)
    profile_uri = db.Column(db.String(255), nullable=True)

    def __init__(self, id, name, profile_uri):
        self.id = id
        self.name = name
        self.profile_uri = profile_uri

    @staticmethod
    def signup(id, name, profile_uri):
        return User(id, name, profile_uri).save()

    @staticmethod
    def find_by_id(id):
        return User.query.filter_by(id=id).first()

    @staticmethod
    def update_profile(id, name, profile_uri):
        user = User.query.filter_by(id=id).first()
        user.name = name
        user.profile_uri = profile_uri
        user.save()
        return user
