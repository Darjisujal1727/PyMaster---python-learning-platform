from models import db


class CodeExample(db.Model):
    __tablename__ = "code_examples"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    code = db.Column(db.Text, nullable=False)
    explanation = db.Column(db.Text)
    language = db.Column(db.String(30), nullable=False, default="python")

    lesson = db.relationship("Lesson", back_populates="code_examples")
