#!/usr/bin/env python3
"""Assignment — Family Heights

Work through the steps below one by one.
Run the script after each step to see the result.

Run with:
    python fundamentals/week-03-variables-and-input/assignments/family_heights.py
"""


# ── Step 1: Create the list ───────────────────────────────────────────────────
# Create a list called family_heights containing the heights (in cm) of your
# family members as floats. Use at least 4 members.
# Example: family_heights = [165.0, 182.5, 158.0, 174.0]

family_heights = []   # ← replace with your own family's heights


# ── Step 2: Total number of family members ────────────────────────────────────
# Use len() to find out how many members are in the list.
# Store the result in num_family_members and print it.

# num_family_members = ...
# print(f"Number of family members: {num_family_members}")


# ── Step 3: Average height ────────────────────────────────────────────────────
# Calculate the average height.
# Hint: sum(family_heights) gives you the total of all values.
# Divide by num_family_members and store in average_height.
# Print the average, rounded to 1 decimal place using :.1f in your f-string.

# average_height = ...
# print(f"Average height: {average_height:.1f} cm")


# ── Step 4: Shortest and tallest ──────────────────────────────────────────────
# Use min() and max() to find the shortest and tallest heights.
# Print both.

# shortest = ...
# tallest  = ...
# print(f"Shortest: {shortest} cm")
# print(f"Tallest : {tallest} cm")


# ── Step 5: Sublist — family members 2 and 3 ─────────────────────────────────
# Use slicing to get a new list with only the heights of family members
# at index 1 and 2 (the second and third members).
# Print the sublist.

# sub = ...
# print(f"Heights of members 2 and 3: {sub}")


# ── Step 6: Someone grew! ─────────────────────────────────────────────────────
# Family member at index 1 has grown 2 cm since last year.
# Update their height in the list and print the updated list.

# family_heights[1] = ...
# print(f"Updated heights: {family_heights}")


# ── Step 7: Console input ─────────────────────────────────────────────────────
# Ask the user to enter a new family member's height using input().
# Remember: input() always returns a str — convert it to float first.
# Append the new height to family_heights and print the final list.

# new_height = float(input("Enter a new family member's height in cm: "))
# family_heights.append(new_height)
# print(f"Final family list: {family_heights}")
