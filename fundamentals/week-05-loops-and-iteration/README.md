# Week 05 — Loops and Iteration

This week you meet the `for` loop — Python's natural way to "do something
to every item in a list" — together with `range()`, `break`, and `continue`,
and the common patterns you'll reach for again and again.

> Last week (`while` loops) you repeated work *while a condition is true*.
> This week you repeat work *for every item in a collection*.

---

## What you will learn

- **`for item in list`** — the standard way to walk a list
- **Looping over strings** — strings are sequences of characters
- **`range()`** — produce a sequence of integers; `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- **`break`** and **`continue`** inside a `for` loop
- **Four loop patterns** you'll use forever:
  - **counting** items that match a rule
  - **summing / averaging** numbers
  - **building** a new list with `.append()`
  - **finding** the first matching item with `break`
- **Nested loops** — a `for` inside another `for` (multiplication table)

---

## How to run the materials

**Option 1 — Marimo VS Code extension (easiest)**
Open this file in VS Code:

```
fundamentals/week-05-loops-and-iteration/notebooks/nb_loops_and_iteration.py
```

**Option 2 — Terminal (Marimo in the browser)**

```sh
marimo run fundamentals/week-05-loops-and-iteration/notebooks/nb_loops_and_iteration.py
```

**Option 3 — Plain script (press F5 in VS Code)**

```sh
python fundamentals/week-05-loops-and-iteration/scripts/loops_and_iteration.py
```

---

## After the lesson

Head to the `assignments/` folder for the **Grade Analyzer** assignment —
a small but realistic program that practises all four loop patterns from
this week against a list of student scores.
