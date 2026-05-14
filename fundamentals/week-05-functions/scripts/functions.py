#!/usr/bin/env python3
"""Week 05 — Functions

Run this script to learn how to define your own functions: parameters,
return values, None, keyword arguments, scope, and try/except.

The capstone is a small Guess-the-number game that uses input().
Run it in a TERMINAL (not the Marimo notebook) so you can actually type:

    python fundamentals/week-05-functions/scripts/functions.py
"""

import random


# ── What is a function? ──────────────────────────────────────────────────────
# A FUNCTION is a mini-program inside a program: a named block of code that
# you can run (CALL) whenever you need it.
#
# You already used built-in functions like print(), input(), len().
# This week you write your OWN.
#
# Defining a function does NOT run it — it just teaches Python the recipe.
# Calling a function (with parentheses) is what actually runs it.


# ── Defining and calling — your first function ───────────────────────────────
print("=== Defining and calling ===")

def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")

hello()      # first call — runs the three prints above
hello()      # second call — runs them again


# ── Why functions? Avoiding duplication (DRY) ────────────────────────────────
# Without the function above, you would have to repeat those three prints
# every time. Programmers call this DRY: Don't Repeat Yourself.
#
# Benefits:
#   • shorter code, easier to read
#   • fix a bug ONCE, in one place
#   • re-use the same logic from many spots


# ── Parameters and arguments ─────────────────────────────────────────────────
# A PARAMETER is a variable that lives inside the function and receives a
# value when the function is called. The value you pass in is the ARGUMENT.
#
#   parameter → the name in the def line:           def hello(name):
#   argument  → the value you pass in the call:     hello("Alice")

print("\n=== Parameters ===")

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Yanni")

