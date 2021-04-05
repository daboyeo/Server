from app.data.model.base import BaseMixin
from app.extension import db


class Report(db.Model, BaseMixin):
    __tablename__ = 'tbl_report'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(7), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    reporter_id = db.Column(db.String(255), db.ForeignKey('tbl_user.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, location, content, reporter_id):
        self.location = location
        self.content = content
        self.reporter_id = reporter_id

    @staticmethod
    def report(location, content, reporter_id):
        return Report(location, content, reporter_id).save()
