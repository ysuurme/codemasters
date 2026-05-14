#!/usr/bin/env python3
"""Week 07 — Dictionaries

Run this script to learn Python's most flexible data structure: the
DICTIONARY — a collection of KEY → VALUE pairs.

    python fundamentals/week-07-dictionaries/scripts/dictionaries.py
"""


# ── Why dictionaries? ────────────────────────────────────────────────────────
# A LIST stores values in order, looked up by POSITION:
#     prices = [2.49, 0.99, 1.89]
#     prices[0]   →  2.49
#
# But position numbers are not very meaningful — what does position 0 mean?
# A DICTIONARY stores values looked up by a LABEL of your choice (the KEY):
#     prices = {"apples": 2.49, "milk": 0.99, "bread": 1.89}
#     prices["apples"]   →  2.49
#
# Use a dict when each value has a label — names paired with ages,
# products paired with prices, settings paired with their value, …


# ── Creating a dictionary ────────────────────────────────────────────────────
# Dictionaries use CURLY BRACES and key: value pairs separated by commas.
# Keys are usually strings; values can be any type (numbers, strings, lists,
# even other dictionaries).

print("=== Creating a dictionary ===")

teacher = {
    "name": "Marijn",
    "age": 48,
    "city": "Eindhoven",
}

print(f"teacher           : {teacher}")
print(f"len(teacher)      : {len(teacher)}")        # number of pairs
print(f"type(teacher)     : {type(teacher).__name__}")


# ── Reading a value by its key ───────────────────────────────────────────────
# Use SQUARE BRACKETS with the key inside, just like list indexing — but
# with a label instead of a position.

print("\n=== Reading values ===")

print(f"teacher['name']   : {teacher['name']}")
print(f"teacher['age']    : {teacher['age']}")
print(f"teacher['city']   : {teacher['city']}")

# What if the key does not exist? Bracket access CRASHES with KeyError.
# Use the safer `.get()` method to get a default value instead:

print(f".get('name')      : {teacher.get('name')}")
print(f".get('country')   : {teacher.get('country')}")              # None
print(f".get('country',?) : {teacher.get('country', 'unknown')}")   # default


# ── Adding, updating, and removing keys ──────────────────────────────────────
# Dictionaries are MUTABLE — you can change them after creation.

print("\n=== Modifying a dictionary ===")

teacher["job"] = "Engineer"     # adds a NEW key
print(f"after add 'job'   : {teacher}")

teacher["age"] = 49             # OVERWRITES an existing key
print(f"after update age  : {teacher}")

del teacher["city"]             # REMOVES a key
print(f"after delete city : {teacher}")


# ── Checking whether a key exists ────────────────────────────────────────────
# Use the `in` keyword — same as with lists.

print("\n=== Membership ===")

if "name" in teacher:
    print("'name' is a key in teacher")
if "city" not in teacher:
    print("'city' is NOT a key in teacher anymore")


# ── Looping over a dictionary ────────────────────────────────────────────────
# Three handy views, all usable in a `for` loop:
#     teacher          → iterates the KEYS
#     teacher.values() → iterates the VALUES
#     teacher.items()  → iterates (key, value) pairs

print("\n=== Looping — keys only ===")
for key in teacher:
    print(f"  key: {key}")

print("\n=== Looping — values only ===")
for value in teacher.values():
    print(f"  value: {value}")

print("\n=== Looping — key and value together ===")
for key, value in teacher.items():
    print(f"  {key:5} → {value}")


# ── Using a dict as a counter ────────────────────────────────────────────────
# A classic dict pattern — count how often each item appears in a list.

print("\n=== Counting with a dict ===")

words   = ["red", "green", "red", "blue", "green", "red"]
counts  = {}

for w in words:
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1

print(f"words  : {words}")
print(f"counts : {counts}")


# ── Lists of dicts — real-world shaped data ──────────────────────────────────
# Most real-world data — rows in a spreadsheet, results from an API, contacts
# in your phone — is a LIST of DICTS. Each dict is one record; each key is
# one column or field.

print("\n=== List of dicts ===")

students = [
    {"name": "Sam",   "age": 19, "score": 72},
    {"name": "Iris",  "age": 21, "score": 48},
    {"name": "Tom",   "age": 24, "score": 88},
    {"name": "Aysha", "age": 22, "score": 55},
    {"name": "Leo",   "age": 20, "score": 34},
]

# Print each student's name and score:
for s in students:
    print(f"  {s['name']:6} ({s['age']}) → {s['score']}")

# Combine with a counter pattern from Week 5:
passed = 0
for s in students:
    if s["score"] >= 55:
        passed = passed + 1
print(f"\n  passed: {passed} of {len(students)}")


# ── Putting it together — a tiny contacts book ───────────────────────────────
# A dict of contacts (key = name, value = phone number).
# We add, look up, list, and remove — the four things you can ever do to a
# collection of labelled data.

print("\n=== Putting it together — contacts book ===")

contacts = {
    "Alice":  "06-1234-5678",
    "Bob":    "06-9876-5432",
    "Yanni":  "06-1111-2222",
}

# Add
contacts["Marijn"] = "06-3333-4444"

# Look up
who = "Bob"
if who in contacts:
    print(f"  {who}: {contacts[who]}")
else:
    print(f"  {who} is not in your contacts.")

# List all
print("\n  All contacts:")
for name, phone in contacts.items():
    print(f"    {name:8} {phone}")

# Remove
del contacts["Alice"]
print(f"\n  after removing Alice: {len(contacts)} contacts left")
