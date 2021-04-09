from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.data.model.report.comment import Comment


class CommentView(Resource):
    @jwt_required()
    def post(self):
        payload = request.json
        comment = Comment.comment(payload["content"], payload["report_id"], get_jwt_identity())
        return {
            "comment_id": comment.id,
            "content": comment.content,
            "report_id": comment.report_id
        }, 201