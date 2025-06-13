from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    pu = db.Column(db.Boolean, default=False, nullable=False)
    tickets = db.relationship('ActiveTicket', back_populates='user', lazy=True)

    @property
    def id(self):
        return self.user_id

    def is_admin(self):
        """Check if user has admin privileges."""
        return self.pu


class ActiveTicket(db.Model):
    __tablename__ = 'active_ticket'
    ticket_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    priority = db.Column(db.String(50), default='Normal', nullable=False)
    status = db.Column(db.String(50), default='Open', nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user = db.relationship('User', back_populates='tickets')
