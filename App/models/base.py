from datetime import datetime

from App import db


class Base(db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.utcnow
    )

    def to_json(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

