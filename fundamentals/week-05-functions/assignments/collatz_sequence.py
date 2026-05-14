#!/usr/bin/env python3
"""Assignment — Collatz Sequence

Build a tiny program that explores the Collatz sequence.

The rule is simple:
    • if a number is EVEN → next = number // 2
    • if a number is ODD  → next = 3 * number + 1
Repeat until you reach 1. Amazingly, this works for every positive integer
ever tried — mathematicians still don't know why!

Work through the steps one by one. Uncomment each block, run the script,
and check the output before moving on.

Run with:
    python fundamentals/week-05-functions/assignments/collatz_sequence.py
"""


# ── Step 1: Define the collatz() function ────────────────────────────────────
# Write a function called collatz(number) that:
#   - if `number` is even, prints AND returns number // 2
#   - if `number` is odd,  prints AND returns 3 * number + 1
# Hint: a number is even when  number % 2 == 0

# def collatz(number):
#     if number % 2 == 0:
#         result = number // 2
#     else:
#         result = 3 * number + 1
#     print(result)
#     return result


# ── Step 2: Call collatz() a few times by hand ───────────────────────────────
# Try it out: start from 10 and keep feeding the returned value back in until
# you reach 1. Six manual calls should be enough.
#
# Expected printed output:
#     5
#     16
#     8
#     4
#     2
#     1

# n = collatz(10)
# n = collatz(n)
# n = collatz(n)
# n = collatz(n)
# n = collatz(n)
# n = collatz(n)


# ── Step 3: Read the starting number from the user ──────────────────────────
# Ask the user for a starting number with input().
# Convert the answer to an int and store it in `number`.

# raw    = input("Enter a starting number: ")
# number = int(raw)
# print(f"Starting from {number}")


# ── Step 4: Loop until you reach 1 ──────────────────────────────────────────
# Use a while loop to keep calling collatz(number) until number == 1.
# The loop body should reassign `number` to the value returned by collatz().

# while number != 1:
#     number = collatz(number)


# ── Step 5: Input validation with try / except ──────────────────────────────
# If the user types something that isn't a whole number (e.g. "puppy"),
# int() raises a ValueError. Wrap the int() call in a try/except so the
# program prints a friendly message instead of crashing.
#
# This combines with Steps 3 and 4 — replace those blocks with this one:

# raw = input("Enter a starting number: ")
# try:
#     number = int(raw)
# except ValueError:
#     print("That was not a whole number.")
# else:
#     # `else` runs only when the try block did NOT raise — i.e. we got an int.
#     print(f"Starting from {number}")
#     while number != 1:
#         number = collatz(number)


# ── Step 6 (bonus): Reject zero and negative numbers ────────────────────────
# The Collatz rule only behaves nicely for positive integers.
# After Step 5, add a check: if number <= 0, print a warning and skip the loop.

# if number <= 0:
#     print("Please enter a number greater than zero.")
# else:
#     while number != 1:
#         number = collatz(number)
