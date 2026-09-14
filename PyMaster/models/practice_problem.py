from models import db


class PracticeProblem(db.Model):
    __tablename__ = "practice_problems"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    starter_code = db.Column(db.Text)
    solution_code = db.Column(db.Text)
    difficulty = db.Column(db.String(30), nullable=False, default="Beginner")

    lesson = db.relationship("Lesson", back_populates="practice_problems")
