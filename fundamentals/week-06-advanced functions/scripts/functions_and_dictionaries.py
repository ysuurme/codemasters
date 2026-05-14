#!/usr/bin/env python3
"""Week 06 — Advanced Functions and Dictionaries

Run this script to expand your toolkit with more built-in functions, methods,
higher-order functions (map, filter, lambda), and a new data structure:
the dictionary.

    python "fundamentals/week-06-advanced functions/scripts/functions_and_dictionaries.py"
"""


# ── Built-in functions ────────────────────────────────────────────────────────
# Python ships with many BUILT-IN functions you can use without importing
# anything. You met a few in Week 3 — here is a wider toolbox you will reach
# for over and over again.
#
#   len(x)        number of items in a list, string, or dict
#   sum(x)        total of all numbers in a list
#   min(x)        smallest value
#   max(x)        largest value
#   abs(x)        absolute value — drops the minus sign
#   round(x, n)   round a float to n decimals
#   sorted(x)     a NEW sorted copy of x (does not change the original)
#   type(x)       the type of a value: str, int, float, list, dict, ...
#
# Tip: in VS Code, hover over a built-in to see its short description.

print("=== Built-in functions ===")
numbers = [3, 8, 1, -5, 12, 7]

print(f"numbers         : {numbers}")
print(f"len()           : {len(numbers)}")
print(f"sum()           : {sum(numbers)}")
print(f"min() / max()   : {min(numbers)} / {max(numbers)}")
print(f"abs(-5)         : {abs(-5)}")
print(f"round(3.567, 1) : {round(3.567, 1)}")
print(f"sorted()        : {sorted(numbers)}  ← original unchanged: {numbers}")


# ── Methods — functions that belong to a value ────────────────────────────────
# A METHOD is a function that belongs to a specific type of value.
# You call it with a DOT:  value.method_name()
#
#   built-in function works ON a value:    len(my_list)
#   method is called ON a value:           my_list.append("x")
#
# Different types have different methods. In VS Code, type a dot after a
# variable and the editor will show all available methods — try it!

print("\n=== List methods ===")
fruits = ["banana", "apple", "cherry"]
print(f"start             : {fruits}")

fruits.append("mango")            # add at the end
print(f"after .append     : {fruits}")

fruits.sort()                     # sort the list in place
print(f"after .sort()     : {fruits}")

fruits.reverse()                  # reverse the list in place
print(f"after .reverse()  : {fruits}")

print(f".count('banana')  : {fruits.count('banana')}")


print("\n=== String methods ===")
greeting = "Good Morning, CodeMasters!"
print(f"original          : {greeting}")
print(f".upper()          : {greeting.upper()}")
print(f".lower()          : {greeting.lower()}")
print(f".replace(...)     : {greeting.replace('Morning', 'Evening')}")
print(f".split(', ')      : {greeting.split(', ')}")


# ── map() — apply a function to every item ────────────────────────────────────
# map(function, list) applies the function to every item in the list
# and returns a new sequence. Wrap it in list(...) to see the values.
#
# Think of map() as "do this to each one".

print("\n=== map() ===")

def squared(x):
    return x * x

numbers = [1, 2, 3, 5, 7, 11]
squares = list(map(squared, numbers))
print(f"numbers : {numbers}")
print(f"squared : {squares}")

# map() works with any function — including methods.
# str.upper is the method that uppercases a string.
groceries = ["apples", "milk", "bread"]
shouted   = list(map(str.upper, groceries))
print(f"groceries : {groceries}")
print(f"SHOUTED   : {shouted}")


# ── filter() — keep only the items that match ─────────────────────────────────
# filter(function, list) keeps every item for which the function returns True.
# Think of filter() as "keep only the ones where this is true".

print("\n=== filter() ===")

def is_even(x):
    return x % 2 == 0

numbers      = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(is_even, numbers))
print(f"numbers      : {numbers}")
print(f"even_numbers : {even_numbers}")


# ── lambda — anonymous one-line functions ─────────────────────────────────────
# A LAMBDA is a small function written on a single line, without using `def`.
#
#   syntax:   lambda arguments: expression
#
# A lambda has no name on its own. It is handy when you need a tiny function
# ONCE — typically as the first argument to map(), filter(), or sorted().

print("\n=== lambda ===")

# Same function, two ways:
def double(x):
    return x * 2

double_lam = lambda x: x * 2

print(f"double(5)      : {double(5)}")
print(f"double_lam(5)  : {double_lam(5)}")

# The most common use — pass directly to map() or filter():
numbers = [1, 2, 3, 5, 7, 11]
squares = list(map(lambda x: x ** 2,    numbers))
odd     = list(filter(lambda x: x % 2,  numbers))
print(f"squares : {squares}")
print(f"odd     : {odd}")


# ── Dictionaries — key/value pairs ────────────────────────────────────────────
# A DICTIONARY (dict) stores data as KEY: VALUE pairs.
#
#   list  → indexed by POSITION:   prices[0]
#   dict  → indexed by KEY:        prices["milk"]
#
# Use a dict when each value has a label — names paired with ages,
# products paired with prices, students paired with grades, etc.
#
# Properties:
#   - Created with curly braces:   {"name": "Marijn", "age": 48}
#   - Keys must be UNIQUE within the dict (and usually str, int, or tuple)
#   - Values can be ANY type
#   - Dictionaries are MUTABLE — you can add, change, or remove pairs

print("\n=== Dictionaries — create and read ===")

teacher = {
    "name": "Marijn",
    "age": 48,
    "city": "Eindhoven",
}

print(f"teacher           : {teacher}")
print(f"teacher['name']   : {teacher['name']}")    # access a value by its key
print(f"teacher['age']    : {teacher['age']}")
print(f"len(teacher)      : {len(teacher)}")        # number of pairs


# ── Adding, updating, and removing keys ───────────────────────────────────────
print("\n=== Dictionaries — modify ===")

teacher["job"] = "Engineer"   # adds a NEW key
teacher["age"] = 49           # OVERWRITES an existing key
del teacher["city"]           # REMOVES a key

print(f"after changes     : {teacher}")


# ── Iterating with .items() ───────────────────────────────────────────────────
# .items() lets a for-loop give you both the key AND the value each step.

print("\n=== Dictionaries — iterate ===")
for key, value in teacher.items():
    print(f"  {key:5} → {value}")


# ── Checking membership with `in` ─────────────────────────────────────────────
print("\n=== Dictionaries — membership ===")
if "name" in teacher:
    print("'name' is a key in teacher")
if "city" not in teacher:
    print("'city' is NOT a key in teacher anymore")


# ── Putting it together — students and grades ─────────────────────────────────
# A dict of student → score combined with map / filter / lambda is a tiny
# but very real program.

print("\n=== Putting it together ===")

grades = {
    "Sam":   72,
    "Iris":  48,
    "Tom":   88,
    "Aysha": 55,
    "Leo":   34,
}

scores = list(grades.values())

# Convert percentages to a Dutch 1–10 grade with a lambda:
to_dutch     = lambda pct: round(pct / 10, 1)
dutch_grades = list(map(to_dutch, scores))

# Which students passed? Dutch grade >= 5.5
passed = list(filter(lambda name: to_dutch(grades[name]) >= 5.5, grades))

print(f"students      : {len(grades)}")
print(f"average       : {sum(scores) / len(grades):.1f}%")
print(f"highest       : {max(scores)}%")
print(f"lowest        : {min(scores)}%")
print(f"dutch grades  : {dutch_grades}")
print(f"passed        : {passed}")
