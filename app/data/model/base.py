import datetime
from app.extension import db


class BaseMixin:
    kst = datetime.timezone(datetime.timedelta(hours=9))
    created_at = db.Column(db.DateTime, server_default=db.func.now(tz=kst))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(tz=kst), server_onupdate=db.func.now(tz=kst))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()