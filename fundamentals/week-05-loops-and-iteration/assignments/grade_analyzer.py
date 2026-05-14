#!/usr/bin/env python3
"""Assignment — Grade Analyzer

Build a small program that analyses a list of student scores using
`for` loops. Each step practises one of the loop patterns from this week.

Work through the steps one by one — uncomment each block, run the script,
and check the output before moving on.

Run with:
    python fundamentals/week-05-loops-and-iteration/assignments/grade_analyzer.py
"""


# A list of student scores out of 100. Use this in every step below.
scores = [72, 48, 88, 55, 34, 91, 67, 80, 22, 76]


# ── Step 1: Print every score on its own line ────────────────────────────────
# Use a `for` loop to walk `scores` and print each one with a "  - " prefix.

# for s in scores:
#     print(f"  - {s}")


# ── Step 2: Count how many students passed ───────────────────────────────────
# A passing score is 55 or higher.
# Use a counter variable that starts at 0 and increases by 1 each time you
# see a passing score. Print the final count.

# passed = 0
# for s in scores:
#     if s >= 55:
#         passed = passed + 1
# print(f"{passed} of {len(scores)} students passed")


# ── Step 3: Compute the average by hand ──────────────────────────────────────
# Sum the scores with a `total = 0` variable and a `for` loop, then divide
# by `len(scores)`. Print the average rounded to 1 decimal.

# total = 0
# for s in scores:
#     total = total + s
# average = total / len(scores)
# print(f"average: {average:.1f}")


# ── Step 4: Build a list of pass / fail labels ───────────────────────────────
# Start with an empty list `labels = []`.
# Walk `scores` with a `for` loop. For each score, append "pass" if it is
# 55 or higher, otherwise "fail". Print the final list.

# labels = []
# for s in scores:
#     if s >= 55:
#         labels.append("pass")
#     else:
#         labels.append("fail")
# print(labels)


# ── Step 5: Find the highest score (and stop early when you see a perfect one) ──
# Walk `scores` keeping track of the biggest you've seen so far.
# If you ever see a perfect 100, print "perfect!" and use `break` to leave
# the loop early. Otherwise print the highest score at the end.

# highest = 0
# for s in scores:
#     if s == 100:
#         print("perfect!")
#         highest = 100
#         break
#     if s > highest:
#         highest = s
# print(f"highest: {highest}")


# ── Step 6: Use range() to print a numbered list ─────────────────────────────
# Use `for i in range(len(scores))` to print each score with its position,
# like:
#     1: 72
#     2: 48
#     ...
# (Add 1 to `i` so it counts from 1 instead of 0.)

# for i in range(len(scores)):
#     print(f"{i + 1:2}: {scores[i]}")


# ── Step 7 (bonus): Skip the lowest scores with `continue` ───────────────────
# Print only the scores that are 55 or higher.
# Use `continue` to skip any score below 55.

# for s in scores:
#     if s < 55:
#         continue
#     print(s)
