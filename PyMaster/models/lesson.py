from models import db


class Lesson(db.Model):
    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey("modules.id"), nullable=False)
    title = db.Column(db.String(180), nullable=False)
    slug = db.Column(db.String(190), nullable=False, unique=True, index=True)
    content = db.Column(db.Text, nullable=False)
    position = db.Column(db.Integer, nullable=False, default=1)
    estimated_minutes = db.Column(db.Integer, nullable=False, default=10)

    module = db.relationship("Module", back_populates="lessons")
    code_examples = db.relationship("CodeExample", back_populates="lesson", cascade="all, delete-orphan")
    practice_problems = db.relationship("PracticeProblem", back_populates="lesson", cascade="all, delete-orphan")
    quiz_questions = db.relationship("QuizQuestion", back_populates="lesson", cascade="all, delete-orphan")
