"""Presentation helpers for deep, comprehensive PyMaster lessons."""

import json
from models import db, CodeExample, PracticeProblem, QuizQuestion

ANALOGIES = {
    "Variables": "Think of a variable like a labeled box in a warehouse where you store information for quick access.",
    "Functions": "Think of a function like a custom kitchen appliance: you provide raw ingredients (inputs), it performs a processing job, and hands back a finished meal (return value).",
    "Conditional": "A condition is like a decision checkpoint at a fork in the road: if it is raining, take the left path with an umbrella; otherwise, take the right path.",
    "Loops": "A loop is like an automated factory conveyor belt: it repeats a specific action for every single item until the container is empty.",
    "Lists": "A list is like a multi-compartment organizer tray: keeping items ordered, accessible by slot index, and easy to modify.",
    "Dictionaries": "A dictionary is like a digital phone directory: you look up a unique contact name (key) to instantly retrieve their phone number (value).",
    "Classes": "A class is an architectural blueprint for a house, while objects are the actual physical houses built from that blueprint.",
    "Exceptions": "Exception handling is like an airbag system in a car: when an unexpected crash event occurs, it inflates smoothly so the trip doesn't end abruptly.",
}

LOGICAL_QUIZZES = {
    "computer": (
        "What is the main role of a computer's CPU?",
        ["Execute program instructions and process data", "Store files permanently", "Provide internet connection", "Display web graphics"],
        "Execute program instructions and process data",
        "The Central Processing Unit (CPU) executes code instructions and performs logical computations."
    ),
    "software": (
        "What is software?",
        ["A collection of instructions that tells hardware what to do", "The physical monitor and keyboard", "A type of internet cable", "A computer battery"],
        "A collection of instructions that tells hardware what to do",
        "Software consists of code programs and applications that direct computer hardware."
    ),
    "programming": (
        "What is computer programming?",
        ["Writing step-by-step instructions for a computer to execute", "Fixing physical computer monitors", "Browsing social media", "Typing fast on a keyboard"],
        "Writing step-by-step instructions for a computer to execute",
        "Programming is crafting algorithms and instructions in code to automate tasks."
    ),
    "language": (
        "Why do developers use high-level programming languages like Python?",
        ["They are readable and easier for humans to write than binary code", "Computers only understand English", "They eliminate all software bugs", "They do not require memory"],
        "They are readable and easier for humans to write than binary code",
        "High-level languages provide human-friendly syntax that translates into machine instructions."
    ),
    "algorithm": (
        "What is an algorithm?",
        ["A step-by-step set of rules or instructions to solve a problem", "A type of computer hardware", "A database server", "A syntax error"],
        "A step-by-step set of rules or instructions to solve a problem",
        "An algorithm is a logical sequence of steps designed to perform a specific calculation or task."
    ),
    "compiler": (
        "How does a Python interpreter run code compared to a compiled language?",
        ["It executes code line-by-line at runtime", "It converts code to a standalone executable binary first", "It requires no memory", "It only runs HTML files"],
        "It executes code line-by-line at runtime",
        "Python is an interpreted language that reads and executes code line by line."
    ),
    "what is python": (
        "Which feature makes Python popular among beginners and professionals?",
        ["Clean, readable syntax and a massive ecosystem of libraries", "It requires complex syntax with curly braces on every line", "It only works on mobile phones", "It has no data types"],
        "Clean, readable syntax and a massive ecosystem of libraries",
        "Python emphasizes code readability and provides thousands of built-in and community packages."
    ),
    "variable": (
        "What does `x = 10` do in Python?",
        ["Assigns integer 10 to variable name x", "Checks if x is equal to 10", "Prints 10 on the screen", "Creates a float"],
        "Assigns integer 10 to variable name x",
        "A single equals sign = is the assignment operator that binds a value to a variable name."
    ),
    "data type": (
        "Which function returns the data type of a value in Python?",
        ["type()", "typeof()", "kind()", "datatype()"],
        "type()",
        "type(obj) returns the built-in data type of the given object."
    ),
    "int": (
        "Which value is of type `int`?",
        ["42", "'42'", "42.0", "True"],
        "42",
        "Whole numbers without decimals (like 42) belong to the int data type."
    ),
    "string": (
        "How do you define a string literal in Python?",
        ["Enclose text in single or double quotes", "Wrap text in angle brackets < >", "Prefix text with #", "Use square brackets [ ]"],
        "Enclose text in single or double quotes",
        "Strings in Python are created by enclosing text in matching single ('') or double (\"\") quotes."
    ),
    "boolean": (
        "What are the two possible Boolean values in Python?",
        ["True and False", "1 and -1", "Yes and No", "Valid and Invalid"],
        "True and False",
        "Python Booleans have exactly two state values: True and False (capitalized)."
    ),
    "input": (
        "What data type does the `input()` function always return by default?",
        ["str (String)", "int (Integer)", "float (Float)", "bool (Boolean)"],
        "str (String)",
        "input() reads user input from standard input as a text string."
    ),
    "operator": (
        "What is the result of integer floor division `17 // 5` in Python?",
        ["3", "3.4", "2", "3.0"],
        "3",
        "The floor division operator // calculates the integer quotient, discarding decimals."
    ),
    "if": (
        "Which keyword starts a conditional evaluation block in Python?",
        ["if", "when", "check", "where"],
        "if",
        "if statements evaluate boolean expressions to branch program execution."
    ),
    "break": (
        "What does the `break` statement do inside a loop in Python?",
        ["Exits the innermost loop immediately", "Skips to the next iteration of the loop", "Restarts the loop from index 0", "Pauses execution for 1 second"],
        "Exits the innermost loop immediately",
        "break terminates execution of the enclosing for or while loop immediately."
    ),
    "continue": (
        "What does the `continue` statement do inside a loop?",
        ["Skips the rest of the current iteration and moves to the next cycle", "Terminates the loop entirely", "Raises a SyntaxError", "Returns None to caller"],
        "Skips the rest of the current iteration and moves to the next cycle",
        "continue stops the current loop iteration and proceeds directly to the next cycle evaluation."
    ),
    "pass": (
        "What is the purpose of the `pass` statement in Python?",
        ["Serves as a null placeholder where code is syntactically required", "Passes variables to a function", "Exits the program immediately", "Deletes a variable"],
        "Serves as a null placeholder where code is syntactically required",
        "pass is a no-operation placeholder statement used when syntax requires a code block."
    ),
    "range": (
        "What elements are generated by `list(range(2, 8, 2))` in Python?",
        ["[2, 4, 6]", "[2, 4, 6, 8]", "[2, 3, 4, 5, 6, 7]", "[0, 2, 4, 6]"],
        "[2, 4, 6]",
        "range(start, stop, step) starts at 2, increments by 2, and stops before reaching 8."
    ),
    "loop": (
        "What does `range(3)` generate in a `for` loop?",
        ["0, 1, 2", "1, 2, 3", "1, 2", "0, 1, 2, 3"],
        "0, 1, 2",
        "range(3) yields 3 sequential integers starting from 0: 0, 1, and 2."
    ),
    "slicing": (
        "What does `text[1:4]` return if `text = 'PYTHON'`?",
        ["'YTH'", "'PYTH'", "'YTHO'", "'P'"],
        "'YTH'",
        "Slicing [1:4] extracts characters starting from index 1 up to (excluding) index 4."
    ),
    "indexing": (
        "What does `nums[-1]` return for list `nums = [10, 20, 30, 40]`?",
        ["40", "10", "30", "-1"],
        "40",
        "Negative index -1 accesses the very last element of a Python sequence."
    ),
    "comment": (
        "How do you write a single-line comment in Python?",
        ["Start line with #", "Enclose in <!-- -->", "Start line with //", "Wrap in /* */"],
        "Start line with #",
        "The # character indicates the start of a single-line comment in Python."
    ),
    "list": (
        "How do you add a new item `5` to the end of a list named `nums`?",
        ["nums.append(5)", "nums.add(5)", "nums.push(5)", "nums.insert_end(5)"],
        "nums.append(5)",
        "The append() method appends an element to the end of an existing list."
    ),
    "tuple": (
        "What is the key difference between a list and a tuple in Python?",
        ["Tuples are immutable (cannot be modified after creation)", "Lists cannot contain numbers", "Tuples use square brackets", "Lists are faster than tuples"],
        "Tuples are immutable (cannot be modified after creation)",
        "Tuples are immutable sequences, whereas lists can be modified (mutable)."
    ),
    "set": (
        "What happens when you add a duplicate element to a Python `set`?",
        ["The set ignores the duplicate and keeps only unique items", "Raises a KeyError", "Creates a nested list", "Appends item to the end"],
        "The set ignores the duplicate and keeps only unique items",
        "Sets in Python automatically deduplicate elements, holding unique items."
    ),
    "dictionary": (
        "How do you access the value associated with key `'name'` in dictionary `user`?",
        ["user['name']", "user.name()", "user(0)", "user->name"],
        "user['name']",
        "Dictionary values are accessed using square bracket key lookup dict[key]."
    ),
    "function": (
        "Which keyword is used to define a custom function in Python?",
        ["def", "function", "func", "define"],
        "def",
        "The def keyword begins a function definition in Python."
    ),
    "lambda": (
        "What is a `lambda` function in Python?",
        ["An anonymous, single-expression function defined inline", "A built-in loop construct", "A database connection wrapper", "A type of exception"],
        "An anonymous, single-expression function defined inline",
        "lambda creates small, unnamed single-expression inline functions."
    ),
    "class": (
        "What is a `class` in Object-Oriented Programming?",
        ["A blueprint for creating objects with attributes and methods", "A list of numbers", "A built-in loop", "An error message"],
        "A blueprint for creating objects with attributes and methods",
        "A class defines the structure and behavior for instances created from it."
    ),
    "exception": (
        "Which block catches runtime errors in Python?",
        ["except", "catch", "error", "handle"],
        "except",
        "In Python, the try...except construct catches and handles exceptions."
    ),
    "file": (
        "What is the best practice for opening files in Python to ensure they close properly?",
        ["Use the `with open(...)` context manager block", "Call file.close() in an infinite loop", "Never call close()", "Use import file"],
        "Use the `with open(...)` context manager block",
        "with open(...) automatically manages closing file handles safely."
    ),
    "json": (
        "Which function converts a Python dictionary into a JSON string?",
        ["json.dumps()", "json.loads()", "json.parse()", "json.encode()"],
        "json.dumps()",
        "json.dumps(obj) serializes Python dictionaries into formatted JSON strings."
    ),
    "sqlite": (
        "Why should you use parameterized queries `cursor.execute(sql, (param,))` in SQLite?",
        ["To prevent SQL Injection security vulnerabilities", "To make queries 10x faster", "To encrypt the database file", "To support HTML"],
        "To prevent SQL Injection security vulnerabilities",
        "Parameterized queries separate SQL instructions from raw input to prevent SQL injection."
    ),
    "api": (
        "Which HTTP status code indicates a successful GET request?",
        ["200 OK", "404 Not Found", "500 Internal Server Error", "301 Redirect"],
        "200 OK",
        "HTTP status code 200 OK signifies a successful request returning valid data."
    )
}

