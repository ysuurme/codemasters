#!/usr/bin/env python3
"""Week 03 — Lists and Console Input

Run this script to explore Python lists, indexing, slicing, and input().
    python scripts/lists_and_input.py
"""


# ── Data structures: why group data? ─────────────────────────────────────────
# Imagine you are carrying 12 eggs. Without a tray you hold each egg
# separately — 12 things, 12 hands. An egg tray is a DATA STRUCTURE:
# one container that organises related values together.
#
# In Python, the most common data structure is the LIST.
# It solves the exact same problem.
#
# Bad approach — one variable per value:
#   score_day_1 = 85
#   score_day_2 = 92
#   score_day_3 = 78
#   ... (imagine doing this for a full month of daily quiz scores)
#
# Good approach — one list holds all related values:
#   daily_scores = [85, 92, 78, 90, 88, 76, 95]
#
# Lists also let you apply the same operation to every item at once
# (searching, sorting, averaging) — that is why they pair naturally
# with algorithms.


# ── Creating lists ────────────────────────────────────────────────────────────
print("=== Creating lists ===")

# A list is created with square brackets [].
# Elements are separated by commas.

groceries   = ["apples", "milk", "bread", "cheese"]     # list of str
quiz_scores = [85, 92, 78, 90, 88]                      # list of int
prices      = [2.49, 1.89, 3.99, 0.75]                  # list of float
mixed       = ["hello", 42, 3.14, True]                  # mixed types

# A list can contain other lists — useful for grids, tables, egg trays!
egg_tray = [
    [1, 2, 3, 4, 5, 6],    # row 1 — six eggs
    [7, 8, 9, 10, 11, 12], # row 2 — six more eggs
]

# Expressions are evaluated when the list is created:
computed = [1 + 2, "ha" * 3, 10 / 2]

print("groceries  :", groceries)
print("scores     :", quiz_scores)
print("prices     :", prices)
print("mixed      :", mixed)
print("egg_tray   :", egg_tray)
print("computed   :", computed)


# ── Index positions ───────────────────────────────────────────────────────────
# Every element in a list has a fixed POSITION called its INDEX.
#
# Python uses 0-BASED INDEXING — the first element is at index 0.
# Think of the index as the DISTANCE from the start:
#
#   index:    0          1        2         3
#           "apples"  "milk"  "bread"  "cheese"
#
# Why start at 0?  It matches how memory addresses work inside a computer,
# and almost every major language (C, Java, JavaScript, Go) does the same.
# Once you know it, 0-based indexing feels completely natural.

print("\n=== Index positions ===")
groceries = ["apples", "milk", "bread", "cheese"]

print(f"groceries[0]  : {groceries[0]}")   # first element
print(f"groceries[1]  : {groceries[1]}")
print(f"groceries[2]  : {groceries[2]}")
print(f"groceries[3]  : {groceries[3]}")   # last element (len - 1)

# f-strings + index access — combine them freely:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = [12, 14, 11, 9, 13, 15, 10]   # °C, one per day

print(f"\nTemperature on {days[2]}: {temps[2]}°C")
print(f"Temperature on {days[5]}: {temps[5]}°C")

# Negative index — counts from the END of the list.
# -1 is always the last element, no matter how long the list is.
print(f"\ngroceries[-1]  : {groceries[-1]}")   # last
print(f"groceries[-2]  : {groceries[-2]}")   # second to last


# ── Modifying elements ────────────────────────────────────────────────────────
print("\n=== Modifying elements ===")
quiz_scores = [85, 92, 78, 90, 88]
print(f"Before : {quiz_scores}")

quiz_scores[2] = 95   # overwrite element at index 2
print(f"After  : {quiz_scores}  ← index 2 updated from 78 → 95")


# ── Methods ───────────────────────────────────────────────────────────────────
# A METHOD is a function that belongs to a specific type.
# You call it with a dot:  list_name.method_name()
# Think of it as asking the list to do something for itself.
#
# Common list methods:
#   len(lst)            number of elements  (technically a built-in, not a method)
#   lst.append(x)       add x to the end
#   lst.insert(i, x)    insert x at index i, shifting everything else right
#   lst.remove(x)       remove the first occurrence of x
#   sorted(lst)         return a new sorted copy (does not change the original)

print("\n=== Methods ===")
fruits = ["banana", "apple", "cherry"]
print(f"Start           : {fruits}")
print(f"len()           : {len(fruits)}")

fruits.append("mango")
print(f"append('mango') : {fruits}")

fruits.insert(1, "blueberry")
print(f"insert(1, ...)  : {fruits}")

fruits.remove("apple")
print(f"remove('apple') : {fruits}")

print(f"sorted()        : {sorted(fruits)}  ← original unchanged: {fruits}")


# ── Slicing ───────────────────────────────────────────────────────────────────
# [start:end] returns a NEW list from index start up to (NOT including) end.
# Leaving out start means "from the beginning".
# Leaving out end means "to the end".

print("\n=== Slicing ===")
scores = [85, 92, 78, 90, 88, 76, 95]
print(f"Full list : {scores}")
print(f"[1:4]     : {scores[1:4]}")   # indices 1, 2, 3
print(f"[:3]      : {scores[:3]}")    # first 3
print(f"[4:]      : {scores[4:]}")    # from index 4 to end
print(f"[-3:]     : {scores[-3:]}")   # last 3


# ── Strings are sequences too ─────────────────────────────────────────────────
# A string behaves like a list of individual characters.
# You can use index access and slicing on strings exactly like lists.

print("\n=== Strings as sequences ===")
word = "CodeMasters"
print(f"word      : {word}")
print(f"word[0]   : {word[0]}")
print(f"word[-1]  : {word[-1]}")
print(f"word[0:4] : {word[0:4]}")
print(f"word[4:]  : {word[4:]}")
print(f"len(word) : {len(word)}")


# ── Console input ─────────────────────────────────────────────────────────────
# input() pauses the program and waits for the user to type something.
# It ALWAYS returns a string — use int() or float() to convert when needed.

print("\n=== Console input ===")
user_name = input("What is your name? ")
print(f"Hello, {user_name}!")

raw_age  = input("How old are you? ")
user_age = int(raw_age)             # str → int so we can do maths
print(f"Next year you will be {user_age + 1} years old.")

raw_number = input("Enter a number to add to the quiz scores list: ")
quiz_scores.append(int(raw_number))
print(f"Updated scores: {quiz_scores}")
