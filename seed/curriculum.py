"""Seed and synchronize the roadmap curriculum."""

import re

from models import Course, Lesson, Module, db
from seed.roadmap import course_levels

LEVELS = course_levels()


def slug_part(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def lesson_content(course_title, topics):
    topic_list = ", ".join(topics)
    return f"""# {course_title}: getting started

In this lesson, you will learn **{topic_list}**. Start with the plain-language explanation, run each example, and change one value to see what happens.

Python is learned by experimenting. Make a prediction, run the code, inspect the result, and explain the idea in your own words.

**Practice prompt:** Build a tiny program using {topics[0]} and then improve it with {topics[1]}."""


def seed_curriculum():
    """Create missing roadmap records and synchronize existing level records."""
    for number, title, track, topics in LEVELS:
        level_number = number.split()[-1]
        slug = f"level-{level_number}-{slug_part(title)}"
        course = Course.query.filter_by(level=number).first()

        if not course:
            course = Course(
                title=f"{number} - {title}",
                slug=slug,
                description=f"{track}: {title}. A guided sequence with theory, examples, and practice.",
                level=number,
            )
            db.session.add(course)
            db.session.flush()

        course.title = f"{number} - {title}"
        course.slug = slug
        course.level = number
        course.description = f"{track}: {title}. A guided sequence with theory, examples, and practice."

        module_count = (len(topics) + 3) // 4
        for module in list(course.modules):
            if module.position > module_count:
                db.session.delete(module)

        for index in range(0, len(topics), 4):
            group = topics[index:index + 4]
            module_number = index // 4 + 1
            module_title = f"Module {module_number}: {group[0]}"
            module = Module.query.filter_by(course_id=course.id, position=module_number).first()

            if not module:
                module = Module(course=course, title=module_title, position=module_number)
                db.session.add(module)
                db.session.flush()

            module.title = module_title
            module.description = "Topics: " + ", ".join(group)
            lesson_slug = f"level-{level_number}-module-{module_number}-{slug_part(group[0])}"
            lesson = Lesson.query.filter_by(module_id=module.id, position=1).first()

            if not lesson:
                lesson = Lesson(module=module, slug=lesson_slug, position=1)
                db.session.add(lesson)

            lesson.title = f"Introduction to {group[0]}"
            lesson.slug = lesson_slug
            lesson.content = lesson_content(title, group)
            lesson.estimated_minutes = 15

    db.session.commit()


if __name__ == "__main__":
    from app import create_app

    app = create_app()
    with app.app_context():
        seed_curriculum()
        print(f"Seeded {Course.query.count()} courses, {Module.query.count()} modules, and {Lesson.query.count()} lessons.")
