#!/usr/bin/env python3
"""Week 02 — Python Syntax

Run this script to explore the building blocks of Python.
    python scripts/python_syntax.py
"""

from datetime import date


# ── Comments ──────────────────────────────────────────────────────────────────
# A comment starts with # and is completely ignored by Python.
# Use comments to explain WHY you did something — not what (the code shows that).
# You can also comment at the end of a line, like the examples below.


# ── print() ───────────────────────────────────────────────────────────────────
# print() displays whatever you put inside its brackets on the screen.
# Use it to show results, follow along as a program runs, and debug.

print("=== print() ===")
print("Hello, World!")          # printing text
print(42)                       # printing a whole number
print(3.14)                     # printing a decimal number
print(10 + 5)                   # print can calculate for you
print()                         # empty print() = blank line
print("The answer is", 42)      # comma → Python adds a space between values


# ── \n — multiple lines in one print() ───────────────────────────────────────
print("\n=== \\n newline ===")
print("Line one\nLine two\nLine three")  # \n starts a new line

city    = "Amsterdam"       # str variable — note the snake_case name
country = "The Netherlands" # str variable
print(f"City: {city}\nCountry: {country}")


# ── Variable types ────────────────────────────────────────────────────────────
# A variable is a named box that stores a value.
# Python has four basic types you will use every day:
#
#   str   — text, always wrapped in quotes:     "hello"   'world'
#   int   — a whole number, no decimal point:   42   -7   0
#   float — a decimal number:                   3.14   -0.5   100.0
#   bool  — either True or False, nothing else: True   False
#
# Python figures out the type automatically when you assign a value.
# Use type() to check.

print("\n=== Variable types ===")

name       = "Sam"     # str
age        = 27        # int
height_cm  = 182.5     # float
is_student = True      # bool  ← "is_" prefix is the convention for booleans

print(f"name       = {name!r:<12}  type: {type(name).__name__}")
print(f"age        = {age:<12}  type: {type(age).__name__}")
print(f"height_cm  = {height_cm:<12}  type: {type(height_cm).__name__}")
print(f"is_student = {is_student!r:<12}  type: {type(is_student).__name__}")


# ── Operations on types ───────────────────────────────────────────────────────
# The same operator can do very different things depending on the type.

print("\n=== String operations ===")

first  = "Code"
second = "Masters"

print(first + second)           # + joins strings: "CodeMasters"
print(first + " " + second)     # add a space manually: "Code Masters"
print("ha" * 3)                 # * repeats a string: "hahaha"
print("-" * 30)                 # useful trick for drawing dividers

# Here is the classic beginner surprise:
print()
print("'5' + '3'  =", "5" + "3")   # "53" — strings are JOINED, not added!
print(" 5  +  3   =", 5 + 3)        #  8   — integers are ADDED

# You cannot add a string and an integer — Python will crash with a TypeError:
# print("5" + 3)    ← uncomment to see the error

print("\n=== Number operations ===")

a = 10   # int
b = 3    # int

print(f"{a} +  {b}  = {a + b}")          # addition      → int
print(f"{a} -  {b}  = {a - b}")          # subtraction   → int
print(f"{a} *  {b}  = {a * b}")          # multiplication → int
print(f"{a} /  {b}  = {a / b:.4f}")      # division      → always float!
print(f"{a} // {b}  = {a // b}")         # floor division → rounds down
print(f"{a} %  {b}  = {a % b}")          # remainder (modulo)
print(f"{a} ** {b}  = {a ** b}")         # power: 10³ = 1000

# int + float → Python promotes the result to float automatically:
print()
print(f"5 + 2.0  = {5 + 2.0}   ← int + float = float")
print(f"4 * 0.5  = {4 * 0.5}   ← int * float = float")


# ── Type conversion ───────────────────────────────────────────────────────────
# You can convert between types using int(), float(), str(), and bool().
# This is called type conversion (or "casting").

print("\n=== Type conversion ===")

