from flask import request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.data.model.report.comment import Comment
from app.data.model.report.image import Image
from app.data.model.report.report import Report
from app.data.model.report.sympathy import Sympathy
from app.data.model.user.user import User
from app.data.model.report.tag import Tag


class ReportView(Resource):
    def get(self):
        query = request.args.get("query")
        tag = request.args.get("tag")
        user = request.args.get("user")
        if query is None and tag is None and user is None:
            return {"reports": [map(report, get_jwt_identity()) for report in Report.get_all_reports()]}
        if query: return {"reports": [map(report, get_jwt_identity()) for report in Report.search_reports(query)]}
        elif tag: return {"reports": [map(report, get_jwt_identity()) for report in Report.search_reports_by_tag(tag)]}
        else: return {"reports": [map(report, get_jwt_identity()) for report in Report.search_reports_by_user(user)]}

    @jwt_required()
    def post(self):
        payload = request.json
        report = Report.report(payload.location, payload.content, get_jwt_identity(), payload.image_uris, payload.tags)
        return {
            "report_id": report.id
        }, 201

    @jwt_required()
    def put(self):
        payload = request.json
        report = Report.get_by_id(payload.report_id)

        if not report: abort(404)
        if report.reporter_id != get_jwt_identity(): abort(401)

        report.update_report(payload.location, payload.content, payload.image_uris, payload.tags)
        return {
            "report_id": report.id
        }, 200

    @jwt_required()
    def delete(self):
        payload = request.json
        report = Report.get_by_id(payload.report_id)
        report.delete()
        return {
            "report_id": report.id
        }, 200


class ReportDetail(Resource):
    def get(self, id):
        report = Report.get_by_id(id)
        reporter = User.find_by_id(report.reporter_id)
        return {
            "report_id": report.id,
            "reporter_name": reporter.name,
            "reporter_profile_uri": reporter.profile_uri,
            "content": report.content,
            "tags": [tag.content for tag in Tag.get_by_report_id(report.id)],
            "image_uris": [image.image_uri for image in Image.get_by_report_id(report.id)],
            "comments": [map_comment(comment) for comment in Comment.get_by_report_id(report.id)],
            "num_of_sympathy": len(Sympathy.get_by_report_id(report.id)),
            "is_sympathy": Sympathy.is_sympathy(get_jwt_identity(), report.id),
            "created_at": report.created_at,
            "updated_at": report.updated_at,
            "location": report.location
        }


def map_comment(comment):
    user = User.find_by_id(comment.user_id)
    return {
        "comment_id": comment.id,
        "user_id": user.id,
        "profile_uri": user.profile_uri,
        "name": user.name,
        "content": comment.content
    }


def map(report: Report, user_id):
    reporter = User.find_by_id(report.reporter_id)
    return {
        "report_id": report.id,
        "reporter_name": reporter.name,
        "reporter_profile_uri": reporter.profile_uri,
        "reporter_id": reporter.id,
        "content": report.content,
        "tags": [tag.content for tag in Tag.get_by_report_id(report.id)],
        "image_uris": [image.image_uri for image in Image.get_by_report_id(report.id)],
        "num_of_sympathy": len(Sympathy.get_by_report_id(report.id)),
        "is_sympathy": Sympathy.is_sympathy(user_id, report.id),
        "created_at": report.created_at,
        "updated_at": report.updated_at,
        "location": report.location
    }
