from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.course import Course
from models.module import Module
from models.lesson import Lesson
from models.code_example import CodeExample
from models.practice_problem import PracticeProblem
from models.quiz_question import QuizQuestion
from models.project import Project

__all__ = [
    "db", "Course", "Module", "Lesson", "CodeExample",
    "PracticeProblem", "QuizQuestion", "Project",
]
