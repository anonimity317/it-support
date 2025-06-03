from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    password = db.Column(db.String(250))
    pu = db.Column(db.Boolean, default=False)
    tickets = db.relationship('ActiveTicket', lazy=True)

class ActiveTicket(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    title = db.Column(db.String(100))
    content = db.Column(db.String(500))
    priority = db.Column(db.String(50), default='Normal')
    status = db.Column(db.String(50), default='Open')
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

