# Week 05 — Assignment: Collatz Sequence

One practical assignment that brings together everything from this week.

**File:** `collatz_sequence.py`

---

## The assignment

The **Collatz sequence** is a famous tiny puzzle:

- If a number is **even** → next number is `number // 2`
- If a number is **odd**  → next number is `3 * number + 1`

Repeat the rule and you always reach `1` — eventually.
(No one knows for sure WHY.)

You will build the sequence step by step, then make the program friendly
by validating user input with `try` / `except`.

### Steps

| Step | Task | Concepts used |
|------|------|--------------|
| 1 | Define `collatz(number)` that prints and returns the next value | `def`, `if/else`, `return` |
| 2 | Call `collatz()` manually a few times starting from 10 | function calls, return values |
| 3 | Read the starting number from the user with `input()` | `input()`, `int()` |
| 4 | Loop with `while number != 1` until the sequence reaches 1 | `while` loop, reassignment |
| 5 | Wrap the `int()` call in `try` / `except ValueError` | error handling |
| 6 | (Bonus) Reject zero and negative numbers | `if`, defensive check |

### Example output

```
Enter a starting number: 3
10
5
16
8
4
2
1
```

---

## How to run

```sh
python fundamentals/week-05-functions/assignments/collatz_sequence.py
```

Uncomment one step at a time and run after each one to see the result.

---

## Tips

- A number is **even** when `number % 2 == 0`.
- Use `//` (integer division) so `number // 2` returns an `int`, not a `float`.
- `input()` always returns a **string** — `int()` converts it to a whole number,
  and `try / except ValueError` keeps the program friendly when the input is junk.
- A `while` loop ends when its condition becomes False, so make sure the
  reassignment inside the loop eventually leads to `number == 1`.
- When you are done, commit your work:
  `"Week 05: collatz sequence assignment complete"`
