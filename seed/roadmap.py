"""The canonical Python Master roadmap and its learner-facing lesson topics."""

ROADMAP_LEVELS = [
    (0, "Computer + Programming Basics", ["Computer hardware", "Software", "Programming", "Programming languages", "Algorithms", "Flowcharts", "Source code", "Python overview"]),
    (1, "Python Setup + Syntax", ["Installing Python", "VS Code setup", "The Python interpreter", "Syntax rules", "Comments", "Indentation", "Naming conventions", "First Python program"]),
    (2, "Variables + Data Types", ["Variables", "Integers", "Floats", "Strings", "Booleans", "None", "Type checking", "Type conversion"]),
    (3, "Operators", ["Arithmetic operators", "Assignment operators", "Comparison operators", "Logical operators", "Identity operators", "Membership operators", "Bitwise operators", "Operator precedence"]),
    (4, "Input + Output", ["print()", "input()", "Formatted output", "Escape characters", "Reading numbers", "Multiple values", "Output formatting", "Interactive programs"]),
    (5, "If / Else", ["if statements", "if and else", "elif branches", "Nested conditions", "Comparison logic", "Truthiness", "Conditional expressions", "Guard clauses"]),
    (6, "Loops", ["for loops", "while loops", "range()", "Nested loops", "break", "continue", "pass", "Loop else"]),
    (7, "Strings", ["Creating strings", "Indexing", "Slicing", "Concatenation", "String formatting", "String methods", "Searching text", "Splitting and joining"]),
    (8, "Lists", ["Creating lists", "Indexing lists", "Slicing lists", "Adding items", "Removing items", "Sorting lists", "Nested lists", "List comprehensions"]),
    (9, "Tuples + Sets", ["Creating tuples", "Tuple unpacking", "Tuple methods", "Immutable data", "Creating sets", "Adding and removing set items", "Set union and intersection", "Set membership"]),
    (10, "Dictionaries", ["Creating dictionaries", "Keys and values", "Reading values", "Adding and updating", "Removing entries", "Dictionary methods", "Nested dictionaries", "Dictionary comprehensions"]),
    (11, "Functions", ["Defining functions", "Parameters", "Arguments", "Return values", "Default arguments", "Keyword arguments", "Scope", "Reusable design"]),
    (12, "Recursion", ["Recursive thinking", "Base cases", "Call stacks", "Recursive counters", "Factorial recursion", "Tree recursion", "Recursive search", "When to use recursion"]),
    (13, "Modules + Packages", ["import", "from import", "Aliases", "Built-in modules", "Custom modules", "Packages", "__name__", "Virtual environments"]),
    (14, "Exception Handling", ["Errors and exceptions", "try and except", "else and finally", "Multiple exceptions", "Raising exceptions", "Custom exceptions", "Validation", "Defensive programs"]),
    (15, "File Handling", ["Opening files", "Reading text", "Writing text", "Appending data", "File modes", "with blocks", "CSV files", "JSON files"]),
    (16, "OOP", ["Classes", "Objects", "Attributes", "Methods", "__init__", "self", "Class variables", "Instance variables"]),
    (17, "Advanced OOP", ["Encapsulation", "Inheritance", "Multiple inheritance", "Polymorphism", "Abstraction", "Composition", "Properties", "Magic methods"]),
    (18, "Iterators + Generators", ["Iterable objects", "iter()", "next()", "Iterator classes", "yield", "Generator functions", "Generator expressions", "Lazy evaluation"]),
    (19, "Decorators", ["Functions as values", "Nested functions", "Closures", "Basic decorators", "Decorator arguments", "functools.wraps", "Class decorators", "Practical logging"]),
    (20, "Lambda + Functional Programming", ["Lambda functions", "map()", "filter()", "reduce()", "sorted() keys", "Higher-order functions", "Pure functions", "Composing transformations"]),
    (21, "Regular Expressions", ["Regex basics", "Character classes", "Quantifiers", "Groups", "re.search()", "re.findall()", "re.sub()", "Input validation"]),
    (22, "SQLite + SQL", ["Database concepts", "SQLite connections", "Creating tables", "Inserting rows", "Selecting data", "Updating and deleting", "Parameterized queries", "Transactions"]),
    (23, "APIs + JSON", ["API concepts", "HTTP methods", "GET requests", "POST requests", "JSON objects", "Parsing responses", "API errors", "Building an API client"]),
    (24, "Web Scraping", ["HTML structure", "HTTP requests", "BeautifulSoup", "Selecting elements", "Extracting text", "Pagination", "Respectful scraping", "Saving scraped data"]),
    (25, "Flask", ["Flask application", "Routes", "Path parameters", "Templates", "Jinja variables", "Forms", "Static files", "JSON responses"]),
    (26, "Django", ["Django project", "Apps", "URLs", "Views", "Templates", "Models", "Admin", "Forms"]),
    (27, "Testing", ["Why testing matters", "Assertions", "pytest", "unittest", "Fixtures", "Test organization", "Mocking", "Coverage"]),
    (28, "Git + GitHub", ["Repositories", "Commits", "Branches", "Merging", "Remote repositories", "Pull requests", "Issues", "Collaboration"]),
    (29, "Automation", ["Automation mindset", "Path operations", "File automation", "Folder automation", "CSV automation", "Email automation", "Scheduled scripts", "Browser automation"]),
    (30, "NumPy", ["Arrays", "Array shapes", "Indexing arrays", "Vectorized operations", "Broadcasting", "Aggregations", "Random data", "Saving arrays"]),
    (31, "Pandas", ["Series", "DataFrames", "Loading data", "Selecting columns", "Filtering rows", "Missing values", "Grouping data", "Exporting data"]),
    (32, "Matplotlib", ["Plot basics", "Line charts", "Bar charts", "Scatter plots", "Labels and legends", "Subplots", "Styling charts", "Saving figures"]),
    (33, "Data Analysis", ["Asking questions", "Collecting data", "Cleaning data", "Exploring distributions", "Summary statistics", "Finding patterns", "Communicating insights", "Analysis projects"]),
    (34, "Machine Learning", ["ML concepts", "Features and labels", "Training data", "Classification", "Regression", "Model evaluation", "Overfitting", "Prediction projects"]),
    (35, "AI with Python", ["AI concepts", "Neural networks", "Language models", "Embeddings", "Prompt design", "Using AI APIs", "Responsible AI", "AI applications"]),
    (36, "Advanced Projects", ["Project planning", "Architecture", "Reusable code", "Databases in projects", "Testing projects", "Deployment", "Documentation", "Portfolio projects"]),
]


def course_levels():
    """Return the seed format used by the curriculum builder."""
    return [(f"Level {level}", title, track_for(level), topics) for level, title, topics in ROADMAP_LEVELS]


def track_for(level):
    if level <= 10:
        return "PYTHON BEGINNER"
    if level <= 21:
        return "PYTHON INTERMEDIATE"
    if level <= 29:
        return "PROFESSIONAL PYTHON"
    if level <= 35:
        return "PYTHON MASTERY"
    return "PYTHON MASTERY"
