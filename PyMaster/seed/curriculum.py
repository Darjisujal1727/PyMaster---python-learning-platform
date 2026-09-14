"""Scalable curriculum seed data for PyMaster."""
from app import create_app
import re
from models import db, Course, Module, Lesson

LEVELS = [
    ("Level 0", "Programming Fundamentals", "ZERO KNOWLEDGE", ["What is a computer?", "What is software?", "What is programming?", "Programming languages", "Algorithms", "Flowcharts", "Source code", "Compiler and interpreter", "What is Python?", "Why Python?", "Where Python is used", "Python careers", "Installing Python", "Installing VS Code", "Running Python", "First Python program"]),
    ("Level 1", "Python Fundamentals", "PYTHON BEGINNER", ["Syntax", "Comments", "Variables and constants", "Naming conventions", "Data types", "int and float", "string, boolean and None", "type() and conversion", "input() and print()", "Escape characters", "Arithmetic and assignment operators", "Comparison and logical operators", "Identity and membership operators", "Operator precedence"]),
    ("Level 2", "Conditional Logic", "PYTHON BEGINNER", ["if", "if/else", "if/elif/else", "Nested conditions", "Conditional expressions", "Combining conditions"]),
    ("Level 3", "Loops", "PYTHON BEGINNER", ["for", "while", "range()", "Nested loops", "break", "continue", "pass", "loop else", "infinite loops"]),
    ("Level 4", "Strings", "PYTHON BEGINNER", ["String creation", "Indexing and negative indexing", "Slicing", "Concatenation and repetition", "Formatting and f-strings", "String methods", "Searching and replacing", "Splitting and joining", "Stripping and case conversion"]),
    ("Level 5", "Lists", "PYTHON BEGINNER", ["Creating lists", "Indexing and slicing", "Updating and adding", "Removing and searching", "Sorting, reversing and copying", "Nested lists", "List methods", "List comprehension"]),
    ("Level 6", "Tuples", "PYTHON BEGINNER", ["Creation", "Indexing and slicing", "Immutability", "Methods", "Tuple unpacking", "Nested tuples"]),
    ("Level 7", "Sets", "PYTHON BEGINNER", ["Creating sets", "Adding and removing", "Union", "Intersection", "Difference", "Symmetric difference", "Membership"]),
    ("Level 8", "Dictionaries", "PYTHON BEGINNER", ["Creating dictionaries", "Keys and values", "Accessing", "Adding and updating", "Removing", "Dictionary methods", "Nested dictionaries", "Dictionary comprehension"]),
    ("Level 9", "Functions", "PYTHON INTERMEDIATE", ["Why functions?", "Creating and calling functions", "Parameters and arguments", "Return values", "Default and keyword arguments", "*args and **kwargs", "Scope", "Local and global variables", "Recursion", "Lambda", "Higher-order functions"]),
    ("Level 10", "Comprehensions", "PYTHON INTERMEDIATE", ["List comprehension", "Set comprehension", "Dictionary comprehension", "Conditional comprehension", "Nested comprehension"]),
    ("Level 11", "Exception Handling", "PYTHON INTERMEDIATE", ["Errors and exceptions", "try and except", "else and finally", "Multiple exceptions", "raise", "Custom exceptions"]),
    ("Level 12", "File Handling", "PYTHON INTERMEDIATE", ["Reading files", "Writing files", "Append", "File modes", "with", "CSV", "JSON"]),
    ("Level 13", "Modules and Packages", "PYTHON INTERMEDIATE", ["import", "from import", "aliases", "Built-in modules", "Custom modules", "Packages", "__name__ and __main__", "pip", "Virtual environments"]),
    ("Level 14", "Object-Oriented Programming", "PYTHON INTERMEDIATE", ["OOP", "Classes and objects", "Attributes and methods", "Constructors and self", "Instance and class variables", "Instance, class and static methods", "Encapsulation", "Inheritance", "Multiple and multilevel inheritance", "Polymorphism and overriding", "Abstraction and abstract classes", "Composition"]),
    ("Level 15", "Advanced Python", "PYTHON ADVANCED", ["Iterators and generators", "yield", "Decorators", "Closures", "Context managers", "Magic methods", "Dataclasses", "Type hints", "Enumerations", "Functional programming", "map(), filter() and reduce()"]),
    ("Level 16", "Regular Expressions", "PYTHON ADVANCED", ["Regex basics", "Patterns and character classes", "Quantifiers", "Groups", "Search and match", "Findall", "Replace"]),
    ("Level 17", "Data Structures and Algorithms", "PYTHON ADVANCED", ["Arrays", "Stacks and queues", "Linked lists", "Hash tables", "Trees and graphs", "Heaps", "Searching and sorting", "Recursion", "BFS and DFS", "Time and space complexity"]),
    ("Level 18", "Databases", "PROFESSIONAL PYTHON", ["Database concepts", "SQLite", "Python SQLite", "CRUD", "SQL", "Parameterized queries", "Transactions", "Database design"]),
    ("Level 19", "APIs", "PROFESSIONAL PYTHON", ["API concepts", "HTTP", "GET and POST", "PUT and DELETE", "JSON", "Requests", "API error handling"]),
    ("Level 20", "Python Web Development", "PROFESSIONAL PYTHON", ["Web basics and HTTP", "Flask", "Routes", "Templates and Jinja", "Forms", "Static files", "CRUD and SQLite", "REST APIs", "Deployment concepts"]),
    ("Level 21", "Automation", "PROFESSIONAL PYTHON", ["File automation", "Folder automation", "CSV automation", "Excel automation", "PDF processing", "Email automation concepts", "Web automation concepts"]),
    ("Level 22", "Python Data Ecosystem", "PROFESSIONAL PYTHON", ["NumPy", "Pandas", "Matplotlib"]),
    ("Level 23", "Professional Python", "PYTHON MASTERY", ["Testing and pytest concepts", "Debugging", "Logging", "Type hints", "Documentation", "PEP 8", "Code quality", "Project structure", "Environment variables", "Git and GitHub concepts"]),
    ("Level 24", "Modern Python Features", "PYTHON MASTERY", ["Pattern matching", "match case", "Walrus operator", "Positional only parameters", "Keyword only parameters", "Exception groups", "F-string improvements"]),
    ("Level 25", "Concurrency & AsyncIO", "PYTHON MASTERY", ["AsyncIO basics", "async and await", "Event loop", "Threading and GIL", "Multiprocessing", "ThreadPoolExecutor", "Task gathering"]),
    ("Level 26", "Advanced Metaprogramming & CPython", "PYTHON MASTERY", ["Metaclasses", "type inheritance", "Descriptors", "Memory management", "Reference counting", "Slots optimization", "Dynamic attributes"]),
    ("Level 27", "FastAPI & Modern Web APIs", "PYTHON MASTERY", ["FastAPI basics", "Pydantic validation", "Async endpoints", "Dependency injection", "WebSockets", "JWT Authentication"]),
    ("Level 28", "Web Scraping & Security", "PYTHON MASTERY", ["Beautiful Soup 4", "HTML parsing", "Selenium automation", "Playwright scraping", "Cryptography and hashlib", "Environment security"]),
    ("Level 29", "Packaging & Cloud Deployment", "PYTHON MASTERY", ["Building Python packages", "pyproject.toml", "Publishing to PyPI", "Docker for Python", "GitHub Actions CI CD", "Gunicorn and Uvicorn"]),
]

