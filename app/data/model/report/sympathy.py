from app.data.model.base import BaseMixin
from app.extension import db


class Sympathy(db.Model, BaseMixin):
    __tablename__ = 'tbl_sympathy'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    report_id = db.Column(db.Integer, db.ForeignKey('tbl_report.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.String(255), db.ForeignKey('tbl_user.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, user_id, report_id):
        self.user_id = user_id
        self.report_id = report_id

    @staticmethod
    def sympathy(user_id, report_id):
        return Sympathy(user_id, report_id).save()
