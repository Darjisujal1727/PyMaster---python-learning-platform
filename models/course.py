from datetime import datetime

from models import db


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, unique=True)
    slug = db.Column(db.String(160), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=False)
    level = db.Column(db.String(30), nullable=False, default="Beginner")
    thumbnail = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    modules = db.relationship("Module", back_populates="course", cascade="all, delete-orphan", order_by="Module.position")
    projects = db.relationship("Project", back_populates="course", cascade="all, delete-orphan")
