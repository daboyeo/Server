from flask import request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.data.model.report.report import Report


class AdminReportView(Resource):
    def get(self):
        query = request.args.get("query")
        tag = request.args.get("tag")
        if query is None and tag is None:
            return {"reports": [map(report, get_jwt_identity()) for report in Report.get_all_reports()]}
        if query: return {"reports": [map(report, get_jwt_identity()) for report in Report.search_reports(query)]}
        else: return {"reports": [map(report, get_jwt_identity()) for report in Report.search_reports(tag)]}

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
