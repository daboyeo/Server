from app.data.model.base import BaseMixin
from app.extension import db


class Comment(db.Model, BaseMixin):
    __tablename__ = 'tbl_comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(100), nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('tbl_report.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.String(255), db.ForeignKey('tbl_user.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, content, report_id, user_id):
        self.content = content
        self.report_id = report_id
        self.user_id = user_id

    @staticmethod
    def comment(content, report_id, user_id):
        return Comment(content, report_id, user_id).save()

    @staticmethod
    def get_by_report_id(report_id):
        return Comment.query.filter_by(report_id=report_id).all()