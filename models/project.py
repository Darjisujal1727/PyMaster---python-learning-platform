from models import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    title = db.Column(db.String(180), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text)
    difficulty = db.Column(db.String(30), nullable=False, default="Beginner")
    repository_url = db.Column(db.String(255))

    course = db.relationship("Course", back_populates="projects")