DETAILED_GUIDES = {
    "computer": {
        "what": "<p>A <strong>computer</strong> is an electronic machine that accepts raw input data, processes it according to pre-written software instructions, stores the results in memory, and generates useful output.</p><p>At the fundamental hardware level, computers consist of five core hardware subsystems: the <strong>CPU (Central Processing Unit)</strong> which performs arithmetic and logic computations; <strong>RAM (Random Access Memory)</strong> which provides high-speed volatile storage for active processes; <strong>Secondary Storage (SSD/HDD)</strong> for non-volatile persistent storage; <strong>Input devices</strong> (keyboard, mouse, sensors); and <strong>Output devices</strong> (monitors, speakers, networks).</p>",
        "why": "<p>Understanding computer architecture is essential for programmers. Every Python script you write ultimately executes on physical hardware. Understanding how memory and processing power are utilized enables you to write faster, memory-efficient software that scales efficiently.</p>",
        "simple": "A computer is an automated processor that takes data, follows instructions (code), and produces an output result.",
        "analogy": "Think of a computer like a commercial restaurant kitchen: the CPU is the Head Chef, RAM is the prep station counter space, SSD storage is the walk-in pantry, and the recipes are the software code.",
        "syntaxes": [
            {"label": "1. System Information Querying", "code": "import sys, os\nprint(sys.platform)\nprint(os.cpu_count())"},
            {"label": "2. Process Identification", "code": "import os\npid = os.getpid()\nprint('PID:', pid)"}
        ],
        "examples": [
            {
                "title": "Example 1: Inspecting Host Hardware & Python Environment",
                "code": "import sys\nimport os\n\nprint('Python Engine:', sys.version.split()[0])\nprint('Operating System Kernel:', sys.platform)\nprint('CPU Logical Cores:', os.cpu_count())\nprint('Current Process ID:', os.getpid())",
                "breakdown": "<p>Imports Python's built-in <code>sys</code> and <code>os</code> modules. Queries the installed Python interpreter version, kernel platform, CPU count, and allocated OS process ID.</p>",
                "output": "Python Engine: 3.11.4\nOperating System Kernel: win32\nCPU Logical Cores: 8\nCurrent Process ID: 14820"
            },
            {
                "title": "Example 2: Measuring CPU Execution Time for Computations",
                "code": "import time\n\nstart_time = time.perf_counter()\n# Perform 1 million arithmetic steps\ntotal = sum(i for i in range(1_000_000))\nend_time = time.perf_counter()\n\nelapsed_ms = (end_time - start_time) * 1000\nprint(f'Computed sum {total:,} in {elapsed_ms:.2f} ms')",
                "breakdown": "<p>Measures how many milliseconds the CPU takes to loop 1 million times and calculate the total sum using <code>time.perf_counter()</code>.</p>",
                "output": "Computed sum 499,999,500,000 in 48.20 ms"
            }
        ],
        "works": "<p>When you trigger Python code, the Operating System loads the Python Interpreter executable into RAM. The OS scheduler assigns thread execution time on CPU cores. Instructions are loaded from memory into CPU registers, decoded by the ALU (Arithmetic Logic Unit), and executed at clock cycle frequencies (GHz).</p>",
        "mistakes": [
            "Assuming RAM stores files permanently (RAM clears when power turns off).",
            "Confusing CPU processing speed (GHz) with storage capacity (GB/TB).",
            "Writing infinite loops that freeze CPU thread execution."
        ],
        "best": [
            "Monitor CPU and RAM consumption when writing loops and working with large data files.",
            "Close file handles and network sockets to release RAM back to the operating system.",
            "Write efficient algorithms to minimize unnecessary CPU instruction cycles."
        ],
        "usage": "Hardware knowledge forms the basis of systems programming, cloud architecture (AWS/GCP), game engine development, and high-performance data processing.",
        "try": "Run the script above and print the current working directory path using <code>os.getcwd()</code>."
    },
    "installing python": {
        "what": "<p>Installing Python means placing the Python interpreter on your computer so it can read and execute <code>.py</code> files. Visual Studio Code (VS Code) is the editor where you write those files; it does not install Python by itself.</p><p>You need three pieces: <strong>Python</strong>, <strong>VS Code</strong>, and the official <strong>Python extension for VS Code</strong>. The extension connects your editor to a selected Python interpreter.</p>",
        "why": "<p>A correct setup lets you run the same program from the terminal, VS Code's Run button, and the debugger. A project virtual environment keeps each project's packages separate, so installing a library for one project does not break another.</p>",
        "simple": "Install Python, verify it from a terminal, install VS Code and its Python extension, select the interpreter, then run a small <code>hello.py</code> file.",
        "analogy": "Python is the engine that executes your program, VS Code is the workshop where you edit it, and a virtual environment is a separate toolbox for one project.",
        "syntaxes": [
            {"label": "1. Verify Python on Windows", "code": "py --version\npython --version\npy -0p"},
            {"label": "2. Create and activate a project environment (Windows PowerShell)", "code": "mkdir my-python-project\ncd my-python-project\npy -m venv .venv\n.\\.venv\\Scripts\\Activate.ps1"},
            {"label": "3. Create, run, and install a package", "code": "code .\npython hello.py\npython -m pip install requests\npython -m pip freeze > requirements.txt"},
            {"label": "4. Equivalent commands on macOS/Linux", "code": "python3 --version\npython3 -m venv .venv\nsource .venv/bin/activate\npython hello.py"}
        ],
        "examples": [
            {
                "title": "Example 1: Install Python on Windows",
                "code": "1. Open https://www.python.org/downloads/\n2. Download the current Python 3 release.\n3. Start the installer.\n4. Enable 'Add python.exe to PATH'.\n5. Choose 'Install Now'.\n6. Close and reopen VS Code after installation.\n\n# In a new PowerShell terminal, verify the installation:\npy --version\npython --version",
                "breakdown": "<p>Download Python only from <code>python.org</code>. The PATH checkbox lets the <code>python</code> command work in a new terminal. Windows also provides the <code>py</code> launcher, which is usually the most reliable command for selecting an installed Python version.</p>",
                "output": "Python 3.12.6\nPython 3.12.6"
            },
            {
                "title": "Example 2: Create and run hello.py in VS Code",
                "code": "# hello.py\nname = input('What is your name? ')\nprint(f'Hello, {name}!')\n\n# Terminal commands:\nmkdir my-python-project\ncd my-python-project\ncode .\npython hello.py",
                "breakdown": "<p>Create a folder, open that folder in VS Code with <code>code .</code>, create a file named <code>hello.py</code>, and run it from the integrated terminal. In VS Code, use <strong>Ctrl+Shift+P</strong>, choose <strong>Python: Select Interpreter</strong>, and select the interpreter inside <code>.venv</code> when one exists.</p>",
                "output": "What is your name? Ada\nHello, Ada!"
            },
            {
                "title": "Example 3: Use a virtual environment and install a package",
                "code": "# Windows PowerShell\npy -m venv .venv\n.\\.venv\\Scripts\\Activate.ps1\npython -m pip install --upgrade pip\npython -m pip install requests\npython -c \"import requests; print(requests.__version__)\"\n\n# Leave the environment when finished:\ndeactivate",
                "breakdown": "<p><code>venv</code> creates an isolated environment. After activation, <code>python</code> and <code>pip</code> point to that project environment. Using <code>python -m pip</code> makes sure the package is installed into the same interpreter that will run your program.</p>",
                "output": "24.2\n"
            }
        ],
        "works": "<p>When you run <code>python hello.py</code>, the operating system starts the selected Python interpreter and passes it the script path. VS Code's Python extension detects installed interpreters and uses the selected one for Run, Debug, linting, and package discovery. A virtual environment is a folder containing a separate interpreter configuration and package directory; its activation changes which commands the terminal resolves.</p>",
        "mistakes": [
            "Installing VS Code but not installing Python; VS Code is an editor and cannot execute Python alone.",
            "Forgetting to enable <strong>Add python.exe to PATH</strong>, then testing in an old terminal that has not been reopened.",
            "Selecting a global Python interpreter in VS Code when the project should use <code>.venv</code>.",
            "Running <code>pip install</code> from a different interpreter; prefer <code>python -m pip install package_name</code>.",
            "Saving the file as <code>hello.py.txt</code> because file extensions are hidden in Windows Explorer.",
            "Typing PowerShell activation commands in Command Prompt, or using the Windows command inside macOS/Linux."
        ],
        "best": [
            "Use one project folder and one <code>.venv</code> per project.",
            "Select the project's <code>.venv</code> interpreter in VS Code before running or debugging.",
            "Upgrade pip and install packages with <code>python -m pip</code> rather than relying on a separate pip command.",
            "Keep dependencies reproducible with <code>python -m pip freeze &gt; requirements.txt</code>.",
            "Do not commit the <code>.venv</code> folder; add <code>.venv/</code> to <code>.gitignore</code>."
        ],
        "usage": "This setup is the foundation for scripts, web applications, data analysis, automation, testing, APIs, and every other Python project built in PyMaster.",
        "try": "Create <code>hello.py</code> in a new VS Code folder. Run <code>py --version</code>, create <code>.venv</code>, select it with <strong>Python: Select Interpreter</strong>, and run the file with both the terminal command <code>python hello.py</code> and VS Code's play button. Then install one small package with <code>python -m pip install colorama</code> and record the environment with <code>python -m pip freeze &gt; requirements.txt</code>."
    },
    "variable": {
        "what": "<p>In Python, a <strong>variable</strong> is a named reference that points to a specific object stored in memory. Python uses <em>dynamic typing</em>, meaning you do not need to declare variable types explicitly (like <code>int</code> or <code>String</code>). Python automatically detects the data type when a value is assigned.</p><p>When you write <code>total_score = 100</code>, Python creates an integer object <code>100</code> in memory and binds the name <code>total_score</code> as a pointer to that object.</p>",
        "why": "<p>Variables allow programs to store, retrieve, and update state dynamically. Without variables, code would be static and unable to process changing user input, database queries, or mathematical calculations.</p>",
        "simple": "A variable is a labeled container that holds a piece of information so you can use and change it later.",
        "analogy": "Imagine a storage warehouse where boxes have sticky labels. The name on the sticky label lets you quickly pull out and update whatever item is inside.",
        "syntaxes": [
            {"label": "1. Basic Declaration & Initialization", "code": "x = 10\nuser_name = 'Alice'\nis_active = True"},
            {"label": "2. Multiple & Unpacking Assignment", "code": "a, b, c = 1, 2, 3\nx = y = z = 0"},
            {"label": "3. Type Annotations (Python 3.6+)", "code": "age: int = 25\nprice: float = 19.99\ntitle: str = 'PyMaster'"}
        ],
        "examples": [
            {
                "title": "Example 1: Basic Variable Initialization & Math Operations",
                "code": "player_name = 'Alex'\nscore = 50\nmultiplier = 1.5\n\n# Calculate final score\nfinal_score = score * multiplier\nprint('Player:', player_name)\nprint('Initial Score:', score)\nprint('Final Score:', final_score)",
                "breakdown": "<p>Defines string, integer, and float variables. Multiplies <code>score</code> by <code>multiplier</code> and outputs formatted results.</p>",
                "output": "Player: Alex\nInitial Score: 50\nFinal Score: 75.0"
            },
            {
                "title": "Example 2: Real-World E-Commerce Receipt Calculation",
                "code": "item_name = 'Python Handbook'\nunit_price = 29.99\nquantity = 3\ntax_rate = 0.08\n\nsubtotal = unit_price * quantity\ntax_amount = subtotal * tax_rate\ngrand_total = subtotal + tax_amount\n\nprint(f'Receipt for: {item_name}')\nprint(f'Subtotal ({quantity} items): ${subtotal:.2f}')\nprint(f'Tax (8%): ${tax_amount:.2f}')\nprint(f'Grand Total: ${grand_total:.2f}')",
                "breakdown": "<p>Computes subtotal, tax amount, and final charge using floating-point math variables formatted with f-strings.</p>",
                "output": "Receipt for: Python Handbook\nSubtotal (3 items): $89.97\nTax (8%): $7.20\nGrand Total: $97.17"
            },
            {
                "title": "Example 3: Dynamic Reassignment & Type Swap",
                "code": "data = 42\nprint('Initial value:', data, '| Type:', type(data))\n\ndata = 'Forty Two'\nprint('Reassigned value:', data, '| Type:', type(data))",
                "breakdown": "<p>Demonstrates Python's dynamic typing. Variable <code>data</code> points to an integer object <code>42</code>, then is reassigned to point to a string <code>'Forty Two'</code>.</p>",
                "output": "Initial value: 42 | Type: <class 'int'>\nReassigned value: Forty Two | Type: <class 'str'>"
            }
        ],
        "works": "<p>In C/C++, variables are named memory locations containing raw bytes. In Python, variables are pointers stored in a namespace dictionary (<code>locals()</code> / <code>globals()</code>). When a variable is reassigned, Python changes the pointer target. Unreferenced old objects are automatically cleaned up by Python's Garbage Collector via reference counting.</p>",
        "mistakes": [
            "Attempting to use a variable before assigning a value to it (causes <code>NameError</code>).",
            "Confusing the single assignment operator <code>=</code> with the comparison operator <code>==</code>.",
            "Using reserved Python keywords (e.g. <code>for</code>, <code>class</code>, <code>import</code>) as variable names.",
            "Starting variable names with numbers or using spaces (e.g., <code>1st_user</code> is illegal syntax)."
        ],
        "best": [
            "Follow PEP 8 naming standards: use lowercase words separated by underscores (<code>snake_case</code>).",
            "Use clear, descriptive names (e.g. <code>user_email_address</code> instead of <code>u_e</code>).",
            "Keep variable scope as narrow as possible to prevent unintended bugs across functions.",
            "Treat constants with ALL_CAPS names (e.g. <code>MAX_LOGIN_ATTEMPTS = 5</code>)."
        ],
        "usage": "Variables are used in every single line of production software—from storing web session tokens, API request payloads, configuration settings, to AI model parameters.",
        "try": "Create variables for <code>item_price = 49.99</code> and <code>tax_rate = 0.08</code>. Compute <code>total_price</code> and print a custom receipt message."
    },
    "function": {
        "what": "<p>A <strong>function</strong> is a reusable block of structured code designed to perform a single, specific task. Functions take optional inputs (known as <em>parameters</em>), execute logical statements, and optionally pass back an output value using the <code>return</code> keyword.</p><p>Functions promote the <strong>DRY (Don't Repeat Yourself)</strong> software engineering principle by avoiding duplicate code.</p>",
        "why": "<p>Without functions, complex programs would require repeating thousands of lines of identical code. Functions make code modular, readable, easy to test, and effortless to maintain.</p>",
        "simple": "A function is a saved recipe: you give it raw ingredients, it runs the cooking steps, and serves up the final dish.",
        "analogy": "Think of a function like a calculator button marked '√'. You type in a number (argument), press the button (call function), and it returns the square root result.",
        "syntaxes": [
            {"label": "1. Basic Function Definition & Return", "code": "def greet(name):\n    return f'Hello, {name}!'\n\nmsg = greet('Alice')"},
            {"label": "2. Function with Default Parameter Values", "code": "def power(base, exponent=2):\n    return base ** exponent\n\nprint(power(5))     # 25\nprint(power(5, 3))  # 125"},
            {"label": "3. Variable Arguments (*args & **kwargs)", "code": "def log_activity(*events, **metadata):\n    print('Events:', events)\n    print('Meta:', metadata)"}
        ],
        "examples": [
            {
                "title": "Example 1: Basic Function with Input & Return Value",
                "code": "def calculate_discount(price, discount_percent=10):\n    \"\"\"Calculates final price after applying discount.\"\"\"\n    discount_amount = price * (discount_percent / 100)\n    final_price = price - discount_amount\n    return round(final_price, 2)\n\nprice1 = calculate_discount(100.0)\nprice2 = calculate_discount(250.0, 20)\n\nprint('Item 1 (10% off): $', price1)\nprint('Item 2 (20% off): $', price2)",
                "breakdown": "<p>Defines function <code>calculate_discount</code> with default parameter <code>discount_percent=10</code>. Calculates discount and returns rounded price.</p>",
                "output": "Item 1 (10% off): $ 90.0\nItem 2 (20% off): $ 200.0"
            },
            {
                "title": "Example 2: Real-World User Authentication Helper (Multiple Return Values)",
                "code": "def validate_user(username, password, min_len=6):\n    if len(password) < min_len:\n        return False, 'Password too short'\n    if username.lower() == 'admin' and password == 'secret123':\n        return True, 'Login successful'\n    return False, 'Invalid credentials'\n\nstatus, msg = validate_user('admin', 'secret123')\nprint(f'Status: {status} | Message: {msg}')",
                "breakdown": "<p>Demonstrates returning multiple values (tuple unpacking) to handle user login validation and message feedback.</p>",
                "output": "Status: True | Message: Login successful"
            },
            {
                "title": "Example 3: Dynamic Variable Arguments (*args Expense Totaling)",
                "code": "def calculate_expenses(*amounts):\n    total = sum(amounts)\n    return total\n\nprint('Expense 1:', calculate_expenses(10, 20, 30))\nprint('Expense 2:', calculate_expenses(5.50, 12.25, 3.00, 40.00))",
                "breakdown": "<p>Uses <code>*args</code> to accept any number of positional arguments dynamically into a tuple, allowing variable-length calculations.</p>",
                "output": "Expense 1: 60\nExpense 2: 60.75"
            }
        ],
        "works": "<p>When a function is called, Python creates a new execution stack frame on the call stack containing local variables. When <code>return</code> executes, the stack frame is popped off memory and execution resumes at the caller statement.</p>",
        "mistakes": [
            "Forgetting the <code>return</code> statement (functions return <code>None</code> by default).",
            "Confusing parameters (defined in function header) with arguments (actual values passed during call).",
            "Modifying mutable default arguments like empty lists <code>def add(item, box=[])</code> across multiple calls."
        ],
        "best": [
            "Keep functions short and focused on a single responsibility (Single Responsibility Principle).",
            "Use clear type hints e.g. <code>def greet(name: str) -> str:</code>.",
            "Write docstrings to explain what the function does and what parameters it accepts."
        ],
        "usage": "Functions power web API endpoint controllers, database query wrappers, mathematical calculations, and automated background tasks.",
        "try": "Write a function <code>is_even(number)</code> that returns <code>True</code> if a number is even, and <code>False</code> otherwise. Test it with numbers 7 and 12."
    },
    "list": {
        "what": "<p>A <strong>list</strong> is a built-in, ordered, mutable collection that allows storing multiple items in a single variable. Lists are defined using square brackets <code>[ ]</code> with comma-separated elements.</p><p>Lists can contain mixed data types (integers, strings, floats, booleans, or nested lists) and allow duplicate elements.</p>",
        "why": "<p>Lists are essential whenever you need to process collections of related objects—such as a list of registered users, shopping cart items, temperature readings, or search results.</p>",
        "simple": "A list is an ordered container where you can store, add, remove, and sort multiple items.",
        "analogy": "A list is like a numbered shopping list where every item has a specific line number starting from slot 0.",
        "syntaxes": [
            {"label": "1. List Creation & Index Lookup", "code": "my_list = [10, 20, 30]\nfirst = my_list[0]\nlast = my_list[-1]"},
            {"label": "2. Modifying Lists (Append, Insert, Remove)", "code": "my_list.append(40)\nmy_list.insert(1, 15)\nmy_list.remove(20)"},
            {"label": "3. List Comprehension Syntax", "code": "squares = [x**2 for x in range(5) if x % 2 == 0]"}
        ],
        "examples": [
            {
                "title": "Example 1: Basic List Operations & Slicing",
                "code": "fruits = ['Apple', 'Banana', 'Cherry', 'Dragonfruit']\nprint('First fruit:', fruits[0])\nprint('Last fruit:', fruits[-1])\nprint('Sliced (1 to 2):', fruits[1:3])",
                "breakdown": "<p>Demonstrates 0-based indexing, negative indexing (<code>-1</code> for last element), and sub-list slicing.</p>",
                "output": "First fruit: Apple\nLast fruit: Dragonfruit\nSliced (1 to 2): ['Banana', 'Cherry']"
            },
            {
                "title": "Example 2: Real-World Student Grade Analytics",
                "code": "grades = [88, 92, 75, 95, 82]\ngrades.append(90)\n\naverage_grade = sum(grades) / len(grades)\nhighest_grade = max(grades)\nlowest_grade = min(grades)\n\nprint(f'Total Students: {len(grades)}')\nprint(f'Average Grade: {average_grade:.1f}')\nprint(f'Highest: {highest_grade} | Lowest: {lowest_grade}')",
                "breakdown": "<p>Appends a new score, then uses built-in functions <code>sum()</code>, <code>len()</code>, <code>max()</code>, and <code>min()</code> to generate grade analytics.</p>",
                "output": "Total Students: 6\nAverage Grade: 87.0\nHighest: 95 | Lowest: 75"
            },
            {
                "title": "Example 3: Filtering & Transforming with List Comprehension",
                "code": "prices_in_usd = [12.50, 45.00, 8.99, 100.00, 25.50]\n# Apply 10% discount to items costing over $20\ndiscounted = [round(p * 0.90, 2) for p in prices_in_usd if p > 20.00]\n\nprint('Original prices:', prices_in_usd)\nprint('Discounted expensive items:', discounted)",
                "breakdown": "<p>Uses concise list comprehension with conditional filtering to modify selected elements in a single expression.</p>",
                "output": "Original prices: [12.5, 45.0, 8.99, 100.0, 25.5]\nDiscounted expensive items: [40.5, 90.0, 22.95]"
            }
        ],
        "works": "<p>Python lists are dynamic array representations storing pointers to memory objects. When a list outgrows its allocated space, Python automatically over-allocates extra array slots to provide $O(1)$ amortized append performance.</p>",
        "mistakes": [
            "Accessing an index beyond list length (causes <code>IndexError: list index out of range</code>).",
            "Attempting to modify a list while iterating over it with a simple <code>for</code> loop.",
            "Confusing <code>.sort()</code> (modifies list in-place) with <code>sorted()</code> (returns new sorted list)."
        ],
        "best": [
            "Use List Comprehension <code>[x*2 for x in nums]</code> for concise, fast list transformation.",
            "Use <code>in</code> operator <code>if 'Apple' in fruits:</code> for membership checks.",
            "Use negative indices <code>list[-1]</code> to access the last element cleanly."
        ],
        "usage": "Lists manage data tables, database query result sets, UI menu items, and queue pipelines in enterprise software.",
        "try": "Create a list of 5 numbers. Write code to find and print the maximum number and the average of all numbers."
    },
    "dictionary": {
        "what": "<p>A <strong>dictionary</strong> is an unordered, mutable collection of key-value pairs. Dictionaries are defined using curly braces <code>{ }</code> with <code>key: value</code> syntax. Keys must be unique and immutable (strings, numbers, tuples).</p>",
        "why": "<p>Dictionaries provide extremely fast $O(1)$ average time complexity lookups by key, making them ideal for structured data like JSON records, user profiles, and configuration settings.</p>",
        "simple": "A dictionary lets you look up information by name (key) instead of a position index number.",
        "analogy": "Like a real language dictionary where you look up a word (key) to get its definition (value).",
        "syntaxes": [
            {"label": "1. Dictionary Creation & Access", "code": "user = {'name': 'Alice', 'role': 'Admin'}\nname = user['name']"},
            {"label": "2. Safe Access & Key Updating", "code": "age = user.get('age', 18)\nuser['email'] = 'alice@example.com'"},
            {"label": "3. Iterating Keys and Values", "code": "for key, val in user.items():\n    print(key, '->', val)"}
        ],
        "examples": [
            {
                "title": "Example 1: Basic Key-Value Lookup & Modification",
                "code": "book = {'title': 'Python 101', 'author': 'John Doe', 'pages': 300}\nbook['pages'] = 320\nbook['publisher'] = 'TechPress'\nprint('Book info:', book)",
                "breakdown": "<p>Updates existing key <code>pages</code> and adds new key <code>publisher</code>.</p>",
                "output": "Book info: {'title': 'Python 101', 'author': 'John Doe', 'pages': 320, 'publisher': 'TechPress'}"
            },
            {
                "title": "Example 2: Real-World API Response JSON Parsing",
                "code": "api_response = {\n    'status': 200,\n    'data': {\n        'user_id': 402,\n        'username': 'coder_pro',\n        'is_verified': True\n    }\n}\n\nuser_info = api_response.get('data', {})\nprint('Username:', user_info.get('username'))\nprint('Verified:', user_info.get('is_verified'))",
                "breakdown": "<p>Parses nested dictionary JSON payload safely using <code>.get()</code> without risking KeyError on missing keys.</p>",
                "output": "Username: coder_pro\nVerified: True"
            },
            {
                "title": "Example 3: Word Frequency Counter Pattern",
                "code": "text = 'python code is easy and python is powerful'\nwords = text.split()\nfreq = {}\n\nfor word in words:\n    freq[word] = freq.get(word, 0) + 1\n\nprint('Word Counts:', freq)",
                "breakdown": "<p>Counts frequency of each word in a string using dictionary key counting.</p>",
                "output": "Word Counts: {'python': 2, 'code': 1, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}"
            }
        ],
        "works": "<p>Python dictionaries are implemented using Hash Tables. When a key is requested, Python hashes the key into an integer index to jump directly to memory location in $O(1)$ constant time.</p>",
        "mistakes": [
            "Accessing a non-existent key directly with <code>dict[key]</code> (raises <code>KeyError</code>). Use <code>.get(key)</code> instead.",
            "Using mutable objects like lists as dictionary keys (raises <code>TypeError: unhashable type</code>).",
            "Assuming dictionary key insertion order in Python versions prior to 3.7."
        ],
        "best": [
            "Use <code>.get('key', default_value)</code> to avoid application crashes on missing keys.",
            "Use Dictionary Comprehension <code>{k: v for k, v in data.items()}</code> for data transformation.",
            "Use <code>.items()</code> to loop through keys and values simultaneously."
        ],
        "usage": "Dictionaries power REST API responses, JSON data parsing, session caches, and configuration settings in Flask, Django, and Data Science.",
        "try": "Create a dictionary storing product names and prices. Write code to calculate the total cost of all products."
    }
}


