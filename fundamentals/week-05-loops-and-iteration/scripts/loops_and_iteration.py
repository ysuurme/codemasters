#!/usr/bin/env python3
"""Week 05 — Loops and Iteration

Run this script to learn the `for` loop — the natural way to do something
to every item in a collection — and the helpers `range()`, `break`, and
`continue`.

    python fundamentals/week-05-loops-and-iteration/scripts/loops_and_iteration.py
"""


# ── Why for-loops? ────────────────────────────────────────────────────────────
# Last week you met `while` loops — they repeat as long as a condition is True.
# Most of the time, though, you don't want "while something is true": you want
# "do this thing to each item in a list". That's what FOR loops are for.
#
#   for item in collection:
#       do_something_with(item)
#
# Python walks through the collection one item at a time, gives it the name
# `item` (you pick the name), and runs the indented block for each.


# ── Looping over a list ───────────────────────────────────────────────────────
print("=== Looping over a list ===")

groceries = ["apples", "milk", "bread", "tofu"]

for item in groceries:
    print(f"  - {item}")

# Compare to the while-with-index pattern from Week 4 — same result, fewer lines:
#   i = 0
#   while i < len(groceries):
#       print(groceries[i])
#       i = i + 1


# ── Looping over a string ─────────────────────────────────────────────────────
# Strings are sequences too, so you can loop over them character by character.

print("\n=== Looping over a string ===")

word = "Python"
for letter in word:
    print(f"  letter: {letter}")


# ── Counting with range() ─────────────────────────────────────────────────────
# When you need a counter — or just want to repeat something N times — use
# `range()`. It produces a sequence of integers.
#
#   range(stop)              0, 1, 2, ..., stop-1
#   range(start, stop)       start, start+1, ..., stop-1
#   range(start, stop, step) start, start+step, ... (up to but not including stop)

print("\n=== for + range() ===")

for i in range(5):              # 0, 1, 2, 3, 4
    print(f"  i = {i}")

print("  ---")
for i in range(2, 6):           # 2, 3, 4, 5
    print(f"  i = {i}")

print("  ---")
for i in range(0, 20, 5):       # 0, 5, 10, 15
    print(f"  step = {i}")

print("  ---")
# range() also works backwards with a negative step:
for i in range(5, 0, -1):       # 5, 4, 3, 2, 1
    print(f"  countdown = {i}")


# ── break and continue inside a for-loop ──────────────────────────────────────
# These work the same way as in a `while` loop:
#   break    → stop the loop immediately
#   continue → skip the rest of this iteration, go to the next item

print("\n=== break ===")

words = ["red", "yellow", "STOP", "green", "blue"]
for w in words:
    if w == "STOP":
        print("  found STOP — leaving the loop")
        break
    print(f"  saw: {w}")


print("\n=== continue ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for n in numbers:
    if n % 2 == 1:          # odd → skip
        continue
    print(f"  even: {n}")


# ── Pattern 1: counting items that match ──────────────────────────────────────
# A very common job: walk a list and count the ones that match some rule.

print("\n=== Counting items ===")

scores = [72, 48, 88, 55, 34, 91, 67]
passed = 0
for s in scores:
    if s >= 55:
        passed = passed + 1
print(f"  {passed} of {len(scores)} students passed")


# ── Pattern 2: summing and averaging ──────────────────────────────────────────
# `sum()` and `len()` already exist for this, but doing it by hand once helps
# you understand what's happening inside the loop.

print("\n=== Summing by hand ===")

total = 0
for s in scores:
    total = total + s
average = total / len(scores)
print(f"  total   = {total}")
print(f"  average = {average:.1f}")


# ── Pattern 3: building a new list ────────────────────────────────────────────
# Start with an empty list, then `.append()` one item per iteration.

print("\n=== Building a new list ===")

prices       = [2.49, 0.99, 1.89, 3.20]
with_tax     = []
for p in prices:
    with_tax.append(round(p * 1.21, 2))
print(f"  prices   = {prices}")
print(f"  with_tax = {with_tax}")


# ── Pattern 4: finding the first match ────────────────────────────────────────
# Use `break` to stop as soon as you've found what you need.

print("\n=== Finding the first match ===")

names  = ["Sam", "Iris", "Tom", "Aysha", "Leo"]
target = "Tom"

found_at = -1
for i in range(len(names)):
    if names[i] == target:
        found_at = i
        break

if found_at >= 0:
    print(f"  '{target}' is at position {found_at}")
else:
    print(f"  '{target}' is not in the list")


# ── Putting it together — a tiny multiplication table ─────────────────────────
# Nested loops: a `for` inside another `for`. The inner loop runs FULLY for
# every step of the outer loop.

print("\n=== Putting it together — multiplication table ===")

for row in range(1, 6):
    line = ""
    for col in range(1, 6):
        line = line + f"{row * col:4}"
    print(line)
