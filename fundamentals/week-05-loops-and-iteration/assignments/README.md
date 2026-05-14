# Week 05 — Assignment: Grade Analyzer

One practical assignment that brings together every `for`-loop pattern from
this week.

**File:** `grade_analyzer.py`

---

## The assignment

Given a fixed list of student scores, build a small analyser that prints
the scores, counts how many passed, computes the average by hand, builds
a labels list, finds the highest, and produces a numbered listing —
all using `for` loops.

### Steps

| Step | Task | Concepts used |
|------|------|--------------|
| 1 | Print every score on its own line | `for item in list` |
| 2 | Count how many students passed (≥ 55) | counter pattern |
| 3 | Compute the average by hand with a running total | sum pattern |
| 4 | Build a list of `"pass"` / `"fail"` labels | build-a-list with `.append()` |
| 5 | Find the highest score, stop early on a perfect 100 | find-first with `break` |
| 6 | Print a numbered list with `range(len(scores))` | `for` + `range()` + indexing |
| 7 | (Bonus) Print only passing scores using `continue` | `continue` |

---

## How to run

```sh
python fundamentals/week-05-loops-and-iteration/assignments/grade_analyzer.py
```

Uncomment one step at a time and run after each one to see the result.

---

## Tips

- Counter pattern: `count = 0` *before* the loop, `count = count + 1` *inside*.
- Sum pattern: `total = 0` before; `total = total + s` inside.
- Build-a-list pattern: `labels = []` before; `labels.append(...)` inside.
- `range(len(my_list))` gives you the *indices*; use `my_list[i]` to read each item.
- `break` leaves the loop immediately; `continue` skips to the next iteration.
- When you are done, commit your work:
  `"Week 05: grade analyzer assignment complete"`
