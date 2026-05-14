#!/usr/bin/env python3
"""Assignment — Traffic Light Advisor

Build a small advisor that tells you what to do at a traffic light.
Each step adds a feature that uses one of this week's topics: booleans,
comparisons, boolean operators, if/elif/else, while, and for/range.

Work through the steps one by one — uncomment each block, run the script,
and check the output before moving on.

Run with:
    python fundamentals/week-04-conditionals-and-control-flow/assignments/traffic_light.py
"""


# ── Step 1: Boolean values ───────────────────────────────────────────────────
# Make two boolean variables describing the scene:
#   - is_pedestrian: True if you are walking, False if you are driving
#   - is_in_a_hurry: True if you are running late, False otherwise
# Print both with f-strings.

# is_pedestrian = True
# is_in_a_hurry = False
# print(f"pedestrian : {is_pedestrian}")
# print(f"in a hurry : {is_in_a_hurry}")


# ── Step 2: A simple if / else for the light ─────────────────────────────────
# Set a variable `light` to one of "red", "yellow", or "green".
# Print:
#   - "STOP"  if the light is "red"
#   - "GO"    otherwise

# light = "red"
# if light == "red":
#     print("STOP")
# else:
#     print("GO")


# ── Step 3: Add elif for the yellow light ────────────────────────────────────
# Extend Step 2 so that:
#   - "red"    → "STOP"
#   - "yellow" → "SLOW DOWN"
#   - "green"  → "GO"
#   - anything else → "Unknown light"

# light = "yellow"
# if light == "red":
#     print("STOP")
# elif light == "yellow":
#     print("SLOW DOWN")
# elif light == "green":
#     print("GO")
# else:
#     print("Unknown light")


# ── Step 4: Combine conditions with boolean operators ────────────────────────
# A pedestrian in a hurry running a yellow light is risky.
# Print "Careful! Risky crossing" when the light is "yellow"
# AND is_pedestrian is True AND is_in_a_hurry is True.
# Otherwise print "Safe enough".

# light = "yellow"
# is_pedestrian = True
# is_in_a_hurry = True
# if light == "yellow" and is_pedestrian and is_in_a_hurry:
#     print("Careful! Risky crossing")
# else:
#     print("Safe enough")


# ── Step 5: Loop a sequence of lights with a for-loop ────────────────────────
# A traffic light cycles. Loop over this list and print the advice for each
# light using your if/elif/else from Step 3.

# cycle = ["red", "red", "green", "green", "yellow", "red"]
# for light in cycle:
#     if light == "red":
#         print(f"{light:6} → STOP")
#     elif light == "yellow":
#         print(f"{light:6} → SLOW DOWN")
#     else:
#         print(f"{light:6} → GO")


# ── Step 6: Count green lights using a while-loop with break ─────────────────
# Pretend you are driving and want to count how many GREEN lights in a row you
# pass before the FIRST non-green one. Use a while True loop with break.

# drive = ["green", "green", "green", "yellow", "green", "red"]
# i = 0
# greens_in_a_row = 0
# while True:
#     if i >= len(drive):
#         break
#     if drive[i] != "green":
#         break
#     greens_in_a_row = greens_in_a_row + 1
#     i = i + 1
# print(f"Greens in a row before stopping: {greens_in_a_row}")


# ── Step 7: Putting it together — interactive advisor ────────────────────────
# Use input() to ask the user for the current light colour.
# Then ask whether they are a pedestrian (answer 'y' or 'n').
# Use input().lower().strip() so case and stray spaces don't break it.
# Print the right advice based on both inputs.

# light = input("Light colour (red / yellow / green): ").lower().strip()
# answer = input("Are you a pedestrian? (y/n): ").lower().strip()
# is_pedestrian = answer == "y"
#
# if light == "red":
#     print("STOP — wait for it to change.")
# elif light == "yellow" and is_pedestrian:
#     print("Don't start crossing.")
# elif light == "yellow":
#     print("Slow down and prepare to stop.")
# elif light == "green":
#     print("Go — but check before you cross.")
# else:
#     print(f"'{light}' is not a valid light.")