# Real example: personal savings in EUR.
# You count your savings as a whole number (int), but interest calculations
# need a decimal (float) to be accurate.

savings_eur   = 20             # int — "I have 20 euros saved"
savings_float = float(savings_eur)  # → 20.0

interest_rate   = 0.035        # 3.5% annual interest
interest_earned = savings_float * interest_rate

print(f"Savings         : €{savings_eur}  (type: {type(savings_eur).__name__})")
print(f"Savings as float: €{savings_float}  (type: {type(savings_float).__name__})")
print(f"Interest at 3.5%: €{interest_earned:.4f}")
print(f"Balance after 1y: €{savings_float + interest_earned:.2f}")

# Converting a string that looks like a number — this is very common when
# reading user input, because input() always returns a string.
print()
text_number = "42"                  # looks like a number, but it is a str
as_int      = int(text_number)      # "42" → 42
as_float    = float(text_number)    # "42" → 42.0
back_to_str = str(as_int)          #  42  → "42"

print(f'"42" → int   : {as_int}    type: {type(as_int).__name__}')
print(f'"42" → float : {as_float}  type: {type(as_float).__name__}')
print(f'42   → str   : "{back_to_str}"   type: {type(back_to_str).__name__}')

# Important: int() truncates floats — it does NOT round, it drops the decimal.
print()
print(f"int(3.9) = {int(3.9)}   ← drops the .9, does NOT round up to 4")
print(f"int(3.1) = {int(3.1)}   ← same behaviour")

# What if you try to convert something that cannot be converted?
# int("hello") would crash with a ValueError.
# int("hello")  ← uncomment to see the error


# ── f-strings ─────────────────────────────────────────────────────────────────
# f-strings are the cleanest way to mix text and values.
# Put f before the opening quote and wrap variables or expressions in {}.

print("\n=== f-strings ===")

product = "laptop"
price   = 999.00
stock   = 14

print(f"Product : {product}")
print(f"Price   : €{price:.2f}")
print(f"In stock: {stock} units")
print(f"Total value: €{price * stock:,.2f}")  # :, adds thousands separator


# ── Naming conventions ────────────────────────────────────────────────────────
# Python follows PEP 8 — the official style guide:
#
#   snake_case        — variables and functions:  user_age   full_name
#   UPPER_SNAKE_CASE  — constants (never change): MAX_SPEED  TAX_RATE
#   PascalCase        — class names (Week 8):     UserProfile
#
#   ✓ full_name       clear, descriptive, snake_case
#   ✓ is_active       bool variables often start with "is_" or "has_"
#   ✓ TAX_RATE        constant — UPPER_SNAKE_CASE
#   ✗ a  x  tmp       too short or vague
#   ✗ fullName        camelCase — common in JavaScript, not Python


# ── A realistic example — personal profile ────────────────────────────────────
print("\n=== Personal profile ===")

full_name       = "Sam de Vries"      # str
birthdate       = date(1998, 6, 15)   # ← change to your own!
height_cm       = 182.5               # float
weight_kg       = 78.0                # float
favourite_food  = "stroopwafel"       # str
has_siblings    = True                # bool

today     = date.today()
age_years = today.year - birthdate.year - (
    (today.month, today.day) < (birthdate.month, birthdate.day)
)

print(
    f"Name     : {full_name}\n"
    f"Age      : {age_years} years  (born {birthdate})\n"
    f"Height   : {height_cm} cm\n"
    f"Weight   : {weight_kg} kg\n"
    f"Food     : {favourite_food}\n"
    f"Siblings : {has_siblings}"
)


# ── Debugging with print() ────────────────────────────────────────────────────
print("\n=== Debugging with print() ===")
# When something goes wrong, print() is the fastest way to inspect a value.

total_price     = 100       # int
discount_pct    = 0.15      # float — 15%
discount_amount = total_price * discount_pct
final_price     = total_price - discount_amount

print(f"total_price     = {total_price}")
print(f"discount_pct    = {discount_pct}")
print(f"discount_amount = {discount_amount}")
print(f"final_price     = {final_price}")
