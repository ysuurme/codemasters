# Week 07 — Assignment: Grocery Prices

One practical assignment that brings together everything from this week
plus a touch of the `for` loops and functions from Weeks 5 and 6.

**File:** `grocery_prices.py`

---

## The assignment

Build a small grocery price-list program using a **dictionary**.
Each step adds a feature that uses a function, method, or pattern you've
learned in this course.

### Steps

| Step | Task | Concepts used |
|------|------|--------------|
| 1 | Create the `groceries` dictionary with at least 5 items and prices | dict creation |
| 2 | Print the count, total, cheapest, and most expensive prices | `len`, `sum`, `min`, `max` |
| 3 | Print every item in uppercase with its price on its own line | `.items()`, `.upper()`, f-string `:.2f` |
| 4 | Add a new item, update a price, delete one item | `dict[key] = ...`, `del` |
| 5 | Build a new dict of items priced at €2.00 or less | for-loop + `.items()` filter |
| 6 | Write a `discount()` function and build a new dict with 10 % off | function from Week 6 + for-loop |
| 7 | Ask the user for an item and look up the price | `input()`, `in`, dict access |
| 8 | (Bonus) Count items per price band using a counter dict | counter pattern with a dict |

---

## How to run

```sh
python fundamentals/week-07-dictionaries/assignments/grocery_prices.py
```

Uncomment one step at a time and run after each one to see the result.

---

## Tips

- `.items()` gives you both the key and the value inside a for-loop.
- `groceries.values()` is a list-like view of just the prices — perfect for
  `sum`, `min`, `max`.
- To build a NEW dict from an existing one, start with `result = {}` then
  `result[key] = value` inside your for-loop — the same shape as the
  build-a-list pattern from Week 5, just with a dict instead.
- `input()` always returns a `str` — `.lower()` is handy to make the lookup
  case-insensitive.
- When you are done, commit your work:
  `"Week 07: grocery prices assignment complete"`
