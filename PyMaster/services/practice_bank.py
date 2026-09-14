"""Coding practice problems from beginner through advanced."""

from collections import OrderedDict


def _p(slug, title, level, topic, prompt, starter, hint, solution, tests):
    return {
        "slug": slug,
        "title": title,
        "level": level,
        "topic": topic,
        "prompt": prompt.strip(),
        "starter": starter.strip("\n"),
        "hint": hint.strip(),
        "solution": solution.strip("\n"),
        "tests": tests.strip("\n"),
    }


PROBLEMS = [
    _p(
        "print-greeting", "Print a greeting", "Beginner", "Output",
        "Print exactly this line:\nHello, Python!",
        "# Print the required text\n",
        "Call print with the exact string Hello, Python!",
        'print("Hello, Python!")',
        '_check_output("Hello, Python!")',
    ),
    _p(
        "add-two-numbers", "Add two numbers", "Beginner", "Variables",
        "Variables a and b are already set. Print their sum.",
        "a = 15\nb = 27\n# Print a + b\n",
        "Use print(a + b).",
        "a = 15\nb = 27\nprint(a + b)",
        '_check_output("42")',
    ),
    _p(
        "even-or-odd", "Even or odd", "Beginner", "Conditions",
        "The variable n is set. Print even if n is divisible by 2, otherwise print odd.",
        "n = 17\n# Print even or odd\n",
        "Use n % 2 == 0.",
        "n = 17\nprint('even' if n % 2 == 0 else 'odd')",
        '_check_output("odd")',
    ),
    _p(
        "largest-of-three", "Largest of three numbers", "Beginner", "Conditions",
        "Print the largest value among a, b, and c.",
        "a, b, c = 9, 21, 14\n# Print the largest\n",
        "You can use max(a, b, c).",
        "a, b, c = 9, 21, 14\nprint(max(a, b, c))",
        '_check_output("21")',
    ),
    _p(
        "multiplication-table", "Multiplication table", "Beginner", "Loops",
        "Print the multiplication table of 7 from 1 to 5. Each line should look like: 7 x 1 = 7",
        "n = 7\n# Print 5 lines\n",
        "Use for i in range(1, 6): and an f-string.",
        "n = 7\nfor i in range(1, 6):\n    print(f'{n} x {i} = {n * i}')",
        '_check_output("7 x 1 = 7\\n7 x 2 = 14\\n7 x 3 = 21\\n7 x 4 = 28\\n7 x 5 = 35")',
    ),
    _p(
        "sum-1-to-n", "Sum from 1 to n", "Beginner", "Loops",
        "n is given. Print the sum of every integer from 1 through n.",
        "n = 10\n# Print 1 + 2 + ... + n\n",
        "range(1, n + 1) or the formula n * (n + 1) // 2.",
        "n = 10\nprint(sum(range(1, n + 1)))",
        '_check_output("55")',
    ),
    _p(
        "count-vowels", "Count vowels", "Beginner", "Strings",
        "Count how many vowels (a, e, i, o, u) are in text. Treat uppercase as lowercase. Print the count.",
        'text = "Education"\n# Print the vowel count\n',
        "Loop through text.lower() and check if the character is in 'aeiou'.",
        'text = "Education"\nprint(sum(1 for ch in text.lower() if ch in "aeiou"))',
        '_check_output("5")',
    ),
    _p(
        "reverse-string", "Reverse a string", "Beginner", "Strings",
        "Print the reverse of word.",
        'word = "Python"\n# Print the reversed word\n',
        "Slicing word[::-1] reverses a string.",
        'word = "Python"\nprint(word[::-1])',
        '_check_output("nohtyP")',
    ),
    _p(
        "list-average", "Average of a list", "Beginner", "Lists",
        "Print the average of nums as a float.",
        "nums = [10, 20, 30, 40]\n# Print the average\n",
        "average is sum(nums) / len(nums).",
        "nums = [10, 20, 30, 40]\nprint(sum(nums) / len(nums))",
        '_check_output("25.0")',
    ),
    _p(
        "fizzbuzz", "FizzBuzz 1 to 15", "Beginner", "Loops",
        "For each number from 1 to 15, print Fizz if divisible by 3, Buzz if divisible by 5, FizzBuzz if both, otherwise the number itself. One value per line.",
        "# Print FizzBuzz lines for 1..15\n",
        "Check 15 first (both), then 3, then 5.",
        """for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)""",
        '_check_output("1\\n2\\nFizz\\n4\\nBuzz\\nFizz\\n7\\n8\\nFizz\\nBuzz\\n11\\nFizz\\n13\\n14\\nFizzBuzz")',
    ),
    _p(
        "factorial-loop", "Factorial with a loop", "Beginner", "Loops",
        "Print n factorial (n!). Do not use math.factorial.",
        "n = 6\n# Print n!\n",
        "Start result at 1, then multiply by each number from 1 to n.",
        "n = 6\nresult = 1\nfor i in range(1, n + 1):\n    result *= i\nprint(result)",
        '_check_output("720")',
    ),
    _p(
        "is-palindrome", "Palindrome word", "Beginner", "Strings",
        "Print True if word is a palindrome (same forwards and backwards), ignoring case. Otherwise print False.",
        'word = "Level"\n# Print True or False\n',
        "Compare word.lower() with its reverse.",
        'word = "Level"\ntext = word.lower()\nprint(text == text[::-1])',
        '_check_output("True")',
    ),
    _p(
        "grade-marks", "Letter grade", "Beginner", "Conditions",
        "Print A if marks >= 90, B if >= 75, C if >= 50, otherwise F.",
        "marks = 81\n# Print the grade\n",
        "Use if / elif / else in that order.",
        """marks = 81
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("F")""",
        '_check_output("B")',
    ),
    _p(
        "remove-duplicates", "Remove duplicates", "Beginner", "Lists",
        "Print a new list from items with duplicates removed, keeping the first occurrence order.",
        "items = [1, 2, 2, 3, 1, 4]\n# Print the unique list\n",
        "Build a result list and only append values that are not already in it.",
        """items = [1, 2, 2, 3, 1, 4]
result = []
for item in items:
    if item not in result:
        result.append(item)
print(result)""",
        '_check_output("[1, 2, 3, 4]")',
    ),
    _p(
        "define-add", "Write an add function", "Intermediate", "Functions",
        "Define a function add(a, b) that returns the sum. Do not print.",
        "def add(a, b):\n    pass\n",
        "Use return a + b.",
        "def add(a, b):\n    return a + b",
        "_check_fn('add', [((2, 3), 5), ((0, 0), 0), ((-4, 10), 6)])",
    ),
    _p(
        "word-count", "Word frequency", "Intermediate", "Dictionaries",
        "Write count_words(text) that returns a dictionary of word -> count. Split on spaces. Ignore case.",
        "def count_words(text):\n    pass\n",
        "text.lower().split() then add 1 for each word in a dict.",
        """def count_words(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts""",
        "_check_fn('count_words', [(('one two one',), {'one': 2, 'two': 1}), (('Hi hi HI',), {'hi': 3})])",
    ),
    _p(
        "second-largest", "Second largest", "Intermediate", "Lists",
        "Write second_largest(nums) that returns the second-largest unique value.",
        "def second_largest(nums):\n    pass\n",
        "Convert to a unique sorted list and take index -2.",
        """def second_largest(nums):
    unique = sorted(set(nums))
    return unique[-2]""",
        "_check_fn('second_largest', [(([4, 1, 7, 7, 3],), 4), (([10, 10, 9],), 9)])",
    ),
    _p(
        "flatten-list", "Flatten a nested list", "Intermediate", "Lists",
        "Write flatten(rows) that turns [[1, 2], [3], [4, 5]] into [1, 2, 3, 4, 5]. Only one level of nesting.",
        "def flatten(rows):\n    pass\n",
        "A double loop, or sum(rows, []).",
        """def flatten(rows):
    result = []
    for row in rows:
        result.extend(row)
    return result""",
        "_check_fn('flatten', [( ([[1, 2], [3], [4, 5]],), [1, 2, 3, 4, 5] ), ( ([],), [] )])",
    ),
    _p(
        "fibonacci", "Nth Fibonacci number", "Intermediate", "Functions",
        "Write fib(n) where fib(0) is 0, fib(1) is 1, and later terms are the sum of the previous two.",
        "def fib(n):\n    pass\n",
        "Keep two running values, or use recursion for small n.",
        """def fib(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b""",
        "_check_fn('fib', [((0,), 0), ((1,), 1), ((7,), 13), ((10,), 55)])",
    ),
    _p(
        "valid-parentheses", "Valid parentheses", "Intermediate", "Stacks",
        "Write is_valid(s) that returns True when every (), [], and {} pair is correctly matched.",
        "def is_valid(s):\n    pass\n",
        "Push opening brackets. When you see a closer, pop and check it matches.",
        """def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack""",
        "_check_fn('is_valid', [(('()[]{}',), True), (('(]',), False), (('({[]})',), True), (('',), True)])",
    ),
    _p(
        "merge-dicts", "Merge dictionaries", "Intermediate", "Dictionaries",
        "Write merge(a, b) that returns a new dict with keys from both. Values from b win when a key repeats.",
        "def merge(a, b):\n    pass\n",
        "{**a, **b} or dict(a) then update(b).",
        "def merge(a, b):\n    return {**a, **b}",
        "_check_fn('merge', [(({'x': 1}, {'x': 2, 'y': 3}), {'x': 2, 'y': 3})])",
    ),
    _p(
        "even-squares", "Even squares", "Intermediate", "Comprehensions",
        "Write even_squares(nums) that returns the squares of even numbers, using a list comprehension.",
        "def even_squares(nums):\n    pass\n",
        "[n * n for n in nums if n % 2 == 0]",
        "def even_squares(nums):\n    return [n * n for n in nums if n % 2 == 0]",
        "_check_fn('even_squares', [(([1, 2, 3, 4, 5],), [4, 16]), (([],), [])])",
    ),
    _p(
        "anagrams", "Are anagrams?", "Intermediate", "Strings",
        "Write are_anagrams(a, b) that returns True if the two words use the same letters (ignore case and spaces).",
        "def are_anagrams(a, b):\n    pass\n",
        "sorted(a.lower().replace(' ', '')) == sorted(b.lower().replace(' ', ''))",
        """def are_anagrams(a, b):
    clean = lambda s: sorted(s.lower().replace(' ', ''))
    return clean(a) == clean(b)""",
        "_check_fn('are_anagrams', [(('listen', 'silent'), True), (('Hello', 'world'), False), (('Dormitory', 'dirty room'), True)])",
    ),
    _p(
        "rectangle-class", "Rectangle class", "Intermediate", "OOP",
        "Create a Rectangle class with width and height. Add area() and perimeter() methods.",
        """class Rectangle:
    def __init__(self, width, height):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass
""",
        "Store width and height on self. Area is width * height. Perimeter is 2 * (width + height).",
        """class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
""",
        """
r = Rectangle(3, 4)
_check('area', r.area(), 12)
_check('perimeter', r.perimeter(), 14)
print('PASS')
""",
    ),
    _p(
        "two-sum", "Two sum indices", "Intermediate", "Algorithms",
        "Write two_sum(nums, target) that returns a tuple of two indices whose values add to target. Return the lowest pair in index order.",
        "def two_sum(nums, target):\n    pass\n",
        "A dict of value -> index lets you look up target - n in O(1).",
        """def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return (seen[need], i)
        seen[n] = i
    return None""",
        "_check_fn('two_sum', [(([2, 7, 11, 15], 9), (0, 1)), (([3, 2, 4], 6), (1, 2))])",
    ),
    _p(
        "recursion-sum", "Recursive list sum", "Intermediate", "Recursion",
        "Write rec_sum(nums) that returns the sum using recursion. Do not use the built-in sum().",
        "def rec_sum(nums):\n    pass\n",
        "Empty list sums to 0. Otherwise return nums[0] + rec_sum(nums[1:]).",
        """def rec_sum(nums):
    if not nums:
        return 0
    return nums[0] + rec_sum(nums[1:])""",
        "_check_fn('rec_sum', [(([1, 2, 3, 4],), 10), (([],), 0)])",
    ),
    _p(
        "call-counter", "Decorator: count calls", "Advanced", "Decorators",
        "Write counted(fn) that returns a wrapper. The wrapper should have a .calls attribute starting at 0 and increasing by 1 each time it is used.",
        """def counted(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
""",
        "Set wrapper.calls = 0, then increment it inside wrapper before calling fn.",
        """def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
""",
        """
@counted
def hello():
    return 'hi'
hello(); hello(); hello()
_check('calls', hello.calls, 3)
_check('result', hello(), 'hi')
_check('calls after extra', hello.calls, 4)
print('PASS')
""",
    ),
    _p(
        "prime-generator", "Prime generator", "Advanced", "Generators",
        "Write primes() that yields prime numbers forever, starting at 2. The tests will take the first 10 values.",
        "def primes():\n    yield 2\n",
        "Try each integer n >= 2 and yield it if no smaller prime divides it.",
        """def primes():
    found = []
    n = 2
    while True:
        if all(n % p for p in found):
            found.append(n)
            yield n
        n += 1
""",
        """
from itertools import islice
got = list(islice(primes(), 10))
_check('first 10 primes', got, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
print('PASS')
""",
    ),
    _p(
        "binary-search", "Binary search", "Advanced", "Algorithms",
        "Write binary_search(items, target) that returns the index of target in a sorted list, or -1 if it is missing. Use binary search, not .index().",
        "def binary_search(items, target):\n    pass\n",
        "Keep low and high indexes. Compare the middle item, then shrink the range.",
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
""",
        "_check_fn('binary_search', [(([1, 3, 5, 7, 9], 7), 3), (([1, 3, 5], 2), -1), (([4], 4), 0)])",
    ),
    _p(
        "group-anagrams", "Group anagrams", "Advanced", "Dictionaries",
        "Write group_anagrams(words) that returns a list of groups. Words in a group are anagrams of each other. Sort letters to make a key. Sort each group, then sort the groups by their first word so the result is stable.",
        "def group_anagrams(words):\n    pass\n",
        "Use ''.join(sorted(word)) as a dictionary key.",
        """def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)
    result = [sorted(group) for group in groups.values()]
    return sorted(result, key=lambda g: g[0])
""",
        "_check_fn('group_anagrams', [((['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],), [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']])])",
    ),
    _p(
        "context-timer", "Context manager", "Advanced", "OOP",
        "Write a class Tag that works with `with Tag('p'):`. On enter print <p>. On exit print </p>.",
        """class Tag:
    def __init__(self, name):
        self.name = name
""",
        "Implement __enter__ and __exit__. __enter__ should return self.",
        """class Tag:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'<{self.name}>')
        return self

    def __exit__(self, *args):
        print(f'</{self.name}>')
""",
        """
import io, sys
_buf = io.StringIO()
_real = sys.stdout
sys.stdout = _buf
with Tag('p'):
    print('hello')
sys.stdout = _real
_check('tag output', _buf.getvalue().replace('\\r\\n', '\\n').strip(), '<p>\\nhello\\n</p>')
print('PASS')
""",
    ),
    _p(
        "memo-fib", "Memoized Fibonacci", "Advanced", "Recursion",
        "Write fib(n) with recursion and a cache (dict or functools.cache) so fib(20) is fast.",
        "def fib(n):\n    pass\n",
        "Store answers in a dict, or decorate with functools.cache.",
        """from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
""",
        "_check_fn('fib', [((0,), 0), ((10,), 55), ((20,), 6765)])",
    ),
    _p(
        "transpose", "Transpose a matrix", "Advanced", "Lists",
        "Write transpose(matrix) that flips rows and columns. matrix is a list of equal-length lists.",
        "def transpose(matrix):\n    pass\n",
        "list(map(list, zip(*matrix)))",
        """def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
""",
        "_check_fn('transpose', [( ([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]] )])",
    ),
    _p(
        "unique-paths", "Grid unique paths", "Advanced", "Algorithms",
        "A robot starts at the top-left of an m by n grid and can only move right or down. Write unique_paths(m, n) that returns how many ways it can reach the bottom-right.",
        "def unique_paths(m, n):\n    pass\n",
        "This is combinatorics, or dynamic programming: dp[i][j] = dp[i-1][j] + dp[i][j-1].",
        """def unique_paths(m, n):
    row = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]
""",
        "_check_fn('unique_paths', [((3, 7), 28), ((3, 2), 3), ((1, 1), 1)])",
    ),
    _p(
        "lru-get", "Tiny LRU cache", "Advanced", "Data structures",
        "Implement class LRUCache(capacity) with get(key) and put(key, value). get returns -1 if missing. When full, put should drop the least recently used key. Both get and put count as use.",
        """class LRUCache:
    def __init__(self, capacity):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass
""",
        "collections.OrderedDict works well: move_to_end on use, popitem(last=False) to drop the oldest.",
        """from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.cap:
            self.data.popitem(last=False)
""",
        """
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
_check('get 1', cache.get(1), 1)
cache.put(3, 3)
_check('evicted 2', cache.get(2), -1)
cache.put(4, 4)
_check('evicted 1', cache.get(1), -1)
_check('get 3', cache.get(3), 3)
_check('get 4', cache.get(4), 4)
print('PASS')
""",
    ),
]

BY_SLUG = {item["slug"]: item for item in PROBLEMS}

HELPER = r'''
def _check(label, got, expected):
    if got != expected:
        print(f"FAIL {label}: got {got!r}, expected {expected!r}")
        raise SystemExit
    return True

def _check_fn(name, cases):
    fn = globals().get(name)
    if fn is None:
        print(f"FAIL: define {name} first")
        raise SystemExit
    for args, expected in cases:
        got = fn(*args)
        if got != expected:
            print(f"FAIL {name}{args}: got {got!r}, expected {expected!r}")
            raise SystemExit
    print("PASS")

def _check_output(expected):
    got = _USER_OUTPUT.replace("\r\n", "\n").strip()
    exp = expected.replace("\r\n", "\n").strip()
    if got != exp:
        print(f"FAIL output:\n got {got!r}\n expected {exp!r}")
        raise SystemExit
    print("PASS")
'''


def grouped_problems():
    groups = OrderedDict()
    for item in PROBLEMS:
        groups.setdefault(item["level"], []).append(item)
    return groups


def get_problem(slug):
    return BY_SLUG.get(slug)


def neighbors(slug):
    slugs = [item["slug"] for item in PROBLEMS]
    index = slugs.index(slug)
    previous = PROBLEMS[index - 1] if index else None
    nxt = PROBLEMS[index + 1] if index + 1 < len(slugs) else None
    return previous, nxt
