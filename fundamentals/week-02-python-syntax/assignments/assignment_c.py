#!/usr/bin/env python3
"""Assignment C — Christmas Tree 🎄

Print a Christmas tree in the terminal using only print() and strings.

Run with:
    python fundamentals/week-02-python-syntax/assignments/assignment_c.py

── Hints ─────────────────────────────────────────────────────────────────────

String repetition with * lets you be smart with spacing:

    " " * 5   →  "     "       (5 spaces)
    "*" * 7   →  "*******"     (7 stars)
    " " * 3 + "*" * 5  →  "   *****"

So instead of counting spaces by hand:
    print("      *")        ← tedious and error-prone

You can write:
    width = 13               # total width of the widest row
    print(" " * 6 + "*")    # or calculate the spaces from the width

── Requirements ──────────────────────────────────────────────────────────────

  ✓ At least 6 layers of branches
  ✓ A trunk at the bottom (use | or █ or any character you like)
  ✓ Use string repetition (* operator) — do not count spaces by hand

── Extra points ──────────────────────────────────────────────────────────────

  ⭐ Add a star or decoration at the top
  ⭐ Add baubles or ornaments on the branches (e.g. o * o * o)
  ⭐ Print a second object (a house, a rocket, a snowman — anything you like!)

── Example output (yours should look different!) ─────────────────────────────

        *
       ***
      *****
     *******
    *********
   ***********
  *************
       |||
       |||

─────────────────────────────────────────────────────────────────────────────
"""

print("=== My Christmas Tree ===")
print()

# Write your tree below.
# Tip: build one row at a time and run the script after each line.
