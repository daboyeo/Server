from app.data.model.base import BaseMixin
from app.extension import db


class Image(db.Model, BaseMixin):
    __tablename__ = 'tbl_image'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    report_id = db.Column(db.Integer, db.ForeignKey('tbl_report.id', ondelete='CASCADE'), nullable=False)
    image_uri = db.Column(db.String(255), nullable=False)

    def __init__(self, report_id, image_uri):
        self.report_id = report_id
        self.image_uri = image_uri

    @staticmethod
    def upload(report_id, image_uri):
        return Image(report_id, image_uri).save()