def concept_name(lesson):
    return lesson.title.replace("Introduction to ", "").strip()


def get_logical_quiz(concept):
    concept_lower = concept.lower()
    for key, data in LOGICAL_QUIZZES.items():
        if key in concept_lower:
            return data
    return (
        f"What is the primary function of {concept} in Python programming?",
        [
            f"To provide structured syntax for {concept} execution",
            f"To disable compiler errors automatically",
            f"To convert Python scripts into HTML pages",
            f"To clear RAM memory instantly"
        ],
        f"To provide structured syntax for {concept} execution",
        f"{concept} is a fundamental Python construct used to write clean, maintainable logic."
    )


def build_dynamic_detailed_guide(concept, lesson):
    """Generates deep, comprehensive, multi-syntax and multi-example topic guides."""
    concept_slug = concept.lower().replace(' ', '_')
    code_example = (
        lesson.code_examples[0].code if (hasattr(lesson, 'code_examples') and lesson.code_examples)
        else f"# Practical demonstration of {concept}\nprint('Learning concept:', '{concept}')"
    )

    return {
        "concept": concept,
        "what": f"""<p><strong>{concept}</strong> is a core concept in Python programming. In modern software engineering, mastering <strong>{concept}</strong> enables developers to design scalable logic, manage program state efficiently, and write maintainable code.</p>
        <p>When working with {concept}, Python manages underlying memory allocation, data structures, and execution flow automatically. Understanding how {concept} behaves allows you to write robust applications without unexpected bugs.</p>""",
        
        "why": f"""<p>We use <strong>{concept}</strong> to eliminate redundant logic, structure code logically, and build software that handles real-world data effectively.</p>
        <p>Without {concept}, applications would be rigid, difficult to maintain, and prone to runtime failures. Integrating {concept} into your development workflow makes your codebase clean, testable, and compliant with professional standards.</p>""",
        
        "simple": f"{concept} is an essential building block in Python that helps you store, manage, or automate computational tasks clearly.",
        
        "analogy": f"Think of {concept} as a specialized tool in a master craftsman's toolkit. Just like choosing the right tool makes building physical structures simple and sturdy, using {concept} makes software architecture clean and reliable.",
        
        "syntaxes": [
            {
                "label": f"1. Basic {concept} Declaration & Setup Pattern",
                "code": f"# Basic initialization pattern\n{concept_slug}_data = 'Initial Value'\nprint({concept_slug}_data)"
            },
            {
                "label": f"2. Processing & Evaluation Blueprint",
                "code": f"# Function processing pattern\ndef process_{concept_slug}(item):\n    return f'Processed: {{item}}'\n\nresult = process_{concept_slug}({concept_slug}_data)"
            },
            {
                "label": f"3. Defensive Safety Check Pattern",
                "code": f"# Validation before execution\nif {concept_slug}_data:\n    print('Validation Passed: Ready to execute')"
            }
        ],

        "examples": [
            {
                "title": f"Example 1: Basic {concept} Initialization & Usage",
                "code": code_example,
                "breakdown": f"<p>Sets up basic state for <code>{concept}</code>, executes standard Python processing statements, and outputs the result to standard console output.</p>",
                "output": f"Learning: {concept}"
            },
            {
                "title": f"Example 2: Practical Application Scenario with {concept}",
                "code": f"items = ['alpha', 'beta', 'gamma']\nfor index, item in enumerate(items, 1):\n    print(f'Item {{index}}: {{item.upper()}} ({concept})')",
                "breakdown": f"<p>Loops through items using <code>enumerate()</code> to dynamically apply transformations and track step count.</p>",
                "output": f"Item 1: ALPHA ({concept})\nItem 2: BETA ({concept})\nItem 3: GAMMA ({concept})"
            },
            {
                "title": f"Example 3: Safe Defensive Pattern for {concept}",
                "code": f"def safe_execute(val):\n    if val is None:\n        return 'Warning: No data provided'\n    return f'Success: Executed {concept} on {{val}}'\n\nprint(safe_execute(None))\nprint(safe_execute('Sample Data'))",
                "breakdown": f"<p>Demonstrates defensive error checking to prevent unexpected crashes when invalid or null data is passed.</p>",
                "output": f"Warning: No data provided\nSuccess: Executed {concept} on Sample Data"
            }
        ],

        "works": f"""<p>Under the hood, Python interprets code statements involving <strong>{concept}</strong> by converting them into Python Bytecode (<code>.pyc</code>). The Python Virtual Machine (PVM) reads these bytecode instructions, manages reference counts in memory, and handles garbage collection automatically when references go out of scope.</p>""",
        
        "mistakes": [
            f"Misunderstanding the syntax constraints of {concept} resulting in a <code>SyntaxError</code> or <code>NameError</code>.",
            f"Failing to handle edge cases such as empty values, missing keys, or unexpected data types.",
            f"Not checking variable scopes, causing unexpected state mutations across execution blocks."
        ],
        
        "best": [
            f"Follow PEP 8 clean code guidelines when implementing {concept}.",
            f"Use descriptive variable and function names to keep {concept} logic self-documenting.",
            f"Write unit tests to verify that {concept} handles edge cases cleanly."
        ],
        
        "usage": f"{concept} is widely used across backend development (Flask/Django), cloud automation scripts, data science pipelines (Pandas/NumPy), and desktop tools.",
        
        "try": f"Run the provided code example in your Python environment. Modify one input value, re-run the script, and observe how the output changes."
    }


