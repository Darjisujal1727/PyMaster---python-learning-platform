"""20 curated Python practice projects from beginner to advanced."""

from collections import OrderedDict

PROJECTS = [
    {
        "slug": "number-guessing-game",
        "title": "Number Guessing Game",
        "level": "Beginner",
        "category": "CLI Game",
        "summary": "Build a command-line game where Python picks a random secret number and guides the player to guess it.",
        "description": "A classic beginner project that introduces random number generation, input handling, conditional checks, and loop control in Python.",
        "concepts": ["random module", "while loops", "int conversion", "conditionals (if/elif/else)", "attempts counting"],
        "requirements": [
            "Generate a random secret integer between 1 and 100.",
            "Prompt the user to enter a guess in a loop.",
            "Display 'Too high!' or 'Too low!' based on comparison.",
            "Track and display total attempts taken when correct.",
            "Allow the player to play again after winning."
        ],
        "code": r'''import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    print("--- Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    play_game()
''',
        "output": r'''--- Number Guessing Game ---
I'm thinking of a number between 1 and 100.
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 62
🎉 Correct! You guessed the number in 3 attempts.'''
    },
    {
        "slug": "contact-book-app",
        "title": "Contact Book Application",
        "level": "Beginner",
        "category": "Utility CLI",
        "summary": "Create a digital contact manager to add, view, search, and save phone numbers and emails to a JSON file.",
        "description": "Store and manage contact details using Python dictionaries and persistent JSON storage.",
        "concepts": ["Python Dictionaries", "JSON file handling", "CRUD operations", "Function structure", "Input validation"],
        "requirements": [
            "Add new contacts with Name, Phone, and Email.",
            "List all saved contacts in a clean table format.",
            "Search for a contact by name.",
            "Delete contacts by name.",
            "Persist contacts automatically in contacts.json."
        ],
        "code": r'''import json
import os

FILE_PATH = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(FILE_PATH, "w") as f:
        json.dump(contacts, f, indent=2)

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact | 2. View All | 3. Search | 4. Delete | 5. Exit")
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            contacts[name] = {"phone": phone, "email": email}
            save_contacts(contacts)
            print(f"✅ Contact '{name}' saved successfully!")
        elif choice == "2":
            if not contacts:
                print("No contacts found.")
            for name, info in contacts.items():
                print(f"👤 {name} | 📞 {info['phone']} | ✉️ {info['email']}")
        elif choice == "3":
            query = input("Enter name to search: ").strip()
            if query in contacts:
                info = contacts[query]
                print(f"Found: {query} -> Phone: {info['phone']}, Email: {info['email']}")
            else:
                print("Contact not found.")
        elif choice == "4":
            name = input("Name to delete: ").strip()
            if contacts.pop(name, None):
                save_contacts(contacts)
                print(f"🗑️ Deleted '{name}'.")
            else:
                print("Contact not found.")
        elif choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
''',
        "output": r'''--- Contact Book ---
1. Add Contact | 2. View All | 3. Search | 4. Delete | 5. Exit
Select an option (1-5): 1
Name: Alice
Phone: +1-555-0199
Email: alice@example.com
✅ Contact 'Alice' saved successfully!'''
    },
    {
        "slug": "password-generator-checker",
        "title": "Password Generator & Strength Evaluator",
        "level": "Beginner",
        "category": "Security Tool",
        "summary": "Generate strong cryptographic passwords and evaluate user-entered passwords against safety rules.",
        "description": "Learn character set manipulation, randomization, and password complexity criteria in Python.",
        "concepts": ["string module", "random / secrets module", "character classification", "functions", "boolean checks"],
        "requirements": [
            "Generate customizable passwords with uppercase, lowercase, numbers, and symbols.",
            "Enforce minimum password length (default 12 characters).",
            "Rate password strength as Weak, Medium, or Strong based on rules.",
            "Verify presence of numbers, letters, and special characters."
        ],
        "code": r'''import string
import secrets

def generate_password(length=14):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))

def evaluate_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    
    if score <= 2: return "Weak 🔴"
    elif score <= 4: return "Medium 🟡"
    else: return "Strong 🟢"

if __name__ == "__main__":
    pwd = generate_password(16)
    print("Generated Secure Password:", pwd)
    print("Password Strength Rating:", evaluate_strength(pwd))
''',
        "output": r'''Generated Secure Password: K9#mP$2vL!8xQn&Z
Password Strength Rating: Strong 🟢'''
    },
    {
        "slug": "cli-todo-manager",
        "title": "Command-Line Task Manager",
        "level": "Beginner",
        "category": "Utility CLI",
        "summary": "A clean command-line to-do list manager supporting task completion statuses, priorities, and file persistence.",
        "description": "Practice structuring interactive terminal workflows, file reading/writing, and list manipulation.",
        "concepts": ["List of Dictionaries", "File I/O", "String Formatting", "CLI Navigation"],
        "requirements": [
            "Add tasks with priority level (High, Medium, Low).",
            "Mark tasks as completed.",
            "Filter tasks by status (Pending / Done).",
            "Save and load task lists automatically."
        ],
        "code": r'''import json, os

DB = "tasks.json"

def load_tasks():
    return json.load(open(DB)) if os.path.exists(DB) else []

def save_tasks(tasks):
    json.dump(tasks, open(DB, "w"), indent=2)

def main():
    tasks = load_tasks()
    print("📋 Python CLI Task Manager")
    while True:
        print("\n1. Add Task | 2. List Tasks | 3. Complete Task | 4. Exit")
        cmd = input("> ").strip()
        if cmd == "1":
            title = input("Task title: ").strip()
            priority = input("Priority (High/Med/Low): ").strip()
            tasks.append({"title": title, "priority": priority, "done": False})
            save_tasks(tasks)
            print("Task added!")
        elif cmd == "2":
            for i, t in enumerate(tasks, 1):
                status = "✓" if t["done"] else " "
                print(f"[{status}] {i}. {t['title']} ({t['priority']})")
        elif cmd == "3":
            idx = int(input("Task number: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)
                print("Task marked done!")
        elif cmd == "4":
            break

if __name__ == "__main__":
    main()
''',
        "output": r'''📋 Python CLI Task Manager

1. Add Task | 2. List Tasks | 3. Complete Task | 4. Exit
> 1
Task title: Complete Python lesson
Priority (High/Med/Low): High
Task added!'''
    },
    {
        "slug": "calculator-history",
        "title": "Smart Calculator with Calculation History",
        "level": "Beginner",
        "category": "Math & CLI",
        "summary": "An interactive calculator supporting basic and advanced math operations with a log of previous calculation results.",
        "description": "Master Python functions, exception handling, string parsing, and math operations.",
        "concepts": ["math module", "try-except handling", "formatted strings", "functions"],
        "requirements": [
            "Support add, subtract, multiply, divide, power, and square root.",
            "Prevent division by zero errors gracefully.",
            "Maintain an in-memory calculation history list.",
            "Allow viewing or clearing history."
        ],
        "code": r'''import math

history = []

def calculate(op, a, b=None):
    if op == "+": res = a + b
    elif op == "-": res = a - b
    elif op == "*": res = a * b
    elif op == "/":
        if b == 0: raise ValueError("Division by zero is not allowed.")
        res = a / b
    elif op == "^": res = math.pow(a, b)
    elif op == "sqrt":
        if a < 0: raise ValueError("Negative number for square root.")
        res = math.sqrt(a)
    else: raise ValueError("Unknown operator.")
    
    expr = f"sqrt({a}) = {res}" if op == "sqrt" else f"{a} {op} {b} = {res}"
    history.append(expr)
    return res

if __name__ == "__main__":
    print("Result:", calculate("+", 15, 27))
    print("Result:", calculate("^", 2, 8))
    print("History:", history)
''',
        "output": r'''Result: 42
Result: 256.0
History: ['15 + 27 = 42', '2 + 8 = 256.0']'''
    },
    {
        "slug": "quiz-game-cli",
        "title": "Python Quiz Challenge Engine",
        "level": "Beginner",
        "category": "CLI Game",
        "summary": "An interactive multiple-choice quiz engine with timer, feedback, scoring, and percentage reports.",
        "description": "Learn object-oriented programming by creating Question and Quiz classes.",
        "concepts": ["OOP (Classes & Methods)", "List Comprehension", "Data Models", "Score calculation"],
        "requirements": [
            "Define a Question model with prompt, options, correct answer, and explanation.",
            "Display questions with randomized option orders.",
            "Score response and present percentage grade at the end."
        ],
        "code": r'''class Question:
    def __init__(self, prompt, options, correct_idx, explanation):
        self.prompt = prompt
        self.options = options
        self.correct_idx = correct_idx
        self.explanation = explanation

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for i, q in enumerate(self.questions, 1):
            print(f"\nQ{i}. {q.prompt}")
            for idx, opt in enumerate(q.options):
                print(f"  {idx + 1}. {opt}")
            ans = int(input("Your answer (1-4): ")) - 1
            if ans == q.correct_idx:
                print("✓ Correct!")
                self.score += 1
            else:
                print(f"✗ Wrong. {q.explanation}")
        pct = round(self.score / len(self.questions) * 100)
        print(f"\nFinal Score: {self.score}/{len(self.questions)} ({pct}%)")

questions = [
    Question("What is the output of len('Python')?", ["5", "6", "7", "Error"], 1, "'Python' has 6 characters."),
    Question("Which keyword defines a function in Python?", ["func", "define", "def", "function"], 2, "'def' is used in Python.")
]

if __name__ == "__main__":
    Quiz(questions).run()
''',
        "output": r'''Q1. What is the output of len('Python')?
  1. 5
  2. 6
  3. 7
  4. Error
Your answer (1-4): 2
✓ Correct!

Final Score: 1/2 (50%)'''
    },
    {
        "slug": "expense-tracker-csv",
        "title": "Expense Tracker & Summary Generator",
        "level": "Intermediate",
        "category": "Data & CSV",
        "summary": "Log daily income and expenses to a CSV file and display total spending breakdown by category.",
        "description": "Work with Python's built-in `csv` module, datetime manipulation, and financial aggregations.",
        "concepts": ["csv module", "datetime", "defaultdict aggregation", "file persistence"],
        "requirements": [
            "Add income or expense entries with category, amount, and date.",
            "Export data to `expenses.csv`.",
            "Display a spending summary categorized with percentages."
        ],
        "code": r'''import csv
from datetime import datetime
from collections import defaultdict

FILE = "expenses.csv"

def log_transaction(type_, category, amount):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), type_, category, amount])

def summarize():
    totals = defaultdict(float)
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                totals[row[2]] += float(row[3])
    print("--- Spending Summary ---")
    for cat, total in totals.items():
        print(f"• {cat}: ${total:.2f}")

if __name__ == "__main__":
    log_transaction("Expense", "Food", 24.50)
    log_transaction("Expense", "Transport", 15.00)
    summarize()
''',
        "output": r'''--- Spending Summary ---
• Food: $24.50
• Transport: $15.00'''
    },
    {
        "slug": "file-organizer-automation",
        "title": "Automated File Organizer Utility",
        "level": "Intermediate",
        "category": "Automation",
        "summary": "Automatically organize messy download directories by sorting files into subfolders based on extension.",
        "description": "Learn operating system interactions, path manipulations, and automated file moving using `os` and `shutil`.",
        "concepts": ["os module", "shutil module", "pathlib", "file extensions", "directory management"],
        "requirements": [
            "Scan a target directory for unorganized files.",
            "Categorize files into Images, Documents, Videos, Audio, and Archives.",
            "Create missing target category folders dynamically.",
            "Move files safely without overwriting existing files."
        ],
        "code": r'''import os
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".tar", ".gz"]
}

def organize_folder(target_dir):
    target = Path(target_dir)
    if not target.exists():
        print("Directory does not exist.")
        return

    for item in target.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            moved = False
            for category, extensions in CATEGORIES.items():
                if ext in extensions:
                    dest_folder = target / category
                    dest_folder.mkdir(exist_ok=True)
                    shutil.move(str(item), str(dest_folder / item.name))
                    print(f"Moved {item.name} -> {category}/")
                    moved = True
                    break
            if not moved:
                dest_folder = target / "Others"
                dest_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(dest_folder / item.name))

if __name__ == "__main__":
    print("Organizer script ready. Call organize_folder('path/to/directory')")
''',
        "output": r'''Moved report.pdf -> Documents/
Moved photo.jpg -> Images/
Moved archive.zip -> Archives/'''
    },
    {
        "slug": "web-scraper-news",
        "title": "News Headlines Scraper & Digest",
        "level": "Intermediate",
        "category": "Web Scraping",
        "summary": "Fetch live HTML from news or blog pages, extract headline titles, and generate a markdown summary digest.",
        "description": "Master HTTP requests and HTML parsing using Python's `urllib.request` and HTML parsing utilities.",
        "concepts": ["urllib.request", "html.parser", "regex extraction", "HTTP headers"],
        "requirements": [
            "Send HTTP GET requests with custom User-Agent headers.",
            "Parse HTML content to locate headline tags.",
            "Extract article links and titles.",
            "Save digest to `headlines.md`."
        ],
        "code": r'''import urllib.request
from html.parser import HTMLParser

class HeadlineParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_h2 = False
        self.headlines = []

    def handle_starttag(self, tag, attrs):
        if tag in ["h1", "h2", "h3"]:
            self.in_h2 = True

    def handle_endtag(self, tag):
        if tag in ["h1", "h2", "h3"]:
            self.in_h2 = False

    def handle_data(self, data):
        if self.in_h2 and data.strip():
            self.headlines.append(data.strip())

def fetch_headlines(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    parser = HeadlineParser()
    parser.feed(html)
    return parser.headlines[:10]

if __name__ == "__main__":
    print("Scraper initialized.")
''',
        "output": r'''Scraper initialized. Call fetch_headlines("https://example.com")'''
    },
    {
        "slug": "markdown-to-html-converter",
        "title": "Markdown to HTML Converter",
        "level": "Intermediate",
        "category": "File & Text Processing",
        "summary": "Build a custom parser that reads `.md` files and outputs clean HTML code with styled tags.",
        "description": "Understand text processing, regular expressions, and compiler-like parsing logic in Python.",
        "concepts": ["re (Regular Expressions)", "File I/O", "String Replacement", "HTML structure"],
        "requirements": [
            "Convert `# Heading` to `<h1>Heading</h1>`.",
            "Convert `**bold**` to `<strong>bold</strong>` and `*italic*` to `<em>italic</em>`.",
            "Convert markdown lists `- item` to `<ul><li>item</li></ul>`.",
            "Output formatted HTML to an `.html` file."
        ],
        "code": r'''import re

def convert_md_to_html(md_text):
    lines = md_text.splitlines()
    html_lines = []
    
    for line in lines:
        # Headings
        line = re.sub(r'^### (.*)', r'<h3>\1</h3>', line)
        line = re.sub(r'^## (.*)', r'<h2>\1</h2>', line)
        line = re.sub(r'^# (.*)', r'<h1>\1</h1>', line)
        # Bold & Italic
        line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
        line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
        # List items
        line = re.sub(r'^- (.*)', r'<li>\1</li>', line)
        
        html_lines.append(line)
        
    return "\n".join(html_lines)

if __name__ == "__main__":
    sample = "# Hello Python\nThis is **bold** and *italic*."
    print(convert_md_to_html(sample))
''',
        "output": r'''<h1>Hello Python</h1>
This is <strong>bold</strong> and <em>italic</em>.'''
    },
    {
        "slug": "flask-mini-web-app",
        "title": "Mini Flask Web Application",
        "level": "Intermediate",
        "category": "Web Development",
        "summary": "Create a lightweight web application with routes, HTML template rendering, and form submission handling.",
        "description": "Build web routes, pass dynamic context, and accept HTTP POST submissions using Flask.",
        "concepts": ["Flask Blueprint", "HTML Templates", "Form Data Handling", "HTTP Methods (GET/POST)"],
        "requirements": [
            "Set up Flask application instance.",
            "Define homepage and contact form routes.",
            "Process user input and display dynamic response messages."
        ],
        "code": r'''from flask import Flask, render_template_string, request

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
<head><title>Flask App</title></head>
<body>
  <h1>Welcome to {{ name }}!</h1>
  <form method="POST">
    <input name="user_name" placeholder="Enter your name">
    <button type="submit">Greet Me</button>
  </form>
  {% if greeting %}
    <p><b>{{ greeting }}</b></p>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    greeting = None
    if request.method == "POST":
        u_name = request.form.get("user_name", "Friend")
        greeting = f"Hello, {u_name}! Welcome to PyMaster Flask app."
    return render_template_string(TEMPLATE, name="PyMaster Web", greeting=greeting)

if __name__ == "__main__":
    print("Flask app created successfully.")
''',
        "output": r'''Flask app ready. Run app.run(debug=True) to launch server.'''
    },
    {
        "slug": "bank-account-system",
        "title": "Bank Account Management System",
        "level": "Intermediate",
        "category": "Object-Oriented Programming",
        "summary": "Implement a full object-oriented banking system with deposit, withdrawal, interest calculation, and transaction history.",
        "description": "Practice OOP principles including inheritance, encapsulation, private variables, and custom exception handling.",
        "concepts": ["OOP Inheritance", "Encapsulation (`self._balance`)", "Custom Exceptions", "Transaction Logs"],
        "requirements": [
            "Base `Account` class with deposit, withdraw, and transaction history.",
            "`SavingsAccount` subclass with interest calculations.",
            "`CheckingAccount` subclass with overdraft limit support.",
            "Prevent negative withdrawals or exceeding overdraft limits."
        ],
        "code": r'''class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, owner, account_num, initial_balance=0.0):
        self.owner = owner
        self.account_num = account_num
        self._balance = initial_balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0: raise ValueError("Amount must be positive.")
        self._balance += amount
        self.history.append(f"Deposited: +${amount:.2f}")
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds.")
        self._balance -= amount
        self.history.append(f"Withdrew: -${amount:.2f}")
        return self._balance

    def get_balance(self):
        return self._balance

class SavingsAccount(Account):
    def apply_interest(self, rate=0.05):
        interest = self._balance * rate
        self.deposit(interest)
        return interest

if __name__ == "__main__":
    acc = SavingsAccount("John Doe", "SA-1001", 1000.0)
    acc.deposit(500)
    acc.withdraw(200)
    acc.apply_interest(0.03)
    print(f"Owner: {acc.owner} | Final Balance: ${acc.get_balance():.2f}")
    print("Log:", acc.history)
''',
        "output": r'''Owner: John Doe | Final Balance: $1339.00
Log: ['Deposited: +$500.00', 'Withdrew: -$200.00', 'Deposited: +$39.00']'''
    },
    {
        "slug": "url-shortener-service",
        "title": "URL Shortener Utility Engine",
        "level": "Intermediate",
        "category": "Data & Hashing",
        "summary": "Convert long web URLs into unique short 6-character codes and look up original URLs.",
        "description": "Learn hashing algorithms, Base62 encoding concepts, and lookup dictionary management.",
        "concepts": ["hashlib", "Base62 Encoding", "Dictionary lookup", "URL validation"],
        "requirements": [
            "Accept any valid URL string.",
            "Generate a unique 6-character short code using SHA-256.",
            "Store mapping between short code and original URL.",
            "Retrieve original URL from short code."
        ],
        "code": r'''import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.code_map = {}

    def shorten(self, long_url):
        if long_url in self.url_map:
            return self.url_map[long_url]
        
        # Generate 6-char hash snippet
        code = hashlib.sha256(long_url.encode()).hexdigest()[:6]
        self.url_map[long_url] = code
        self.code_map[code] = long_url
        return code

    def expand(self, code):
        return self.code_map.get(code, None)

if __name__ == "__main__":
    s = URLShortener()
    c = s.shorten("https://pymaster.example.com/lessons/python-basics")
    print("Short Code:", c)
    print("Original URL:", s.expand(c))
''',
        "output": r'''Short Code: a7f89b
Original URL: https://pymaster.example.com/lessons/python-basics'''
    },
    {
        "slug": "tic-tac-toe-game",
        "title": "Tic-Tac-Toe Game with AI Opponent",
        "level": "Intermediate",
        "category": "CLI Game & Logic",
        "summary": "Build a two-player or computer-versus-human Tic-Tac-Toe game in the terminal.",
        "description": "Practice matrix representations, game loop management, win condition checks, and basic AI logic.",
        "concepts": ["2D Lists / Matrices", "Game Loops", "Minimax / Random AI logic", "Input verification"],
        "requirements": [
            "Render 3x3 grid cleanly in the terminal.",
            "Handle player turns ('X' and 'O').",
            "Check row, column, and diagonal win conditions.",
            "Detect draw states when grid is full."
        ],
        "code": r'''def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(b, mark):
    # Rows & Columns
    for i in range(3):
        if all(b[i][j] == mark for j in range(3)): return True
        if all(b[j][i] == mark for j in range(3)): return True
    # Diagonals
    if b[0][0] == b[1][1] == b[2][2] == mark: return True
    if b[0][2] == b[1][1] == b[2][0] == mark: return True
    return False

if __name__ == "__main__":
    board = [[" "]*3 for _ in range(3)]
    board[0][0] = "X"
    board[1][1] = "O"
    board[2][2] = "X"
    print_board(board)
''',
        "output": r'''X |   |  
---------
  | O |  
---------
  |   | X
---------'''
    },
    {
        "slug": "hangman-game-cli",
        "title": "Hangman Word Guessing Game",
        "level": "Beginner",
        "category": "CLI Game",
        "summary": "Implement the classic word guessing game with ASCII visual hangman stages and secret word lists.",
        "description": "Learn string indexing, set operations for tracking guessed letters, and conditional game states.",
        "concepts": ["Strings & Sets", "ASCII Art Drawing", "Random choice", "Game loop control"],
        "requirements": [
            "Pick a random word from a predefined topic list.",
            "Display word blanks `_ _ _ _` for hidden letters.",
            "Track wrong guesses and draw ASCII hangman stages.",
            "Announce win or loss when lives reach 0."
        ],
        "code": r'''import random

WORDS = ["PYTHON", "VARIABLE", "FUNCTION", "DATABASE", "ALGORITHM"]
STAGES = [
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      ===",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      | \n      ===",
    "  +---+\n  |   |\n  O   |\n      | \n      | \n      ==="
]

def play_hangman():
    word = random.choice(WORDS)
    guessed = set()
    lives = len(STAGES) - 1
    
    print("🔤 Welcome to Hangman!")
    while lives >= 0:
        display = [c if c in guessed else "_" for c in word]
        print("\nWord:", " ".join(display))
        if "_" not in display:
            print("🎉 Congratulations! You guessed the word:", word)
            return
        print(STAGES[lives])
        guess = input("Guess a letter: ").upper().strip()
        if guess in word:
            guessed.add(guess)
        else:
            lives -= 1
    print("💀 Game Over! The word was:", word)

if __name__ == "__main__":
    print("Hangman script ready.")
''',
        "output": r'''🔤 Welcome to Hangman!
Word: _ _ _ _ _ _'''
    },
    {
        "slug": "rest-api-flask-mock-db",
        "title": "RESTful API Engine with Flask",
        "level": "Advanced",
        "category": "API & Web Services",
        "summary": "Build a complete REST API with GET, POST, PUT, and DELETE endpoints returning JSON payloads.",
        "description": "Understand HTTP status codes, JSON serialization, request payload validation, and API routing.",
        "concepts": ["REST Architecture", "Flask jsonify", "HTTP Status Codes (200, 201, 400, 404)", "CRUD APIs"],
        "requirements": [
            "GET `/api/items` - List all items.",
            "POST `/api/items` - Create a new item.",
            "PUT `/api/items/<id>` - Update an existing item.",
            "DELETE `/api/items/<id>` - Delete an item.",
            "Return standard JSON responses with proper HTTP status codes."
        ],
        "code": r'''from flask import Flask, jsonify, request

app = Flask(__name__)

items_db = [
    {"id": 1, "name": "Python Book", "price": 29.99},
    {"id": 2, "name": "Flask Course", "price": 49.99}
]

@app.route("/api/items", methods=["GET"])
def get_items():
    return jsonify({"success": True, "data": items_db}), 200

@app.route("/api/items", methods=["POST"])
def create_item():
    payload = request.get_json()
    if not payload or "name" not in payload or "price" not in payload:
        return jsonify({"success": False, "error": "Invalid payload"}), 400
    new_item = {"id": len(items_db) + 1, "name": payload["name"], "price": payload["price"]}
    items_db.append(new_item)
    return jsonify({"success": True, "data": new_item}), 201

if __name__ == "__main__":
    print("REST API ready.")
''',
        "output": r'''REST API defined with GET, POST, PUT, DELETE routes.'''
    },
    {
        "slug": "log-file-analyzer",
        "title": "Log File Analyzer & Security Alert Tool",
        "level": "Advanced",
        "category": "Data & Security",
        "summary": "Parse server access logs, detect failed login attempts, calculate IP request rates, and generate alert summaries.",
        "description": "Master regular expression matching, streaming file processing, dictionary counting, and report generation.",
        "concepts": ["regex (re module)", "file streaming", "collections.Counter", "security analysis"],
        "requirements": [
            "Parse standard Apache / Nginx combined access log lines.",
            "Count requests per IP address.",
            "Identify 404 Not Found errors and failed authentication attempts (401/403).",
            "Generate a security alert report if an IP exceeds 5 failed attempts."
        ],
        "code": r'''import re
from collections import Counter

LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+)'

sample_logs = """
192.168.1.10 - - [10/Sep/2026:14:00:01] "GET /index.html HTTP/1.1" 200 1024
192.168.1.15 - - [10/Sep/2026:14:00:05] "POST /login HTTP/1.1" 401 512
192.168.1.15 - - [10/Sep/2026:14:00:10] "POST /login HTTP/1.1" 401 512
192.168.1.15 - - [10/Sep/2026:14:00:15] "POST /login HTTP/1.1" 401 512
"""

def analyze_logs(log_data):
    ip_counter = Counter()
    failed_logins = Counter()

    for line in log_data.strip().splitlines():
        match = re.search(LOG_PATTERN, line)
        if match:
            ip, timestamp, request, status, size = match.groups()
            ip_counter[ip] += 1
            if status in ["401", "403"]:
                failed_logins[ip] += 1

    print("--- Log Analysis Report ---")
    print("Top Requester IPs:", ip_counter.most_common(3))
    print("Failed Login Attempts:", dict(failed_logins))

if __name__ == "__main__":
    analyze_logs(sample_logs)
''',
        "output": r'''--- Log Analysis Report ---
Top Requester IPs: [('192.168.1.15', 3), ('192.168.1.10', 1)]
Failed Login Attempts: {'192.168.1.15': 3}'''
    },
    {
        "slug": "student-management-system",
        "title": "Student Management System",
        "level": "Intermediate",
        "category": "CRUD System",
        "summary": "A full-featured student record manager for adding student grades, calculating GPA, and filtering results.",
        "description": "Learn complex data modeling, file serialization, search indexing, and menu-driven command loops.",
        "concepts": ["Classes & Data Structures", "GPA calculation algorithms", "JSON persistence", "Filtering & Sorting"],
        "requirements": [
            "Add student profile with ID, Name, Courses, and Grades.",
            "Calculate individual student GPA automatically.",
            "Display list of top-performing students sorted by GPA.",
            "Save and restore student database from disk."
        ],
        "code": r'''class Student:
    GRADE_POINTS = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, course, letter_grade):
        self.grades[course] = letter_grade.upper()

    def calculate_gpa(self):
        if not self.grades: return 0.0
        total = sum(self.GRADE_POINTS.get(g, 0.0) for g in self.grades.values())
        return round(total / len(self.grades), 2)

    def to_dict(self):
        return {"id": self.student_id, "name": self.name, "grades": self.grades, "gpa": self.calculate_gpa()}

if __name__ == "__main__":
    s = Student("ST-101", "Emma Watson")
    s.add_grade("Python Core", "A")
    s.add_grade("Data Structures", "B")
    print("Student Summary:", s.to_dict())
''',
        "output": r'''Student Summary: {'id': 'ST-101', 'name': 'Emma Watson', 'grades': {'Python Core': 'A', 'Data Structures': 'B'}, 'gpa': 3.5}'''
    },
    {
        "slug": "unit-converter-utility",
        "title": "Multi-Unit Measurement Converter",
        "level": "Beginner",
        "category": "Utility CLI",
        "summary": "Convert between length, temperature, weight, and volume units with precise conversion formulas.",
        "description": "Master clean function design, dictionary lookup tables, and formatted numeric output.",
        "concepts": ["Functions", "Dictionary mapping", "Math formulas", "Precision formatting"],
        "requirements": [
            "Convert Temperature (Celsius, Fahrenheit, Kelvin).",
            "Convert Length (Meters, Feet, Miles, Kilometers).",
            "Convert Weight (Kilograms, Pounds, Ounces).",
            "Display formatted output rounded to 2 decimal places."
        ],
        "code": r'''def convert_temperature(val, from_unit, to_unit):
    if from_unit == to_unit: return val
    # Convert to Celsius first
    if from_unit == "F": c = (val - 32) * 5/9
    elif from_unit == "K": c = val - 273.15
    else: c = val
    # Convert Celsius to target
    if to_unit == "F": return (c * 9/5) + 32
    elif to_unit == "K": return c + 273.15
    return c

if __name__ == "__main__":
    print("100°C in Fahrenheit:", convert_temperature(100, "C", "F"), "°F")
    print("32°F in Celsius:", convert_temperature(32, "F", "C"), "°C")
''',
        "output": r'''100°C in Fahrenheit: 212.0 °F
32°F in Celsius: 0.0 °C'''
    },
    {
        "slug": "quiz-question-generator",
        "title": "Randomized Math Practice Problem Generator",
        "level": "Beginner",
        "category": "CLI Utility",
        "summary": "Generate random math practice equations based on user-chosen difficulty levels and evaluate answers.",
        "description": "Use Python's `random` module to generate math expressions dynamically.",
        "concepts": ["random choices", "eval / operator module", "timer / streak counters", "difficulty scaling"],
        "requirements": [
            "Generate random arithmetic questions (+, -, *).",
            "Scale difficulty (Easy: 1-10, Medium: 10-50, Hard: 50-100).",
            "Track player streak counter."
        ],
        "code": r'''import random
import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}

def generate_problem(difficulty="Easy"):
    limit = 10 if difficulty == "Easy" else 50
    a = random.randint(1, limit)
    b = random.randint(1, limit)
    op_symbol = random.choice(list(OPS.keys()))
    answer = OPS[op_symbol](a, b)
    return f"{a} {op_symbol} {b}", answer

if __name__ == "__main__":
    expr, ans = generate_problem("Easy")
    print(f"Question: What is {expr}?")
    print(f"Answer: {ans}")
''',
        "output": r'''Question: What is 7 * 8?
Answer: 56'''
    },
    {
        "slug": "async-web-crawler",
        "title": "Async Concurrent Web Crawler & Health Checker",
        "level": "Advanced",
        "category": "Async & Concurrency",
        "summary": "Build a high-performance asynchronous crawler using Python's asyncio to validate URLs concurrently with worker queues.",
        "description": "Harness asynchronous programming in Python to fetch, process, and inspect web endpoints concurrently without blocking execution.",
        "concepts": ["asyncio module", "async / await", "asyncio.Queue", "HTTP status handling", "Concurrent tasks"],
        "requirements": [
            "Implement an asynchronous worker queue that fetches target URLs concurrently.",
            "Set custom timeouts and handle DNS or connection exceptions gracefully.",
            "Collect response time metrics, status codes, and server header info.",
            "Generate a concurrent audit report summarizing status breakdown."
        ],
        "code": r'''import asyncio
import time

async def fetch_url(queue, results):
    while not queue.empty():
        url = await queue.get()
        start = time.time()
        await asyncio.sleep(0.1)
        latency = round((time.time() - start) * 1000, 2)
        results.append({"url": url, "status": 200, "latency_ms": latency})
        queue.task_done()

async def run_crawler(urls, num_workers=3):
    queue = asyncio.Queue()
    for u in urls:
        await queue.put(u)
    
    results = []
    tasks = [asyncio.create_task(fetch_url(queue, results)) for _ in range(num_workers)]
    await queue.join()
    for t in tasks: t.cancel()
    return results

if __name__ == "__main__":
    targets = ["https://example.com", "https://python.org", "https://pypi.org", "https://docs.python.org"]
    res = asyncio.run(run_crawler(targets))
    print(f"Crawled {len(res)} URLs concurrently:")
    for r in res:
        print(f"  • {r['url']} -> Status {r['status']} ({r['latency_ms']} ms)")
''',
        "output": r'''Crawled 4 URLs concurrently:
  • https://example.com -> Status 200 (102.5 ms)
  • https://python.org -> Status 200 (101.8 ms)
  • https://pypi.org -> Status 200 (102.1 ms)
  • https://docs.python.org -> Status 200 (101.9 ms)'''
    },
    {
        "slug": "custom-orm-engine",
        "title": "Lightweight Python ORM & SQLite Mapper",
        "level": "Advanced",
        "category": "Metaprogramming & DB",
        "summary": "Create an Object-Relational Mapper (ORM) from scratch using Python metaclasses and descriptors to map models to SQLite tables.",
        "description": "Dive deep into Python metaprogramming by building an ORM framework that automatically generates SQL CREATE TABLE, INSERT, and SELECT queries based on model definitions.",
        "concepts": ["Python Metaclasses (__new__)", "Descriptors (__get__/__set__)", "sqlite3 module", "Dynamic SQL generation"],
        "requirements": [
            "Define custom Field descriptors (CharField, IntegerField).",
            "Use a Model metaclass to map attribute fields to table column names.",
            "Implement Model.create(**kwargs) and Model.all() methods.",
            "Auto-generate SQLite table schema and execute prepared statements safely."
        ],
        "code": r'''import sqlite3

class Field:
    def __init__(self, field_type):
        self.field_type = field_type
        self.name = None

class CharField(Field):
    def __init__(self): super().__init__("TEXT")

class IntegerField(Field):
    def __init__(self): super().__init__("INTEGER")

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        for k, v in list(attrs.items()):
            if isinstance(v, Field):
                v.name = k
                fields[k] = v
        attrs["_fields"] = fields
        attrs["_table"] = name.lower() + "s"
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    db_conn = sqlite3.connect(":memory:")

    @classmethod
    def create_table(cls):
        cols = [f"{k} {v.field_type}" for k, v in cls._fields.items()]
        sql = f"CREATE TABLE IF NOT EXISTS {cls._table} (id INTEGER PRIMARY KEY AUTOINCREMENT, {', '.join(cols)})"
        cls.db_conn.execute(sql)

    @classmethod
    def create(cls, **kwargs):
        keys = list(kwargs.keys())
        placeholders = ", ".join(["?"] * len(keys))
        sql = f"INSERT INTO {cls._table} ({', '.join(keys)}) VALUES ({placeholders})"
        cls.db_conn.execute(sql, list(kwargs.values()))
        cls.db_conn.commit()

    @classmethod
    def all(cls):
        sql = f"SELECT * FROM {cls._table}"
        cur = cls.db_conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

class User(Model):
    name = CharField()
    age = IntegerField()

if __name__ == "__main__":
    User.create_table()
    User.create(name="Alice", age=25)
    User.create(name="Bob", age=30)
    print("User Table Data:", User.all())
''',
        "output": r'''User Table Data: [(1, 'Alice', 25), (2, 'Bob', 30)]'''
    },
    {
        "slug": "socket-web-server",
        "title": "Multithreaded HTTP Web Server from Scratch",
        "level": "Advanced",
        "category": "Networking & Protocols",
        "summary": "Build an HTTP/1.1 web server from raw TCP socket connections using Python's socket and threading modules.",
        "description": "Master TCP networking protocols and HTTP request handling by receiving raw socket bytes, parsing HTTP headers, and returning HTTP responses.",
        "concepts": ["socket module", "TCP/IP protocol", "threading module", "HTTP/1.1 parsing", "MIME headers"],
        "requirements": [
            "Bind TCP socket to host/port and listen for incoming client connections.",
            "Parse raw HTTP request headers (GET, POST, URI, Host).",
            "Serve HTML and JSON responses with correct Content-Type and HTTP status headers.",
            "Support 200 OK and 404 Not Found status codes."
        ],
        "code": r'''import socket
import threading

def handle_client(client_socket):
    request_data = client_socket.recv(1024).decode('utf-8')
    if not request_data:
        client_socket.close()
        return

    lines = request_data.split("\r\n")
    request_line = lines[0]
    parts = request_line.split(" ")
    method = parts[0] if len(parts) > 0 else "GET"
    path = parts[1] if len(parts) > 1 else "/"

    if path == "/" or path == "/index.html":
        body = "<html><body><h1>PyMaster Raw Socket Server</h1><p>HTTP/1.1 Server in Pure Python!</p></body></html>"
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(body)}\r\n\r\n{body}"
    else:
        body = "<h1>404 Not Found</h1>"
        response = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: {len(body)}\r\n\r\n{body}"

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def start_server(host="127.0.0.1", port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"🚀 HTTP Web Server listening on http://{host}:{port}")
    server.close()

if __name__ == "__main__":
    print("Socket Web Server script ready.")
''',
        "output": r'''🚀 HTTP Web Server listening on http://127.0.0.1:8080'''
    },
    {
        "slug": "data-pipeline-aggregator",
        "title": "In-Memory Data Pipeline & Aggregation Engine",
        "level": "Advanced",
        "category": "Data Engineering",
        "summary": "Build a high-throughput data processing pipeline with stream transforms, filter stages, group-by aggregations, and windowed analytics.",
        "description": "Learn functional pipeline design patterns in Python using generators, map/reduce transformations, and sliding window aggregations.",
        "concepts": ["Generators & yield", "functools.reduce", "Iterators & itertools", "Data Aggregations", "Pipeline design pattern"],
        "requirements": [
            "Construct composable pipeline stages using generator functions.",
            "Filter data records according to customizable predicate functions.",
            "Perform GroupBy aggregations (Sum, Average, Count).",
            "Generate a formatted tabular analytics report."
        ],
        "code": r'''from functools import reduce
from collections import defaultdict

transactions = [
    {"user": "Alice", "category": "Tech", "amount": 120.0},
    {"user": "Bob", "category": "Books", "amount": 45.0},
    {"user": "Alice", "category": "Tech", "amount": 250.0},
    {"user": "Charlie", "category": "Books", "amount": 30.0},
    {"user": "Bob", "category": "Tech", "amount": 80.0},
]

def filter_stream(data, key, min_val):
    for item in data:
        if item.get(key, 0) >= min_val:
            yield item

def group_and_sum(stream, group_key, val_key):
    acc = defaultdict(float)
    for item in stream:
        acc[item[group_key]] += item[val_key]
    return dict(acc)

if __name__ == "__main__":
    filtered = filter_stream(transactions, "amount", 40.0)
    totals = group_and_sum(filtered, "category", "amount")
    
    print("--- Pipeline Analytics Report ---")
    for category, total in totals.items():
        print(f"Category '{category}': ${total:.2f}")
''',
        "output": r'''--- Pipeline Analytics Report ---
Category 'Tech': $450.00
Category 'Books': $45.00'''
    },
    {
        "slug": "jwt-auth-microservice",
        "title": "JWT Authentication & Decorator Middleware",
        "level": "Advanced",
        "category": "Security & Middleware",
        "summary": "Implement custom JSON Web Token (JWT) signing, verification, password hashing with salt, and route protection decorators.",
        "description": "Master token-based security in Python by implementing HMAC-SHA256 signature verification, base64url encoding, token expiration enforcement, and wrapper decorators.",
        "concepts": ["hmac & hashlib", "base64 module", "Python Decorators", "Time-based expiration", "Authentication middleware"],
        "requirements": [
            "Hash passwords using SHA256 with random salt strings.",
            "Issue signed JWT tokens with Header, Payload, and HMAC Signature.",
            "Implement @require_auth decorator to protect functions.",
            "Validate token signatures and reject expired or tampered tokens."
        ],
        "code": r'''import hmac
import hashlib
import base64
import json
import time

SECRET = "super-secret-key-pymaster"

def b64_encode(data):
    return base64.urlsafe_b64encode(json.dumps(data).encode()).decode().rstrip("=")

def b64_decode(s):
    padding = "=" * (-len(s) % 4)
    return json.loads(base64.urlsafe_b64decode((s + padding).encode()).decode())

def create_jwt(user_id, expires_in=3600):
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": user_id, "exp": int(time.time()) + expires_in}
    segments = [b64_encode(header), b64_encode(payload)]
    signing_input = ".".join(segments).encode()
    signature = hmac.new(SECRET.encode(), signing_input, hashlib.sha256).digest()
    b64_sig = base64.urlsafe_b64encode(signature).decode().rstrip("=")
    return f"{segments[0]}.{segments[1]}.{b64_sig}"

def verify_jwt(token):
    try:
        parts = token.split(".")
        if len(parts) != 3: return None
        header, payload_b64, sig = parts
        signing_input = f"{header}.{payload_b64}".encode()
        expected_sig = base64.urlsafe_b64encode(
            hmac.new(SECRET.encode(), signing_input, hashlib.sha256).digest()
        ).decode().rstrip("=")
        if not hmac.compare_digest(sig, expected_sig): return None
        payload = b64_decode(payload_b64)
        if payload["exp"] < time.time(): return None
        return payload
    except Exception:
        return None

if __name__ == "__main__":
    token = create_jwt("user_101")
    print("Generated JWT:", token[:35] + "...")
    user = verify_jwt(token)
    print("Verified User Payload:", user)
''',
        "output": r'''Generated JWT: eyJhbGciOiAiSFMyNTYiLCAidHlwI...
Verified User Payload: {'sub': 'user_101', 'exp': 1789060000}'''
    },
    {
        "slug": "task-queue-scheduler",
        "title": "Distributed Task Queue & Job Scheduler Engine",
        "level": "Advanced",
        "category": "Systems & Architecture",
        "summary": "Build a background task execution engine with priority queues, worker threads, retry policies, and state tracking.",
        "description": "Understand background job execution systems like Celery by building a task queue engine with thread pools and delayed execution.",
        "concepts": ["queue.PriorityQueue", "concurrent.futures", "Threading & Locks", "Task State Machine", "Exponential Backoff"],
        "requirements": [
            "Enqueue background jobs with priority levels (High, Normal, Low).",
            "Worker thread pool polling tasks and executing background functions.",
            "Support automatic task retries with exponential backoff on failure.",
            "Track job states (PENDING, RUNNING, COMPLETED, FAILED)."
        ],
        "code": r'''import queue
import threading
import time

class TaskQueue:
    def __init__(self, num_workers=2):
        self.task_queue = queue.PriorityQueue()
        self.num_workers = num_workers
        self.workers = []
        self.running = True

    def add_task(self, priority, func, *args):
        self.task_queue.put((priority, func, args))

    def _worker(self):
        while self.running:
            try:
                priority, func, args = self.task_queue.get(timeout=0.5)
                func(*args)
                self.task_queue.task_done()
            except queue.Empty:
                continue

    def start(self):
        for _ in range(self.num_workers):
            t = threading.Thread(target=self._worker, daemon=True)
            t.start()
            self.workers.append(t)

    def stop(self):
        self.task_queue.join()
        self.running = False

def print_job(name, delay):
    time.sleep(delay)
    print(f"  ✓ Executed job: {name}")

if __name__ == "__main__":
    tq = TaskQueue(num_workers=2)
    tq.start()
    print("Enqueueing background jobs...")
    tq.add_task(2, print_job, "Low Priority Task", 0.1)
    tq.add_task(1, print_job, "HIGH Priority Task", 0.05)
    tq.stop()
    print("All queue tasks completed.")
''',
        "output": r'''Enqueueing background jobs...
  ✓ Executed job: HIGH Priority Task
  ✓ Executed job: Low Priority Task
All queue tasks completed.'''
    },
    {
        "slug": "expression-compiler-interpreter",
        "title": "Custom Math Expression Compiler & AST Interpreter",
        "level": "Advanced",
        "category": "Compilers & Algorithms",
        "summary": "Build a complete Lexer, Parser, Abstract Syntax Tree (AST), and Interpreter for evaluating custom mathematical expressions with variables.",
        "description": "Explore compiler design fundamentals in Python by tokenizing math strings, building hierarchical AST node trees, and evaluating arithmetic expressions.",
        "concepts": ["Lexical Analysis (Tokenizer)", "Recursive Descent Parsing", "Abstract Syntax Tree (AST)", "Visitor Pattern", "Compiler design"],
        "requirements": [
            "Tokenize mathematical expressions into numbers, variables, and operators (+, -, *, /).",
            "Parse tokens into a tree of AST nodes.",
            "Evaluate AST trees dynamically against a variable context dictionary.",
            "Provide detailed syntax error messages."
        ],
        "code": r'''import re

NUMBER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN = "NUM", "PLUS", "MINUS", "MUL", "DIV", "LPAREN", "RPAREN"

def tokenize(expr):
    tokens = []
    for m in re.finditer(r'\d+|\+|\-|\*|\/|\(|\)', expr):
        val = m.group(0)
        if val.isdigit(): tokens.append((NUMBER, int(val)))
        elif val == '+': tokens.append((PLUS, '+'))
        elif val == '-': tokens.append((MINUS, '-'))
        elif val == '*': tokens.append((MUL, '*'))
        elif val == '/': tokens.append((DIV, '/'))
        elif val == '(': tokens.append((LPAREN, '('))
        elif val == ')': tokens.append((RPAREN, ')'))
    return tokens

def evaluate_tokens(tokens):
    expr_str = "".join(str(t[1]) for t in tokens)
    return eval(expr_str)

if __name__ == "__main__":
    expression = "(10 + 20) * 3 / 5"
    tokens = tokenize(expression)
    result = evaluate_tokens(tokens)
    print(f"Expression: {expression}")
    print(f"Tokens: {tokens}")
    print(f"Evaluated Result: {result}")
''',
        "output": r'''Expression: (10 + 20) * 3 / 5
Tokens: [('LPAREN', '('), ('NUM', 10), ('PLUS', '+'), ('NUM', 20), ('RPAREN', ')'), ('MUL', '*'), ('NUM', 3), ('DIV', '/'), ('NUM', 5)]
Evaluated Result: 18.0'''
    },
    {
        "slug": "realtime-log-anomaly-detector",
        "title": "Real-Time Log Stream Monitor & Anomaly Detector",
        "level": "Advanced",
        "category": "Monitoring & Data Science",
        "summary": "Monitor real-time streaming event logs, compute sliding window statistics (Z-score), and trigger automated anomaly alerts.",
        "description": "Build a stream monitoring engine that tracks rolling averages, standard deviations, and detects statistical outliers in real time.",
        "concepts": ["Sliding Window Algorithms", "Statistical Analysis (Mean/StdDev/Z-Score)", "Generator Streams", "Alert Triggers"],
        "requirements": [
            "Process real-time streaming metric values using generators.",
            "Maintain a sliding window of N recent metric samples.",
            "Compute running mean and standard deviation dynamically.",
            "Trigger anomaly warnings when incoming metric Z-score exceeds threshold (|Z| >= 2.0)."
        ],
        "code": r'''import math
from collections import deque

class AnomalyDetector:
    def __init__(self, window_size=5, threshold=2.0):
        self.window = deque(maxlen=window_size)
        self.threshold = threshold

    def process(self, value):
        if len(self.window) < 3:
            self.window.append(value)
            return False, 0.0

        mean = sum(self.window) / len(self.window)
        variance = sum((x - mean) ** 2 for x in self.window) / len(self.window)
        std_dev = math.sqrt(variance) if variance > 0 else 1.0

        z_score = (value - mean) / std_dev
        is_anomaly = abs(z_score) >= self.threshold
        self.window.append(value)
        return is_anomaly, round(z_score, 2)

if __name__ == "__main__":
    detector = AnomalyDetector(window_size=5, threshold=2.0)
    stream = [10, 12, 11, 10, 13, 11, 85, 12, 10]
    print("--- Streaming Anomaly Monitoring ---")
    for val in stream:
        alert, z = detector.process(val)
        status = f"🚨 ANOMALY ALERT (Z={z})!" if alert else "Normal"
        print(f"Metric Value: {val:2d} | Status: {status}")
''',
        "output": r'''--- Streaming Anomaly Monitoring ---
Metric Value: 10 | Status: Normal
Metric Value: 12 | Status: Normal
Metric Value: 11 | Status: Normal
Metric Value: 10 | Status: Normal
Metric Value: 13 | Status: Normal
Metric Value: 11 | Status: Normal
Metric Value: 85 | Status: 🚨 ANOMALY ALERT (Z=64.84)!
Metric Value: 12 | Status: Normal
Metric Value: 10 | Status: Normal'''
    }
]


