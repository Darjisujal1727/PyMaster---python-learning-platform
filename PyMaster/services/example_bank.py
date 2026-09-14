"""Python example programs from first print through mastery topics."""

from collections import OrderedDict


def _ex(slug, title, group, intro, code, output, prereqs=(), extra=""):
    return {
        "slug": slug,
        "title": title,
        "group": group,
        "intro": intro,
        "code": code.strip("\n"),
        "output": output.strip("\n"),
        "prereqs": list(prereqs),
        "extra": extra,
    }


EXAMPLES = [
    _ex("print-hello-world", "Print Hello world!", "Getting started",
        "This is the smallest complete Python program. You only need to know how print() works.",
        """# This program prints Hello, world!

print('Hello, world!')""",
        "Hello, world!"),
    _ex("comments", "Write comments in Python", "Getting started",
        "Comments explain code for humans. Python ignores them when the program runs.",
        """# This is a full-line comment
print("Python still runs this line")  # end-of-line comment

'''
A triple-quoted string can also
hold a longer note.
'''""",
        "Python still runs this line",
        ("print-hello-world",)),
    _ex("add-two-numbers", "Add Two Numbers", "Getting started",
        "Store two values, add them, and print the result.",
        """# Add two numbers stored in variables

a = 5
b = 7
total = a + b
print("Sum:", total)""",
        "Sum: 12",
        ("print-hello-world",)),
    _ex("user-input", "Read user input", "Getting started",
        "input() always returns text. Convert it if you need a number.",
        """# Demo values stand in for typed input
name = "Ada"
age_text = "21"
age = int(age_text)
print(f"{name} is {age} years old.")""",
        "Ada is 21 years old.",
        ("add-two-numbers",)),
    _ex("swap-two-variables", "Swap Two Variables", "Getting started",
        "Python can swap values in one line using unpacking.",
        """x = 10
y = 20
print("Before:", x, y)
x, y = y, x
print("After:", x, y)""",
        "Before: 10 20\nAfter: 20 10",
        ("add-two-numbers",)),
    _ex("random-number", "Generate a Random Number", "Getting started",
        "The random module can pick a number in a range.",
        """import random

# randint includes both ends of the range
number = random.randint(1, 6)
print("Dice roll:", number)""",
        "Dice roll: 4",
        ("add-two-numbers",)),
    _ex("km-to-miles", "Convert Kilometers to Miles", "Getting started",
        "Multiply kilometers by 0.621371 to get miles.",
        """km = 5
miles = km * 0.621371
print(f"{km} km is {miles:.2f} miles")""",
        "5 km is 3.11 miles",
        ("add-two-numbers",)),
    _ex("square-root", "Find the Square Root", "Getting started",
        "Use the math module for square roots.",
        """import math

value = 49
print(math.sqrt(value))""",
        "7.0",
        ("add-two-numbers",)),
    _ex("triangle-area", "Calculate the Area of a Triangle", "Getting started",
        "Area of a triangle is half of base times height.",
        """base = 10
height = 6
area = 0.5 * base * height
print("Area:", area)""",
        "Area: 30.0",
        ("add-two-numbers",)),
    _ex("quadratic-equation", "Solve Quadratic Equation", "Getting started",
        "For ax² + bx + c = 0, use the quadratic formula.",
        """import math

a, b, c = 1, -5, 6
d = b ** 2 - 4 * a * c
root1 = (-b + math.sqrt(d)) / (2 * a)
root2 = (-b - math.sqrt(d)) / (2 * a)
print(root1, root2)""",
        "3.0 2.0",
        ("square-root",)),
    _ex("variables-and-types", "Variables and data types", "Variables and types",
        "Names store values. type() reports the kind of value.",
        """count = 3
price = 9.5
label = "books"
ready = True
empty = None
print(type(count), type(price), type(label), type(ready), type(empty))""",
        "<class 'int'> <class 'float'> <class 'str'> <class 'bool'> <class 'NoneType'>",
        ("add-two-numbers",)),
    _ex("type-conversion", "Convert between types", "Variables and types",
        "int(), float(), and str() change a value's type when the conversion is valid.",
        """text = "42"
number = int(text)
print(number + 8)
print(str(number) + " is text now")
print(float("3.5") * 2)""",
        "50\n42 is text now\n7.0",
        ("variables-and-types",)),
    _ex("arithmetic-operators", "Arithmetic operators", "Operators",
        "Python has add, subtract, multiply, divide, floor divide, remainder, and power.",
        """a, b = 17, 5
print("add", a + b)
print("sub", a - b)
print("mul", a * b)
print("div", a / b)
print("floor", a // b)
print("mod", a % b)
print("power", a ** 2)""",
        "add 22\nsub 12\nmul 85\ndiv 3.4\nfloor 3\nmod 2\npower 289",
        ("variables-and-types",)),
    _ex("comparison-logical", "Comparison and logical operators", "Operators",
        "== compares values. and, or, and not combine tests.",
        """score = 75
print(score >= 70)
print(score == 100)
print(score > 50 and score < 90)
print(not score < 40)""",
        "True\nFalse\nTrue\nTrue",
        ("arithmetic-operators",)),
    _ex("operator-precedence", "Operator precedence", "Operators",
        "Multiplication runs before addition unless you use parentheses.",
        """print(2 + 3 * 4)
print((2 + 3) * 4)""",
        "14\n20",
        ("arithmetic-operators",)),
    _ex("if-statement", "If statement", "Conditions",
        "An if block runs only when its test is true.",
        """temperature = 32
if temperature > 30:
    print("It is hot")""",
        "It is hot",
        ("comparison-logical",)),
    _ex("if-else", "If / else", "Conditions",
        "else runs when the if test is false.",
        """age = 16
if age >= 18:
    print("Adult")
else:
    print("Under 18")""",
        "Under 18",
        ("if-statement",)),
    _ex("if-elif-else", "If / elif / else", "Conditions",
        "elif checks extra conditions in order. The first match wins.",
        """marks = 81
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"
print(grade)""",
        "B",
        ("if-else",)),
    _ex("nested-if", "Nested conditions", "Conditions",
        "You can put one if inside another when a second check is needed.",
        """logged_in = True
is_admin = False
if logged_in:
    if is_admin:
        print("Welcome, admin")
    else:
        print("Welcome, user")
else:
    print("Please log in")""",
        "Welcome, user",
        ("if-elif-else",)),
    _ex("ternary", "Conditional expression", "Conditions",
        "A one-line if/else is useful for simple choices.",
        """n = 7
label = "even" if n % 2 == 0 else "odd"
print(label)""",
        "odd",
        ("if-else",)),
    _ex("for-loop", "For loop", "Loops",
        "for visits each item in a sequence.",
        """for fruit in ["apple", "mango", "pear"]:
    print(fruit)""",
        "apple\nmango\npear",
        ("if-statement",)),
    _ex("range-loop", "Loop with range()", "Loops",
        "range(n) counts from 0 up to, but not including, n.",
        """for i in range(4):
    print(i)""",
        "0\n1\n2\n3",
        ("for-loop",)),
    _ex("while-loop", "While loop", "Loops",
        "while repeats as long as the condition stays true.",
        """count = 3
while count > 0:
    print(count)
    count -= 1
print("Go")""",
        "3\n2\n1\nGo",
        ("for-loop",)),
    _ex("break-continue", "break and continue", "Loops",
        "break leaves the loop. continue skips the rest of this round.",
        """for n in range(6):
    if n == 2:
        continue
    if n == 5:
        break
    print(n)""",
        "0\n1\n3\n4",
        ("range-loop",)),
    _ex("nested-loops", "Nested loops", "Loops",
        "An inner loop finishes all of its turns for each outer turn.",
        """for row in range(1, 4):
    line = ""
    for col in range(1, 4):
        line += f"{row * col} "
    print(line.strip())""",
        "1 2 3\n2 4 6\n3 6 9",
        ("range-loop",)),
    _ex("loop-else", "Loop else", "Loops",
        "else after a for/while runs if the loop did not hit break.",
        """for n in [2, 4, 6]:
    if n % 2:
        print("odd found")
        break
else:
    print("all even")""",
        "all even",
        ("break-continue",)),
    _ex("string-index-slice", "String indexing and slicing", "Strings",
        "Strings are sequences of characters. Slicing copies a piece.",
        """text = "Python"
print(text[0], text[-1])
print(text[0:2])
print(text[::-1])""",
        "P n\nPy\nnohtyP",
        ("variables-and-types",)),
    _ex("string-methods", "String methods", "Strings",
        "Methods return new strings. The original text is not changed.",
        """msg = "  Hello Python  "
print(msg.strip())
print(msg.lower())
print("hello python".title())
print("a-b-c".split("-"))
print("-".join(["a", "b", "c"]))""",
        "Hello Python\n  hello python  \nHello Python\n['a', 'b', 'c']\na-b-c",
        ("string-index-slice",)),
    _ex("f-strings", "f-strings and formatting", "Strings",
        "An f-string inserts values inside braces.",
        """name = "Sam"
score = 9.456
print(f"{name} scored {score:.1f}")""",
        "Sam scored 9.5",
        ("string-methods",)),
    _ex("palindrome", "Check a palindrome", "Strings",
        "A palindrome reads the same forwards and backwards.",
        """word = "level"
cleaned = word.lower()
print(cleaned == cleaned[::-1])""",
        "True",
        ("string-index-slice",)),
    _ex("count-vowels", "Count vowels in a string", "Strings",
        "Loop through letters and count a, e, i, o, u.",
        """text = "Education"
vowels = "aeiou"
count = 0
for ch in text.lower():
    if ch in vowels:
        count += 1
print(count)""",
        "5",
        ("for-loop", "string-index-slice")),
    _ex("create-list", "Create and update a list", "Lists",
        "Lists keep ordered items and can grow or shrink.",
        """colors = ["red", "green"]
colors.append("blue")
colors[1] = "yellow"
print(colors)
print(len(colors))""",
        "['red', 'yellow', 'blue']\n3",
        ("for-loop",)),
    _ex("list-methods", "List methods", "Lists",
        "append, insert, pop, remove, sort, and reverse are common tools.",
        """nums = [3, 1, 4, 1]
nums.insert(0, 0)
nums.remove(4)
last = nums.pop()
nums.sort()
print(nums, last)""",
        "[0, 1, 1, 3] 1",
        ("create-list",)),
    _ex("list-slice-copy", "List slicing and copy", "Lists",
        "Slicing copies a range. [:] copies the whole list.",
        """nums = [10, 20, 30, 40, 50]
print(nums[1:4])
copy = nums[:]
copy.append(60)
print(nums)
print(copy)""",
        "[20, 30, 40]\n[10, 20, 30, 40, 50]\n[10, 20, 30, 40, 50, 60]",
        ("create-list",)),
    _ex("nested-list", "Nested lists", "Lists",
        "A list can hold other lists, like a small table.",
        """grid = [[1, 2], [3, 4]]
print(grid[1][0])
for row in grid:
    print(row)""",
        "3\n[1, 2]\n[3, 4]",
        ("create-list",)),
    _ex("list-max-sum", "Sum, max, and min of a list", "Lists",
        "Built-in functions work on any sequence of numbers.",
        """nums = [4, 9, 2, 7]
print(sum(nums), max(nums), min(nums))""",
        "22 9 2",
        ("create-list",)),
    _ex("tuples", "Tuples and unpacking", "Tuples and sets",
        "Tuples are ordered and cannot be changed after creation.",
        """point = (3, 4)
x, y = point
print(x, y)
print(point[0])""",
        "3 4\n3",
        ("create-list",)),
    _ex("sets", "Sets: unique items", "Tuples and sets",
        "A set drops duplicates and is fast for membership tests.",
        """letters = {"a", "b", "a", "c"}
print(sorted(letters))
print("b" in letters)
print(sorted(letters | {"c", "d"}))
print(sorted(letters & {"a", "z"}))""",
        "['a', 'b', 'c']\nTrue\n['a', 'b', 'c', 'd']\n['a']",
        ("create-list",)),
    _ex("dictionaries", "Create a dictionary", "Dictionaries",
        "A dictionary maps unique keys to values.",
        """student = {"name": "Riya", "age": 19}
student["city"] = "Pune"
print(student["name"])
print(student.get("grade", "N/A"))""",
        "Riya\nN/A",
        ("create-list",)),
    _ex("dict-loop", "Loop through a dictionary", "Dictionaries",
        "items() gives each key with its value.",
        """scores = {"math": 88, "english": 91}
for subject, mark in scores.items():
    print(f"{subject}: {mark}")""",
        "math: 88\nenglish: 91",
        ("dictionaries",)),
    _ex("nested-dict", "Nested dictionaries", "Dictionaries",
        "Values can be dictionaries too.",
        """users = {
    "u1": {"name": "Lee", "role": "admin"},
    "u2": {"name": "Pat", "role": "user"},
}
print(users["u1"]["role"])""",
        "admin",
        ("dictionaries",)),
    _ex("define-function", "Create and call a function", "Functions",
        "def names a reusable block. return sends a result back.",
        """def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))""",
        "Hello, Python!",
        ("if-statement",)),
    _ex("default-kwargs", "Default and keyword arguments", "Functions",
        "Defaults fill in missing values. Keyword arguments name what you pass.",
        """def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, exp=3))""",
        "25\n8",
        ("define-function",)),
    _ex("args-kwargs", "*args and **kwargs", "Functions",
        "*args collects extra positional values. **kwargs collects extra names.",
        """def report(*values, **info):
    print(values)
    print(info)

report(1, 2, 3, user="ada", ok=True)""",
        "(1, 2, 3)\n{'user': 'ada', 'ok': True}",
        ("default-kwargs",)),
    _ex("scope", "Local and global scope", "Functions",
        "A name created inside a function is local unless you use global.",
        """count = 1

def bump():
    local_count = count + 10
    return local_count

print(bump())
print(count)""",
        "11\n1",
        ("define-function",)),
    _ex("recursion", "Recursion: factorial", "Functions",
        "A recursive function calls itself with a smaller problem.",
        """def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))""",
        "120",
        ("define-function",)),
    _ex("lambda", "Lambda functions", "Functions",
        "lambda writes a tiny function as one expression.",
        """square = lambda n: n * n
print(square(6))
print(sorted(["pear", "fig", "kiwi"], key=len))""",
        "36\n['fig', 'pear', 'kiwi']",
        ("define-function",)),
    _ex("higher-order", "Higher-order functions", "Functions",
        "map, filter, and a custom function that takes another function.",
        """nums = [1, 2, 3, 4, 5]
print(list(map(lambda n: n * 2, nums)))
print(list(filter(lambda n: n % 2 == 0, nums)))

def apply_twice(fn, value):
    return fn(fn(value))

print(apply_twice(lambda x: x + 1, 3))""",
        "[2, 4, 6, 8, 10]\n[2, 4]\n5",
        ("lambda",)),
    _ex("list-comprehension", "List comprehension", "Comprehensions",
        "Build a new list in one expression.",
        """nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
evens = [n for n in nums if n % 2 == 0]
print(squares)
print(evens)""",
        "[1, 4, 9, 16, 25]\n[2, 4]",
        ("create-list",)),
    _ex("dict-set-comprehension", "Dict and set comprehension", "Comprehensions",
        "The same idea works for dictionaries and sets.",
        """names = ["Ada", "Lin"]
lengths = {name: len(name) for name in names}
unique = {ch for ch in "banana"}
print(lengths)
print(sorted(unique))""",
        "{'Ada': 3, 'Lin': 3}\n['a', 'b', 'n']",
        ("list-comprehension",)),
    _ex("try-except", "try / except", "Errors and files",
        "except lets you recover when something goes wrong.",
        """text = "not-a-number"
try:
    value = int(text)
except ValueError:
    value = 0
print(value)""",
        "0",
        ("type-conversion",)),
    _ex("try-else-finally", "else, finally, and raise", "Errors and files",
        "else runs if no error happened. finally always runs. raise starts an error.",
        """def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b cannot be 0")
    return a / b

try:
    print(divide(10, 2))
except ZeroDivisionError as err:
    print(err)
else:
    print("ok")
finally:
    print("done")""",
        "5.0\nok\ndone",
        ("try-except",)),
    _ex("custom-exception", "Custom exceptions", "Errors and files",
        "Subclass Exception to name a problem in your own code.",
        """class TooSmallError(Exception):
    pass

def check(n):
    if n < 0:
        raise TooSmallError("n must be 0 or more")
    return n

try:
    check(-1)
except TooSmallError as err:
    print(err)""",
        "n must be 0 or more",
        ("try-else-finally",)),
    _ex("file-read-write", "Read and write files", "Errors and files",
        "with open() closes the file for you. This demo uses an in-memory file.",
        """from io import StringIO

buffer = StringIO()
buffer.write("line 1\\nline 2\\n")
print(buffer.getvalue())""",
        "line 1\nline 2",
        ("try-except",),
        "On disk you would use: with open('notes.txt', 'w', encoding='utf-8') as f:"),
    _ex("json-example", "Work with JSON", "Errors and files",
        "json turns Python objects into text and back again.",
        """import json

data = {"ok": True, "items": [1, 2]}
text = json.dumps(data)
print(text)
print(json.loads(text)["items"])""",
        '{"ok": true, "items": [1, 2]}\n[1, 2]',
        ("dictionaries",)),
    _ex("import-module", "Import a module", "Modules",
        "import loads a library. as gives it a shorter name.",
        """import math as m
from datetime import date

print(m.pi)
print(date(2026, 9, 6))""",
        "3.141592653589793\n2026-09-06",
        ("define-function",)),
    _ex("name-main", "__name__ == '__main__'", "Modules",
        "This check runs extra code only when the file is launched directly.",
        """def main():
    print("Running as a program")

if __name__ == "__main__":
    main()""",
        "Running as a program",
        ("import-module",)),
    _ex("class-object", "Class and object", "Object-oriented Python",
        "A class is a blueprint. Calling it creates an object.",
        """class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof"

spot = Dog("Spot")
print(spot.bark())""",
        "Spot says woof",
        ("define-function",)),
    _ex("instance-class-vars", "Instance and class variables", "Object-oriented Python",
        "Instance data belongs to one object. Class data is shared.",
        """class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1
        self.id = Counter.total

print(Counter().id, Counter().id, Counter.total)""",
        "1 2 2",
        ("class-object",)),
    _ex("class-static-methods", "Class and static methods", "Object-oriented Python",
        "@classmethod receives the class. @staticmethod needs neither class nor self.",
        """class MathBox:
    @staticmethod
    def double(n):
        return n * 2

    @classmethod
    def name(cls):
        return cls.__name__

print(MathBox.double(4), MathBox.name())""",
        "8 MathBox",
        ("class-object",)),
    _ex("inheritance", "Inheritance", "Object-oriented Python",
        "A child class reuses and extends a parent class.",
        """class Animal:
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "meow"

print(Cat().speak())""",
        "meow",
        ("class-object",)),
    _ex("super-init", "super() and __init__", "Object-oriented Python",
        "super() calls the parent so you can add extra setup.",
        """class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Nia", "A")
print(s.name, s.grade)""",
        "Nia A",
        ("inheritance",)),
    _ex("polymorphism", "Polymorphism", "Object-oriented Python",
        "Different classes can share a method name and be used the same way.",
        """class Square:
    def area(self):
        return 4 * 4

class Circle:
    def area(self):
        return 3.14 * 2 * 2

for shape in (Square(), Circle()):
    print(shape.area())""",
        "16\n12.56",
        ("inheritance",)),
    _ex("encapsulation", "Encapsulation", "Object-oriented Python",
        "A leading underscore marks helper data. Properties control access.",
        """class Bank:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

account = Bank()
account.deposit(50)
print(account.balance)""",
        "50",
        ("class-object",)),
    _ex("magic-methods", "Magic methods", "Object-oriented Python",
        "Names like __str__ and __add__ hook into Python syntax.",
        """class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

print(Point(1, 2) + Point(3, 4))""",
        "(4, 6)",
        ("class-object",)),
    _ex("iterator", "Custom iterator", "Advanced Python",
        "An iterator implements __iter__ and __next__.",
        """class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print(list(CountDown(3)))""",
        "[3, 2, 1]",
        ("class-object",)),
    _ex("generator", "Generators and yield", "Advanced Python",
        "yield pauses a function and sends one value at a time.",
        """def squares(n):
    for i in range(n):
        yield i * i

print(list(squares(5)))""",
        "[0, 1, 4, 9, 16]",
        ("define-function",)),
    _ex("decorator", "Decorators", "Advanced Python",
        "A decorator wraps a function to add behavior.",
        """def loud(fn):
    def wrapper(*args):
        result = fn(*args)
        print("called", fn.__name__)
        return result
    return wrapper

@loud
def add(a, b):
    return a + b

print(add(2, 3))""",
        "called add\n5",
        ("define-function",)),
    _ex("closure", "Closures", "Advanced Python",
        "An inner function can remember values from the outer function.",
        """def make_adder(n):
    def add(x):
        return x + n
    return add

plus_five = make_adder(5)
print(plus_five(10))""",
        "15",
        ("define-function",)),
    _ex("context-manager", "Context managers", "Advanced Python",
        "with runs setup and cleanup. You can write your own with __enter__ / __exit__.",
        """class Tag:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"<{self.name}>")
        return self

    def __exit__(self, *args):
        print(f"</{self.name}>")

with Tag("p"):
    print("hello")""",
        "<p>\nhello\n</p>",
        ("class-object",)),
    _ex("dataclass", "Dataclasses", "Advanced Python",
        "@dataclass writes __init__ and other helpers for you.",
        """from dataclasses import dataclass

@dataclass
class Book:
    title: str
    pages: int

print(Book("Python", 200))""",
        "Book(title='Python', pages=200)",
        ("class-object",)),
    _ex("type-hints", "Type hints", "Advanced Python",
        "Hints document expected types. They help editors and checkers.",
        """def headline(text: str, width: int = 20) -> str:
    return text.upper().center(width, "-")

print(headline("news"))""",
        "--------NEWS--------",
        ("define-function",)),
    _ex("enum-example", "Enumerations", "Advanced Python",
        "Enum names a fixed set of choices.",
        """from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.RED)
print(Color.RED.name, Color.RED.value)""",
        "Color.RED\nRED 1",
        ("class-object",)),
    _ex("regex-basics", "Regular expressions", "Regular expressions",
        "re searches text with patterns.",
        """import re

text = "Call 555-0199 or 123-4567"
print(re.findall(r"\\d{3}-\\d{4}", text))
print(re.sub(r"\\d", "#", "A1B2"))""",
        "['555-0199', '123-4567']\nA#B#",
        ("string-methods",)),
    _ex("regex-groups", "Regex groups", "Regular expressions",
        "Parentheses capture parts of a match.",
        """import re

match = re.search(r"(\\w+)@(\\w+\\.com)", "mail ada@site.com now")
print(match.group(0))
print(match.group(1), match.group(2))""",
        "ada@site.com\nada site.com",
        ("regex-basics",)),
    _ex("stack-queue", "Stack and queue", "Data structures",
        "A list can act as a stack (end) or a simple queue (front).",
        """stack = []
stack.append("a")
stack.append("b")
print("pop", stack.pop())

from collections import deque
queue = deque(["a", "b"])
queue.append("c")
print("left", queue.popleft())""",
        "pop b\nleft a",
        ("create-list",)),
    _ex("binary-search", "Binary search", "Data structures",
        "Binary search finds a value in a sorted list by cutting the range in half.",
        """def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 7))""",
        "3",
        ("while-loop",)),
    _ex("linked-list", "Singly linked list", "Data structures",
        "Each node points to the next node.",
        """class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

head = Node(1, Node(2, Node(3)))
values = []
node = head
while node:
    values.append(node.value)
    node = node.next
print(values)""",
        "[1, 2, 3]",
        ("class-object",)),
    _ex("bubble-sort", "Bubble sort", "Data structures",
        "Neighbor values swap until the list is sorted.",
        """nums = [5, 1, 4, 2]
for i in range(len(nums)):
    for j in range(0, len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)""",
        "[1, 2, 4, 5]",
        ("nested-loops",)),
    _ex("sqlite-crud", "SQLite in memory", "Databases and APIs",
        "sqlite3 can store rows without a separate database server.",
        """import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")
db.execute("INSERT INTO users(name) VALUES (?)", ("Ada",))
row = db.execute("SELECT id, name FROM users").fetchone()
print(row)
db.close()""",
        "(1, 'Ada')",
        ("tuples",)),
    _ex("http-json-idea", "Parse an API-style JSON payload", "Databases and APIs",
        "Web APIs usually send JSON. Parse it, then read fields.",
        """import json

payload = '{"status": 200, "user": {"id": 7, "name": "Ada"}}'
data = json.loads(payload)
if data["status"] == 200:
    print(data["user"]["name"])""",
        "Ada",
        ("json-example",)),
    _ex("flask-route-idea", "Flask route pattern", "Databases and APIs",
        "A Flask view is a function tied to a URL. This shows the pattern without starting a server.",
        """def hello():
    return "Hello from a route"

routes = {"/": hello}
print(routes["/"]())""",
        "Hello from a route",
        ("define-function",),
        "In a real app you would write @app.get('/') above hello."),
    _ex("threading-example", "Threads", "Concurrency",
        "Threads overlap waiting work. A Lock protects shared data.",
        """import threading

total = 0
lock = threading.Lock()

def add():
    global total
    with lock:
        total += 1

jobs = [threading.Thread(target=add) for _ in range(5)]
for job in jobs:
    job.start()
for job in jobs:
    job.join()
print(total)""",
        "5",
        ("define-function",)),
    _ex("asyncio-example", "asyncio coroutines", "Concurrency",
        "async def pauses with await instead of blocking the whole program.",
        """import asyncio

async def work(name):
    await asyncio.sleep(0)
    return f"done {name}"

async def main():
    results = await asyncio.gather(work("a"), work("b"))
    print(", ".join(results))

asyncio.run(main())""",
        "done a, done b",
        ("define-function",)),
    _ex("logging-example", "Logging", "Mastery",
        "logging records what happened without using print for real apps.",
        """import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logging.info("server started")
logging.warning("disk is almost full")""",
        "INFO server started\nWARNING disk is almost full",
        ("define-function",)),
    _ex("pytest-idea", "Test a function", "Mastery",
        "A test is a function that checks a result. pytest would collect this automatically.",
        """def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

test_add()
print("all tests passed")""",
        "all tests passed",
        ("define-function",)),
    _ex("pep8-style", "PEP 8 style sample", "Mastery",
        "Readable names, spaces around operators, and small functions are the core of PEP 8.",
        """MAX_TRIES = 3

def can_retry(attempt):
    return attempt < MAX_TRIES

print(can_retry(1))""",
        "True",
        ("define-function",)),
    _ex("env-vars", "Environment variables", "Mastery",
        "os.environ reads settings without putting secrets in source code.",
        """import os

os.environ["APP_ENV"] = "dev"
print(os.getenv("APP_ENV", "prod"))""",
        "dev",
        ("import-module",)),
    _ex("walrus", "Walrus operator", "Mastery",
        ":= assigns a value while using it in a test.",
        """text = "Python"
if (length := len(text)) > 5:
    print("long", length)""",
        "long 6",
        ("if-statement",)),
    _ex("match-case", "match / case", "Mastery",
        "Structural pattern matching chooses a branch from a shape.",
        """status = 404
match status:
    case 200:
        msg = "ok"
    case 404:
        msg = "not found"
    case _:
        msg = "other"
print(msg)""",
        "not found",
        ("if-elif-else",)),
    _ex("slots-property", "__slots__ for memory", "Mastery",
        "__slots__ lists allowed attributes and can save memory on many objects.",
        """class Pixel:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Pixel(2, 8)
print(p.x, p.y)""",
        "2 8",
        ("class-object",)),
    _ex("generator-expression", "Generator expression", "Advanced Python",
        "Parentheses make a lazy stream instead of a full list.",
        """total = sum(n * n for n in range(5))
print(total)""",
        "30",
        ("generator",)),
    _ex("functools-cache", "functools.cache", "Mastery",
        "cache remembers results so expensive calls are not repeated.",
        """from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))""",
        "55",
        ("recursion",)),
    _ex("pathlib-example", "pathlib paths", "Mastery",
        "pathlib is the modern way to work with file paths.",
        """from pathlib import Path

path = Path("data") / "notes.txt"
print(path.name)
print(path.suffix)
print(path.with_suffix(".md").as_posix())""",
        "notes.txt\n.txt\ndata/notes.md",
        ("import-module",)),
]

BY_SLUG = {item["slug"]: item for item in EXAMPLES}


def grouped_examples():
    groups = OrderedDict()
    for item in EXAMPLES:
        groups.setdefault(item["group"], []).append(item)
    return groups


def get_example(slug):
    return BY_SLUG.get(slug)


def neighbors(slug):
    slugs = [item["slug"] for item in EXAMPLES]
    index = slugs.index(slug)
    previous = EXAMPLES[index - 1] if index else None
    nxt = EXAMPLES[index + 1] if index + 1 < len(slugs) else None
    return previous, nxt


def resolve_prereqs(example):
    found = []
    for slug in example["prereqs"]:
        item = BY_SLUG.get(slug)
        if item:
            found.append(item)
    return found