def guide(lesson):
    concept = concept_name(lesson)
    concept_lower = concept.lower()

    # Search for matching predefined guide
    matched_guide = None
    for key, data in DETAILED_GUIDES.items():
        if key in concept_lower:
            matched_guide = dict(data)
            matched_guide["concept"] = concept
            break

    # If no static guide matched, generate dynamic rich guide
    if not matched_guide:
        matched_guide = build_dynamic_detailed_guide(concept, lesson)

    # Attach real-world analogy fallback if missing
    if "analogy" not in matched_guide or not matched_guide["analogy"]:
        analogy_text = next(
            (text for key, text in ANALOGIES.items() if key.lower() in concept_lower),
            f"Think of {concept} as a reliable building block in your software system."
        )
        matched_guide["analogy"] = analogy_text

    return matched_guide


def add_resources():
    from models import Lesson

    for lesson in Lesson.query.all():
        concept = concept_name(lesson)
        if not lesson.code_examples:
            code = (
                'message = "Hello, Python!"\nprint(message)'
                if "Variable" in concept
                else f'print("Learning: {concept}")'
            )
            db.session.add(
                CodeExample(
                    lesson=lesson,
                    title=f"{concept} example",
                    code=code,
                    explanation=f"A detailed practical example of {concept}.",
                )
            )
        if not lesson.practice_problems:
            db.session.add(
                PracticeProblem(
                    lesson=lesson,
                    title=f"Practice {concept}",
                    prompt=f"Write a short Python program that demonstrates {concept}. Start with the example and modify it to explore edge cases.",
                    starter_code="# Write your code below\n",
                    solution_code=f'print("Learning: {concept}")',
                    difficulty="Beginner",
                )
            )

        question_text, options, correct_ans, explanation = get_logical_quiz(concept)
        if not lesson.quiz_questions:
            db.session.add(
                QuizQuestion(
                    lesson=lesson,
                    question=question_text,
                    options_json=json.dumps(options),
                    correct_answer=correct_ans,
                    explanation=explanation,
                )
            )
        else:
            q = lesson.quiz_questions[0]
            # Always update quiz questions to ensure fresh logical questions and answers
            q.question = question_text
            q.options_json = json.dumps(options)
            q.correct_answer = correct_ans
            q.explanation = explanation

    db.session.commit()
