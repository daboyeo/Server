from app.data.model.base import BaseMixin
from app.extension import db


class User(db.Model, BaseMixin):
    __tablename__ = 'tbl_user'
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(4), nullable=False)
    profile_uri = db.Column(db.String(50), nullable=True)

    def __init__(self, id, name, profile_uri):
        self.id = id
        self.name = name
        self.profile_uri = profile_uri

    @staticmethod
    def signup(ud, name, number):
        return User(id, name, number).save()

    @staticmethod
    def find_by_id(id):
        return User.query.filter_by(id=id).first()
