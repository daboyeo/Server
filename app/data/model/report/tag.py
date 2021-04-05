from app.data.model.base import BaseMixin
from app.extension import db


class Tag(db.Model, BaseMixin):
    __tablename__ = 'tbl_tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(10), nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('tbl_report.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, content, report_id):
        self.content = content
        self.reporter_id = report_id

    @staticmethod
    def tag(content, report_id):
        return Tag(content, report_id).save()
