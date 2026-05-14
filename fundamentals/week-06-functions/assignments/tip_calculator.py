#!/usr/bin/env python3
"""Assignment — Tip Calculator

Build a small bill-splitter using several cooperating FUNCTIONS.
Each step adds one function that uses this week's topics: `def`, parameters,
`return`, default arguments, and scope.

Work through the steps one by one — uncomment each block, run the script,
and check the output before moving on.

Run with:
    python fundamentals/week-06-functions/assignments/tip_calculator.py
"""


# ── Step 1: A function with one parameter and a return ───────────────────────
# Write a function `tip(amount)` that returns 15% of the bill amount.
# Test it by printing the tip on a €40 bill.

# def tip(amount):
#     return amount * 0.15
#
# print(f"15% tip on €40 = €{tip(40):.2f}")


# ── Step 2: Add a default argument ───────────────────────────────────────────
# Rewrite `tip()` so the percentage is a parameter with a DEFAULT of 0.15
# (i.e. 15%). The caller can override it.
# Test with: tip(40), tip(40, 0.20), tip(40, percentage=0.10).

# def tip(amount, percentage=0.15):
#     return amount * percentage
#
# print(f"default tip      → €{tip(40):.2f}")
# print(f"20% tip          → €{tip(40, 0.20):.2f}")
# print(f"10% tip (kwarg)  → €{tip(40, percentage=0.10):.2f}")


# ── Step 3: A second function that uses the first ────────────────────────────
# Write `total_with_tip(amount, percentage=0.15)` that returns the bill PLUS
# the tip. Inside this function, call your `tip()` function — don't re-do the
# multiplication. Functions that call other functions are how programs grow.

# def total_with_tip(amount, percentage=0.15):
#     return amount + tip(amount, percentage)
#
# print(f"€40 + 15% tip = €{total_with_tip(40):.2f}")
# print(f"€40 + 20% tip = €{total_with_tip(40, 0.20):.2f}")


# ── Step 4: Split the bill between several people ────────────────────────────
# Write `split(amount, num_people, percentage=0.15)` that returns how much
# EACH person pays (bill + tip, divided by num_people).
# Reuse `total_with_tip()` instead of repeating the arithmetic.

# def split(amount, num_people, percentage=0.15):
#     return total_with_tip(amount, percentage) / num_people
#
# print(f"€60 between 4 people : €{split(60, 4):.2f} each")
# print(f"€60 between 4, 20%   : €{split(60, 4, 0.20):.2f} each")


# ── Step 5: Print a tidy receipt ─────────────────────────────────────────────
# Write `print_receipt(amount, num_people, percentage=0.15)` that PRINTS
# (and does NOT return) a receipt like:
#
#     Bill         : €60.00
#     Tip (15%)    : €9.00
#     Total        : €69.00
#     Per person   : €17.25  (4 people)
#
# This is a function with side effects — it prints but doesn't return a value
# (so it returns None implicitly — that's fine for a print-only helper).

# def print_receipt(amount, num_people, percentage=0.15):
#     t           = tip(amount, percentage)
#     total       = total_with_tip(amount, percentage)
#     per_person  = split(amount, num_people, percentage)
#     pct_label   = int(percentage * 100)
#     print(f"Bill         : €{amount:.2f}")
#     print(f"Tip ({pct_label}%)    : €{t:.2f}")
#     print(f"Total        : €{total:.2f}")
#     print(f"Per person   : €{per_person:.2f}  ({num_people} people)")
#
# print_receipt(60, 4)
# print_receipt(120, 3, 0.20)


# ── Step 6: Ask the user (no error handling yet) ─────────────────────────────
# Use input() three times to ask for the bill amount, number of people, and
# tip percentage (as a whole number like 15). Convert with float() / int(),
# then call `print_receipt()`.
#
# If the user types something that isn't a number, the program WILL crash.
# That's OK — Week 9 covers try / except.

# raw_amount = input("Bill amount in €: ")
# raw_people = input("How many people are splitting? ")
# raw_pct    = input("Tip percentage (e.g. 15): ")
#
# amount      = float(raw_amount)
# num_people  = int(raw_people)
# percentage  = int(raw_pct) / 100
#
# print_receipt(amount, num_people, percentage)
