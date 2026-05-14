# Week 06 — Functions

This week you write your own **functions** — mini-programs with their own
inputs (parameters) and outputs (return values). Functions are the main way
you keep code organised and avoid duplication.

---

## What you will learn

- **`def`** — defining your own functions
- **Parameters** and **arguments** — passing data into a function
- **`return`** — sending a value back to the caller
- **`None`** — Python's "no value" value
- **Keyword arguments** — `print(end=, sep=)`
- **Default argument values** — making parameters optional
- **Local vs global scope** — where variables live, and why functions
  should *take what they need* and *return what they produce* rather than
  reach outside themselves
- A small **Guess-the-number** game that uses all of the above

> Error handling with `try` / `except` arrives in Week 9 — for now the
> guessing game trusts that you type a whole number.

---

## How to run the materials

**Option 1 — Marimo VS Code extension (easiest)**
Open this file in VS Code:

```
fundamentals/week-06-functions/notebooks/nb_functions.py
```

**Option 2 — Terminal (Marimo in the browser)**

```sh
marimo run fundamentals/week-06-functions/notebooks/nb_functions.py
```

**Option 3 — Plain script (run in a terminal — the Guess-the-number game uses `input()`)**

```sh
python fundamentals/week-06-functions/scripts/functions.py
```

> The notebook simulates `input()` with text boxes. To play the live
> Guess-the-number game, run the **script** in a terminal.

---

## After the lesson

Head to the `assignments/` folder for the **Tip Calculator** assignment —
build a small bill-splitter using several cooperating functions.