def slug_part(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")

def lesson_content(course_title, topics):
    topic_list = ", ".join(topics)
    return f"""# {course_title}: getting started

In this lesson, you will begin with **{topic_list}**. Read each idea slowly, try a small example, and explain it back in your own words.

Python learning is practical: make a prediction, run code, notice the result, and change one thing. You do not need to memorize everything today. The goal is to understand what each concept is for and build confidence through small experiments.

**Practice prompt:** Write down one question you have about {topics[0]}, then create the smallest Python example you can when code is introduced."""

def seed_curriculum():
    for number, title, track, topics in LEVELS:
        level_number = number.split()[-1]
        slug = f"level-{level_number}-{title.lower().replace(' ', '-').replace('&', 'and')}"
        
        course = Course.query.filter_by(slug=slug).first()
        if not course:
            course = Course(
                title=f"{number} - {title}",
                slug=slug,
                description=f"{track}: {title}. A guided sequence for learners starting exactly where they are.",
                level=number
            )
            db.session.add(course)
            db.session.flush()

        for index in range(0, len(topics), 4):
            group = topics[index:index + 4]
            module_number = index // 4 + 1
            mod_title = f"Module {module_number}: {group[0]}"
            
            module = Module.query.filter_by(course_id=course.id, title=mod_title).first()
            if not module:
                module = Module(
                    course=course,
                    title=mod_title,
                    description="Topics: " + ", ".join(group),
                    position=module_number
                )
                db.session.add(module)
                db.session.flush()

            les_slug = f"level-{level_number}-module-{module_number}-{slug_part(group[0])}"
            lesson = Lesson.query.filter_by(module_id=module.id, slug=les_slug).first()
            if not lesson:
                lesson = Lesson(
                    module=module,
                    title=f"Introduction to {group[0]}",
                    slug=les_slug,
                    content=lesson_content(title, group),
                    position=1,
                    estimated_minutes=12
                )
                db.session.add(lesson)

    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_curriculum()
        print(f"Seeded {Course.query.count()} courses, {Module.query.count()} modules, and {Lesson.query.count()} lessons.")
