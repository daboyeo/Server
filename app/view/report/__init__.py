from flask import Blueprint
from flask_restful import Api

report_blueprint = Blueprint('report', __name__, url_prefix='/report')
api = Api(report_blueprint)

from .report_view import ReportView, ReportDetail
api.add_resource(ReportView, '')
api.add_resource(ReportDetail, "/<string:id>")

from .comment_view import CommentView
api.add_resource(CommentView, '/comment')

from .sympathy_view import SympathyView
api.add_resource(SympathyView, '/sympathy')

