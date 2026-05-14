# Week 06 — Assignment: Tip Calculator

One practical assignment that brings together everything from this week.

**File:** `tip_calculator.py`

---

## The assignment

Build a tiny **bill-splitter** made of several cooperating functions.
Each step adds one new function, building on the ones before it. By the
end you'll have four small functions calling each other — the way real
programs grow.

### Steps

| Step | Task | Concepts used |
|------|------|--------------|
| 1 | `tip(amount)` — return 15 % of the amount | `def`, parameter, `return` |
| 2 | Add a default `percentage=0.15` and override it from the call | default arguments, keyword arguments |
| 3 | `total_with_tip(amount, percentage=0.15)` — calls `tip()` inside | functions calling functions |
| 4 | `split(amount, num_people, percentage=0.15)` — reuses `total_with_tip()` | more reuse |
| 5 | `print_receipt(...)` — a function that PRINTS instead of returns | side effects, implicit `None` |
| 6 | Read the bill, people, and tip percentage from the user | `input()`, `float()`, `int()` |

---

## How to run

```sh
python fundamentals/week-06-functions/assignments/tip_calculator.py
```

Uncomment one step at a time and run after each one to see the result.

---

## Tips

- A function with no `return` line silently returns `None`. That's fine for
  helpers like `print_receipt()` that exist for their side effect.
- When one function calls another, the called function runs to completion
  *before* the calling function continues — like a sub-task.
- `input()` always returns a string. Convert with `float()` for money and
  `int()` for whole numbers. If the user types junk, the program will
  crash — Week 9 covers how to handle that gracefully.
- When you are done, commit your work:
  `"Week 06: tip calculator assignment complete"`