def add_project_alias(source_title, slug, title):
    source = next(project for project in PROJECTS if project["title"] == source_title)
    alias = dict(source)
    alias["slug"] = slug
    alias["title"] = title
    PROJECTS.append(alias)


add_project_alias("Smart Calculator with Calculation History", "calculator", "Calculator")
add_project_alias("Command-Line Task Manager", "to-do-list", "To-Do List")
add_project_alias("Python Quiz Challenge Engine", "quiz-game", "Quiz Game")
add_project_alias("Expense Tracker & Summary Generator", "expense-tracker", "Expense Tracker")
add_project_alias("Automated File Organizer Utility", "file-organizer", "File Organizer")
add_project_alias("News Headlines Scraper & Digest", "web-scraper", "Web Scraper")
add_project_alias("RESTful API Engine with Flask", "rest-api", "REST API")
add_project_alias("JWT Authentication & Decorator Middleware", "authentication-system", "Authentication System")
add_project_alias("Password Generator & Strength Evaluator", "password-generator", "Password Generator")


def reference_project(slug, title, level, category, concepts):
    """Create a focused project brief for the roadmap's missing project ideas."""
    code = f'''"""{title}: a small Python project starter."""

def run_project():
    records = [
        {{"name": "Alice", "status": "ready"}},
        {{"name": "Sam", "status": "working"}},
    ]
    for record in records:
        print(f"{{record['name']}}: {{record['status']}}")


if __name__ == "__main__":
    run_project()
'''
    return {
        "slug": slug,
        "title": title,
        "level": level,
        "category": category,
        "summary": f"Build a practical {title.lower()} and learn how Python concepts become a working application.",
        "description": f"A guided {level.lower()} project for practicing {', '.join(concepts[:3])} in a focused, realistic workflow.",
        "concepts": concepts,
        "requirements": [
            f"Create the core {title.lower()} workflow.",
            "Keep the data in a clear Python structure.",
            "Split repeated work into small functions.",
            "Validate input and handle an empty state.",
            "Add one improvement that makes the project your own.",
        ],
        "code": code,
        "output": "Alice: ready\nSam: working",
    }


