#!/usr/bin/env python3
"""Assignment B — Type Conversion Exploration

Explore what happens when you convert between types.
Read each section carefully, run the script, and answer the questions
by writing your explanation as a comment.

Run with:
    python fundamentals/week-02-python-syntax/assignments/assignment_b.py
"""

# ── Part 1: Successful conversions ────────────────────────────────────────────
# Convert each value to the requested type and print the result and its type.
# Example:
#   text = "99"
#   result = int(text)
#   print(f'int("99") = {result}  type: {type(result).__name__}')

text_number  = "42"     # convert this to int, then to float
decimal_text = "3.14"   # convert this to float
whole_float  = 7.0      # convert this to int — what do you notice?

# Write your conversions and print statements here:


# ── Part 2: What happens when it goes wrong? ──────────────────────────────────
# Uncomment the line below and run the script.
# Read the error message carefully.

# result = int("hello world")
# print(result)

# Now answer these questions as comments:
# What type of error do you get?
#   →
#
# In your own words, why does this error happen?
#   →
#
# Can you think of a situation in a real program where this could go wrong?
#   →


# ── Part 3: The truncation trap ───────────────────────────────────────────────
# int() does NOT round — it truncates (drops the decimal part).
# Convert each of the following floats to int and print the result.
# Write a comment next to each one explaining what happened.

a =  3.9   # you might expect 4, but...
b =  3.1
c = -3.9   # this one is surprising — think carefully!

# Write your conversions and comments here:
