#!/usr/bin/env python3
"""Week 04 — Conditionals and Control Flow

Run this script to learn how programs make decisions and repeat work:
boolean values, comparisons, if/elif/else, while/break/continue, and for/range.

    python fundamentals/week-04-conditionals-and-control-flow/scripts/conditionals_and_control_flow.py
"""


# ── Why flow control? ─────────────────────────────────────────────────────────
# Up to now your programs ran top-to-bottom, one line after another.
# Real programs DECIDE what to do (if/else), and REPEAT work (loops).
# Together these are called FLOW CONTROL — they change the path through the code.


# ── Boolean values ───────────────────────────────────────────────────────────
# The bool type has only TWO possible values: True and False.
# Both start with a capital letter — `true` (lowercase) is a NameError.
# Booleans are how Python answers a yes/no question.

print("=== Boolean values ===")

is_raining     = True
is_sunny       = False
has_umbrella   = True

print(f"is_raining    = {is_raining}    type: {type(is_raining).__name__}")
print(f"is_sunny      = {is_sunny}")
print(f"has_umbrella  = {has_umbrella}")


# ── Comparison operators ─────────────────────────────────────────────────────
# A comparison compares TWO values and evaluates to True or False.
#
#   ==   equal to            !=   not equal to
#   <    less than           >    greater than
#   <=   less than or equal  >=   greater than or equal
#
# Watch out: `==` is the comparison; `=` is assignment.
#   age == 18   →  asks "is age the same as 18?"
#   age =  18   →  stores 18 in age

print("\n=== Comparison operators ===")

age          = 19
voting_age   = 18

print(f"age == voting_age  → {age == voting_age}")
print(f"age != voting_age  → {age != voting_age}")
print(f"age >= voting_age  → {age >= voting_age}")
print(f"age <  voting_age  → {age <  voting_age}")

# Strings compare by content (and are case-sensitive):
print(f"'cat' == 'cat'     → {'cat' == 'cat'}")
print(f"'cat' == 'Cat'     → {'cat' == 'Cat'}")


# ── Boolean operators (and / or / not) ───────────────────────────────────────
# Combine boolean values with `and`, `or`, `not`.
#
#   and  → True only if BOTH sides are True
#   or   → True if EITHER side is True
#   not  → flips True ↔ False
#
# Truth tables:
#
#     A     B     A and B   A or B
#   True   True    True      True
#   True   False   False     True
#   False  True    False     True
#   False  False   False     False
#
#     A     not A
#   True   False
#   False  True

print("\n=== Boolean operators ===")

print(f"True  and True   → {True  and True}")
print(f"True  and False  → {True  and False}")
print(f"True  or  False  → {True  or  False}")
print(f"False or  False  → {False or  False}")
print(f"not True         → {not True}")


# ── Mixing comparisons and boolean operators ─────────────────────────────────
# Each comparison evaluates to a boolean, so you can chain them with and/or/not.

print("\n=== Mixing comparisons ===")

temp_c = 12     # °C outside

# Should I take a jacket? Cold OR raining.
take_jacket = temp_c < 15 or is_raining
print(f"take_jacket = {take_jacket}")

# Can I go for a sunny picnic? Sunny AND warm AND no rain.
picnic_ok = is_sunny and temp_c >= 20 and not is_raining
print(f"picnic_ok   = {picnic_ok}")

# Python supports the math-style chain  low < x < high :
score = 73
in_b_range = 60 <= score < 80
print(f"in_b_range  = {in_b_range}    (score = {score})")


# ── if / else / elif ─────────────────────────────────────────────────────────
# An `if` statement runs a block of code ONLY when its condition is True.
#
#   if condition:        ← ends with a colon
#       do_something()   ← indented block — this is the CLAUSE
#
# Indentation is how Python knows which lines belong to the if.
# Four spaces is the convention.
#
# Add `else` for the "otherwise" case, and `elif` for more options.

print("\n=== if / else ===")

age = 17
if age >= 18:
    print(f"At {age} you can vote in the Netherlands.")
else:
    print(f"At {age} you need to wait {18 - age} more years to vote.")


print("\n=== if / elif / else ===")

# An umbrella-policy assistant — multi-way decision.
temp_c       = 8
is_raining   = True

if is_raining and temp_c < 10:
    print("Cold and wet — coat AND umbrella.")
elif is_raining:
    print("Just rain — grab an umbrella.")
elif temp_c < 10:
    print("Cold but dry — wear a coat.")
elif temp_c >= 25:
    print("Hot! Sunglasses recommended.")
else:
    print("Nothing special needed today.")


# ── Order matters in elif chains ─────────────────────────────────────────────
# Python checks each branch top-to-bottom and runs the FIRST one that is True.
# All later branches are skipped — even if they would also match.

print("\n=== Order of elif matters ===")

age = 3000   # very long-lived person

# CORRECT — most specific first:
if age > 2000:
    label = "ancient"
elif age > 100:
    label = "very old"
elif age >= 18:
    label = "adult"
else:
    label = "minor"
print(f"correct order  → {label}")

# WRONG — `> 100` matches first, so we'll never reach `> 2000`:
if age > 100:
    label = "very old"
elif age > 2000:
    label = "ancient"
else:
    label = "young"
print(f"wrong order    → {label}     ← bug: 3000 is also > 100!")


# ── Truthy and falsy values ──────────────────────────────────────────────────
# In a condition, some non-boolean values are treated as True or False.
# FALSY: 0, 0.0, "" (empty string), [] (empty list), None
# Everything else is truthy.
# This lets you write tidy checks like  `if name:`  instead of  `if name != "":`.

print("\n=== Truthy and falsy ===")

name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("(no name yet)")

groceries = ["bread", "milk"]
if groceries:
    print(f"Shopping list has {len(groceries)} items.")


# ── while loops — repeat until the condition becomes False ───────────────────
# A `while` loop checks its condition BEFORE every iteration.
# As long as the condition is True, the indented block runs again.
#
#   while condition:
#       do_something()
#
# Make sure something inside the loop eventually changes the condition,
# otherwise you create an INFINITE LOOP (press Ctrl+C in the terminal to stop).

print("\n=== while loop ===")

count_down = 5
while count_down > 0:
    print(f"  T-minus {count_down} ...")
    count_down = count_down - 1
print("  Lift off!")


# ── break — leave a loop early ───────────────────────────────────────────────
# `break` jumps out of the loop immediately.
# Combined with `while True:` it gives you a "loop forever until I say stop" pattern.

print("\n=== break ===")

allowed_attempts = 3
correct_pin      = "1234"
demo_inputs      = ["0000", "1111", "1234"]   # pretending the user types these

attempt = 0
while True:
    pin = demo_inputs[attempt]      # in a real program: pin = input("PIN: ")
    print(f"  attempt {attempt + 1}: typed '{pin}'")
    if pin == correct_pin:
        print("  ✓ correct PIN — unlocked")
        break
    attempt = attempt + 1
    if attempt >= allowed_attempts:
        print("  ✗ too many tries — locked")
        break


# ── continue — skip the rest of THIS iteration ───────────────────────────────
# `continue` jumps back to the top of the loop, skipping the remaining lines
# of the current iteration. Use it to "skip" over items you don't want to handle.

print("\n=== continue ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for n in numbers:
    if n % 2 == 1:        # odd → skip
        continue
    print(f"  even number: {n}")


# ── for loops with range() ───────────────────────────────────────────────────
# Use a `for` loop when you know HOW MANY times to repeat.
#
#   range(stop)              0, 1, 2, ..., stop-1
#   range(start, stop)       start, start+1, ..., stop-1
#   range(start, stop, step) start, start+step, ... (up to but not including stop)
#
# The variable after `for` (here `i`) takes each value in turn.

print("\n=== for + range() ===")

for i in range(5):
    print(f"  i = {i}")

print("  ---")

for i in range(2, 6):           # 2, 3, 4, 5
    print(f"  i = {i}")

print("  ---")

for i in range(0, 20, 5):       # 0, 5, 10, 15
    print(f"  i = {i}")

print("  ---")

# range() also runs backwards with a negative step:
for i in range(5, 0, -1):       # 5, 4, 3, 2, 1
    print(f"  count = {i}")


# ── Putting it together — what should I wear today? ──────────────────────────
# A tiny decision tree using nearly every feature from this week.
# We loop over a forecast for the week and print a clothing tip per day.

print("\n=== Putting it together — weekly outfit advice ===")

forecast = [
    ("Mon",  6, True),     # day, °C, raining?
    ("Tue", 14, False),
    ("Wed",  9, True),
    ("Thu", 22, False),
    ("Fri", 28, False),
    ("Sat", 18, True),
    ("Sun", 12, False),
]

for day, temp_c, raining in forecast:
    if temp_c >= 25:
        tip = "T-shirt + sunscreen"
    elif temp_c >= 15 and not raining:
        tip = "Light jacket"
    elif raining and temp_c < 15:
        tip = "Coat + umbrella"
    elif raining:
        tip = "Umbrella"
    else:
        tip = "Warm sweater"
    print(f"  {day}: {temp_c:>2}°C, rain={raining!s:<5} → {tip}")
