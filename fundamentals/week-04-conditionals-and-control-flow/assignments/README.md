# Week 04 — Assignment: Traffic Light Advisor

One practical assignment that brings together everything from this week.

**File:** `traffic_light.py`

---

## The assignment

Build a small **traffic-light advisor** that tells the user what to do at
a junction. Each step adds a new feature using one of this week's topics.

### Steps

| Step | Task | Concepts used |
|------|------|--------------|
| 1 | Create two boolean variables describing the scene | `bool`, f-strings |
| 2 | Print "STOP" or "GO" based on the light | `if` / `else`, `==` |
| 3 | Add the yellow light and an "Unknown" fallback | `elif`, multi-way branching |
| 4 | Warn when a pedestrian in a hurry crosses on yellow | `and`, boolean combinations |
| 5 | Walk a cycle of lights with `while` and an index, printing advice for each | `while` + index, `len()` |
| 6 | Count green lights in a row until the first non-green | `while True`, `break` |
| 7 | Ask the user for the colour and pedestrian status with `input()` | `input()`, full decision tree |

---

## How to run

```sh
python fundamentals/week-04-conditionals-and-control-flow/assignments/traffic_light.py
```

Uncomment one step at a time and run after each one to see the result.

---

## Tips

- `input()` always returns a **string** — `.lower().strip()` keeps stray
  capitals and spaces from breaking the comparison.
- `==` checks equality; `=` assigns. They are NOT interchangeable.
- For the `while True` loop, make sure something inside the loop eventually
  triggers `break`, or you'll be stuck in an infinite loop. Press **Ctrl + C**
  in the terminal to escape.
- When you are done, commit your work:
  `"Week 04: traffic light assignment complete"`
