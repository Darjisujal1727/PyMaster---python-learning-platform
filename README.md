# PyMaster

PyMaster is a free Python learning platform built with Flask. It is designed to guide learners from complete beginner to advanced Python without accounts, payments, or locked content.

## Foundation included

- Flask application factory and base configuration
- SQLite database configured through Flask-SQLAlchemy
- Course, Module, Lesson, CodeExample, PracticeProblem, QuizQuestion, and Project models
- A home route, health route, and Bootstrap-based base template
- Reserved folders for services, seed data, static assets, and learning-progress JavaScript

## Installation

1. Open a terminal in this `PyMaster` folder.
2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

## Run

```powershell
python app.py
```

Open `http://127.0.0.1:5000/` in a browser. On first run, the SQLite database is created at `database/pymaster.db`.

To check the app without opening the UI, visit `http://127.0.0.1:5000/health`.