# Multiple parameters — separate them with commas:
def greet_with_age(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet_with_age("Iris", 19)


# ── Return values ────────────────────────────────────────────────────────────
# Most useful functions GIVE BACK a value. Use the `return` keyword to send
# a value back to the place that called the function.
#
#   • The call evaluates to the returned value, just like 5 + 3 evaluates to 8.
#   • Code after `return` does NOT run — `return` ends the function.

print("\n=== Return values ===")

def add(a, b):
    return a + b

total = add(3, 5)
print(f"add(3, 5)         = {total}")
print(f"add(10, 20) * 2   = {add(10, 20) * 2}")    # use the return inline


# A bigger example — Magic 8-Ball with nine possible fortunes.
def get_answer(answer_number):
    if answer_number == 1:
        return "It is certain"
    elif answer_number == 2:
        return "It is decidedly so"
    elif answer_number == 3:
        return "Yes"
    elif answer_number == 4:
        return "Reply hazy, try again"
    elif answer_number == 5:
        return "Ask again later"
    elif answer_number == 6:
        return "Concentrate and ask again"
    elif answer_number == 7:
        return "My reply is no"
    elif answer_number == 8:
        return "Outlook not so good"
    elif answer_number == 9:
        return "Very doubtful"

r = random.randint(1, 9)
fortune = get_answer(r)
print(f"Magic 8-Ball ({r}) → {fortune}")


# ── None — the value that means "no value" ───────────────────────────────────
# Python has a special value called None to represent "nothing here yet".
# Other languages call this null, nil, or undefined. Always capital N.
#
# A function with no `return` line silently returns None.
# print() itself returns None — it only DISPLAYS text.

print("\n=== None ===")

def shout(text):
    print(text.upper() + "!")        # prints, but does not return anything

result = shout("hello")
print(f"result       = {result}")
print(f"type(result) = {type(result).__name__}")


# ── Keyword arguments — end and sep on print() ───────────────────────────────
# Most arguments are passed by POSITION. Some functions accept extra,
# optional arguments by NAME. These are called KEYWORD ARGUMENTS.
#
# Two handy ones on print():
#   end="..."  → what to print AFTER the values (default: "\n")
#   sep="..."  → what to put BETWEEN the values (default: " ")

print("\n=== Keyword arguments ===")

print("Hello", end="")               # no newline at the end
print("World")                       # → HelloWorld

print("cats", "dogs", "mice")             # cats dogs mice (default sep=" ")
print("cats", "dogs", "mice", sep=", ")   # cats, dogs, mice
print("2026", "05", "14", sep="-")        # 2026-05-14


# ── Local vs global scope ────────────────────────────────────────────────────
# A SCOPE is a container for variables.
#   • Variables defined OUTSIDE any function → GLOBAL scope (one per program).
#   • Variables defined INSIDE a function    → LOCAL scope of that function.
#
# Rules:
#   1. Code inside a function CAN read global variables.
#   2. Code outside a function CANNOT read a function's local variables.
#   3. Each function call has its OWN local scope — gone when the function ends.
#   4. Using the same name in different scopes works, but is confusing.

print("\n=== Scope ===")

shop_name = "CodeMasters Café"           # GLOBAL — visible everywhere

def show_receipt(item, price):
    tax = price * 0.21                   # LOCAL — only exists inside this function
    total = price + tax
    print(f"{shop_name}: {item} — €{total:.2f} (incl. 21% tax)")

show_receipt("coffee", 3.00)
show_receipt("sandwich", 6.50)

# Trying to use `tax` here would crash — it doesn't exist outside the function.
# print(tax)   ← would raise NameError: name 'tax' is not defined


# ── The global statement ─────────────────────────────────────────────────────
# Normally, assigning to a name INSIDE a function creates a LOCAL variable —
# even if a global with the same name already exists. The `global` keyword
# tells Python "no, use the global one".
#
# Use `global` sparingly. Most of the time it's cleaner to take an argument
# and return a value, like add() did above.

print("\n=== The global statement ===")

counter = 0

def increment_counter():
    global counter                       # use the global `counter`, don't shadow it
    counter = counter + 1

increment_counter()
increment_counter()
increment_counter()
print(f"counter after 3 calls : {counter}")


# ── try / except — handling errors without crashing ──────────────────────────
# When something goes wrong (dividing by zero, converting "abc" to int, …)
# Python normally STOPS the program with an error.
#
# Wrap risky code in `try:` and react to specific errors in `except`.
# The program keeps running — much friendlier for the user.

print("\n=== try / except ===")

def safe_divide(top, bottom):
    try:
        return top / bottom
    except ZeroDivisionError:
        return "cannot divide by zero"

print(f"42 / 2 = {safe_divide(42, 2)}")
print(f"42 / 0 = {safe_divide(42, 0)}")
print(f"42 / 7 = {safe_divide(42, 7)}")

# Another common one: int() crashes on non-numeric text.
raw = "42 bananas"
try:
    number = int(raw)
    print(f"converted : {number}")
except ValueError:
    print(f"'{raw}' is not a whole number — using 0 instead")


# ── Putting it together — Guess the number ──────────────────────────────────
# The computer picks a number 1–20; you have 6 tries. Each guess is too
# high / too low / correct. We use functions, return values, scope, and
# try/except all in one tiny game.

print("\n=== Guess the number ===")

MAX_GUESSES = 6
LOW         = 1
HIGH        = 20

def ask_for_guess():
    """Ask the player for a whole number, re-asking on bad input."""
    while True:
        raw = input(f"Take a guess ({LOW}-{HIGH}): ")
        try:
            return int(raw)
        except ValueError:
            print(f"  '{raw}' is not a whole number — try again.")

def play_guessing_game():
    secret = random.randint(LOW, HIGH)
    print(f"I am thinking of a number between {LOW} and {HIGH}.")

    for guesses_taken in range(1, MAX_GUESSES + 1):
        guess = ask_for_guess()
        if guess < secret:
            print("  Too low.")
        elif guess > secret:
            print("  Too high.")
        else:
            print(f"Got it! You guessed it in {guesses_taken} tries.")
            return
    print(f"Out of tries — the number was {secret}.")

play_guessing_game()
