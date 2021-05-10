from app.data.model.base import BaseMixin
from app.data.model.report.image import Image
from app.data.model.report.tag import Tag
from app.extension import db


class Report(db.Model, BaseMixin):
    __tablename__ = 'tbl_report'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    reporter_id = db.Column(db.String(255), db.ForeignKey('tbl_user.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, location, content, reporter_id):
        self.location = location
        self.content = content
        self.reporter_id = reporter_id

    @staticmethod
    def get_all_reports():
        return Report.query.all()

    @staticmethod
    def search_reports(query):
        return Report.query.filter(Report.content.like(f'%{query}%')).all()

    @staticmethod
    def search_reports_by_tag(tag):
        v = []
        for t in Tag.get_by_content(tag):
            v += Report.query.filter(Report.get_by_id(t.report_id)).all()
        return v

    @staticmethod
    def search_reports_by_user(user):
        return Report.query.filter_by(reporter_id=user).all()

    @staticmethod
    def get_by_id(report_id):
        return Report.query.filter_by(report_id=report_id).first()

    @staticmethod
    def report(location, content, reporter_id, image_uris, tags):
        report = Report(location, content, reporter_id).save()
        for image_uri in image_uris: Image.upload(report.id, image_uri)
        for tag in tags: Tag.tag(tag, report.id)
        return report

    def update_report(self, location, content, image_uris, tags):
        self.location = location
        self.content = content
        self.save()
        for image_uri in Image.get_by_report_id(self.id): image_uri.delete()
        for tag in Tag.get_by_report_id(self.id): tag.delete()
        for image_uri in image_uris: Image.upload(self.id, image_uri)
        for tag in tags: Tag.tag(tag, self.id)