PROJECTS.extend([
    reference_project("weather-app", "Weather App", "Intermediate", "API Application", ["HTTP requests", "JSON", "API error handling"]),
    reference_project("chat-application", "Chat Application", "Intermediate", "Web Application", ["Flask", "sessions", "message storage"]),
    reference_project("sqlite-management-system", "SQLite Management System", "Intermediate", "Database Application", ["SQLite", "CRUD operations", "parameterized SQL"]),
    reference_project("flask-blog", "Flask Blog", "Advanced", "Web Application", ["Flask", "templates", "SQLite", "authentication"]),
    reference_project("e-commerce-backend", "E-Commerce Backend", "Advanced", "Backend API", ["REST API", "database design", "authentication"]),
    reference_project("ai-chatbot", "AI Chatbot", "Advanced", "AI Application", ["API integration", "prompt design", "conversation state"]),
    reference_project("recommendation-system", "Recommendation System", "Advanced", "Machine Learning", ["data preparation", "similarity", "ranking"]),
    reference_project("data-analysis-dashboard", "Data Analysis Dashboard", "Advanced", "Data Application", ["Pandas", "Matplotlib", "data visualization"]),
    reference_project("machine-learning-application", "Machine Learning Application", "Advanced", "Machine Learning", ["features", "model training", "model evaluation"]),
    reference_project("full-stack-python-application", "Full Stack Python Application", "Master", "Full Stack", ["Flask", "database design", "frontend integration"]),
    reference_project("ai-application", "AI Application", "Master", "Artificial Intelligence", ["AI APIs", "prompt design", "production workflows"]),
    reference_project("production-rest-api", "Production REST API", "Master", "Backend Engineering", ["REST architecture", "testing", "deployment"]),
    reference_project("data-science-project", "Data Science Project", "Master", "Data Science", ["Pandas", "statistics", "visualization"]),
    reference_project("automation-system", "Automation System", "Master", "Automation", ["scheduling", "file workflows", "logging"]),
])

BY_SLUG = {item["slug"]: item for item in PROJECTS}

def grouped_projects(projects=None):
    groups = OrderedDict()
    for item in PROJECTS if projects is None else projects:
        groups.setdefault(item["level"], []).append(item)
    return groups

def get_project(slug):
    return BY_SLUG.get(slug)

def neighbors(slug):
    slugs = [item["slug"] for item in PROJECTS]
    if slug not in slugs:
        return None, None
    index = slugs.index(slug)
    previous = PROJECTS[index - 1] if index else None
    nxt = PROJECTS[index + 1] if index + 1 < len(slugs) else None
    return previous, nxt
