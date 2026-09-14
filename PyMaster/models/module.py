from models import db


class Module(db.Model):
    __tablename__ = "modules"

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    position = db.Column(db.Integer, nullable=False, default=1)

    course = db.relationship("Course", back_populates="modules")
    lessons = db.relationship("Lesson", back_populates="module", cascade="all, delete-orphan", order_by="Lesson.position")
