#!/usr/bin/env python3
"""Assignment A — Personal Introduction

Fill in your own details below, then run this script.
Your output should be a short paragraph introducing yourself.

Run with:
    python fundamentals/week-02-python-syntax/assignments/assignment_a.py
"""

from datetime import date

# ── Step 1: Fill in your details ──────────────────────────────────────────────
# Replace each placeholder with your own value.
# Pay attention to the type — str uses quotes, int/float do not.

full_name      = "Your Name"        # str  — replace with your name
birthdate      = date(2000, 1, 1)   # date — replace with your own birthdate
height_cm      = 170.0              # float — replace with your height in cm
favourite_food = "pizza"            # str  — replace with your favourite food
has_siblings   = True               # bool — True if you have siblings, False if not


# ── Step 2: Calculate age automatically ───────────────────────────────────────
# You do not need to change anything here — Python works it out from birthdate.
today     = date.today()
age_years = today.year - birthdate.year - (
    (today.month, today.day) < (birthdate.month, birthdate.day)
)


# ── Step 3: Print your introduction ───────────────────────────────────────────
# Write 3 to 5 print() statements that introduce yourself.
# Use f-strings so the variables are embedded naturally in the text.
#
# Example output (yours must use your own variables — do not hard-code values!):
#
#   Hi! My name is Sam. I am 27 years old and 182.5 cm tall.
#   My favourite food is stroopwafel.
#   Do I have siblings? True.
#
# The output must include: full_name, age_years, height_cm,
#                          favourite_food, and has_siblings.

# Write your print() statements below:
