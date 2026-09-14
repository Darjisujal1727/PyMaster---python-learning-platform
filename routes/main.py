from random import SystemRandom
from flask import Blueprint, redirect, render_template, request, url_for
from sqlalchemy import or_

from models import Course, Lesson
from seed.roadmap import ROADMAP_LEVELS as ROADMAP_CURRICULUM
from services.example_bank import (
    EXAMPLES,
    get_example,
    grouped_examples,
    neighbors,
    resolve_prereqs,
)
from services.lesson_content import guide
from services.practice_bank import (
    HELPER,
    PROBLEMS,
    get_problem,
    grouped_problems,
)
from services.practice_bank import neighbors as practice_neighbors
from services.project_bank import (
    PROJECTS,
    get_project,
    grouped_projects,
)
from services.project_bank import neighbors as project_neighbors
from services.quiz_bank import QUESTION_BANKS, QUESTIONS_PER_QUIZ, QUIZZES

main_bp = Blueprint("main", __name__)

RNG = SystemRandom()

ROADMAP_LEVELS = [(level, title) for level, title, _ in ROADMAP_CURRICULUM]


def build_quiz(topic):
    title, category = QUIZZES[topic]
    selected = RNG.sample(QUESTION_BANKS[topic], QUESTIONS_PER_QUIZ)
    randomized = []
    for question, options, correct, explanation in selected:
        answer = options[correct]
        shuffled_options = list(options)
        RNG.shuffle(shuffled_options)
        randomized.append((question, shuffled_options, shuffled_options.index(answer), explanation))
    return title, category, randomized


@main_bp.get("/")
def home():
    return render_template("home.html")


@main_bp.get("/learn")
def learn():
    query = request.args.get("q", "").strip()
    roadmap_numbers = [f"Level {level}" for level, _, _ in ROADMAP_CURRICULUM]
    courses = Course.query.filter(Course.level.in_(roadmap_numbers)).order_by(Course.id).all()
    setup_lesson = Lesson.query.filter_by(title="Introduction to Installing Python").first()
    results = (
        Lesson.query.filter(
            or_(
                Lesson.title.ilike(f"%{query}%"),
                Lesson.content.ilike(f"%{query}%"),
            )
        )
        .order_by(Lesson.title)
        .all()
        if query
        else []
    )
    return render_template(
        "learn.html",
        courses=courses,
        query=query,
        results=results,
        setup_lesson=setup_lesson,
    )


@main_bp.get("/lessons/<slug>")
def lesson(slug):
    current = Lesson.query.filter_by(slug=slug).first_or_404()
    course = current.module.course
    lessons = [x for m in course.modules for x in m.lessons]
    index = lessons.index(current)
    return render_template(
        "lesson.html",
        lesson=current,
        course=course,
        modules=course.modules,
        guide=guide(current),
        previous=lessons[index - 1] if index else None,
        next_lesson=lessons[index + 1] if index + 1 < len(lessons) else None,
        progress=round((index + 1) / len(lessons) * 100),
    )


@main_bp.get("/quizzes")
def quizzes():
    return render_template("quizzes.html", quizzes=QUIZZES)


@main_bp.get("/quizzes/<topic>")
def quiz(topic):
    if topic not in QUIZZES:
        return ("Quiz not found", 404)
    return render_template("quiz.html", topic=topic, quiz=build_quiz(topic))


@main_bp.get("/examples")
def examples():
    return redirect(url_for("main.example", slug=EXAMPLES[0]["slug"]))


@main_bp.get("/examples/<slug>")
def example(slug):
    current = get_example(slug)
    if not current:
        return ("Example not found", 404)
    previous, nxt = neighbors(slug)
    return render_template(
        "example.html",
        example=current,
        groups=grouped_examples(),
        previous=previous,
        next_example=nxt,
        prereqs=resolve_prereqs(current),
        example_count=len(EXAMPLES),
    )


@main_bp.get("/practice")
def practice():
    return redirect(url_for("main.practice_problem", slug=PROBLEMS[0]["slug"]))


@main_bp.get("/practice/<slug>")
def practice_problem(slug):
    current = get_problem(slug)
    if not current:
        return ("Practice problem not found", 404)
    previous, nxt = practice_neighbors(slug)
    return render_template(
        "practice.html",
        problem=current,
        groups=grouped_problems(),
        previous=previous,
        next_problem=nxt,
        problem_count=len(PROBLEMS),
        helper=HELPER,
    )


@main_bp.get("/projects")
def projects():
    query = request.args.get("q", "").strip().lower()
    level_filter = request.args.get("level", "").strip()

    filtered_projects = PROJECTS
    if query:
        filtered_projects = [
            p
            for p in filtered_projects
            if query in p["title"].lower()
            or query in p["summary"].lower()
            or query in p["category"].lower()
            or any(query in c.lower() for c in p["concepts"])
        ]
    if level_filter:
        filtered_projects = [p for p in filtered_projects if p["level"].lower() == level_filter.lower()]

    return render_template(
        "projects.html",
        projects=filtered_projects,
        project_groups=grouped_projects(filtered_projects),
        project_count=len(PROJECTS),
        query=query,
        selected_level=level_filter,
    )


@main_bp.get("/projects/<slug>")
def project_detail(slug):
    project = get_project(slug)
    if not project:
        return ("Project not found", 404)
    previous, nxt = project_neighbors(slug)
    return render_template(
        "project.html",
        project=project,
        previous=previous,
        next_project=nxt,
        project_count=len(PROJECTS),
    )


@main_bp.get("/roadmap")
def roadmap():
    return render_template("roadmap.html", roadmap_levels=ROADMAP_LEVELS)


@main_bp.get("/playground")
def playground():
    return render_template("playground.html")


@main_bp.get("/health")
def health():
    return {"status": "ok", "application": "PyMaster"}
