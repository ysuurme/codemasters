# Week 03 — Assignment: Family Heights

One practical assignment that brings together everything from this week.

**File:** `family_heights.py`

---

## The assignment

You will build a program that analyses the heights of your family members
using a list. Work through the steps inside the file one by one —
each step builds on the previous one.

### Steps

| Step | Task | Concepts used |
|------|------|--------------|
| 1 | Create `family_heights` with your family's heights | list creation |
| 2 | Calculate and print the number of family members | `len()` |
| 3 | Calculate and print the average height | arithmetic, f-string formatting |
| 4 | Find and print the shortest and tallest heights | `min()`, `max()` |
| 5 | Print a sublist with only the heights of members 2 and 3 | slicing `[1:3]` |
| 6 | Update a family member's height — they grew 2 cm! | index assignment |
| 7 | Ask the user for a new member's height and add it | `input()`, `float()`, `.append()` |

---

## How to run

```sh
python fundamentals/week-03-variables-and-input/assignments/family_heights.py
```

Uncomment one step at a time and run after each one to see the result.

---

## Tips

- `sum(my_list)` adds up all the numbers in a list — useful for the average.
- `min(my_list)` and `max(my_list)` work exactly as their names suggest.
- `input()` always returns a **string** — convert it with `float()` before doing maths.
- When you are done, commit your work:
  `"Week 03: family heights assignment complete"`
