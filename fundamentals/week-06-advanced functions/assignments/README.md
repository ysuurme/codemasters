# Week 06 — Assignment: Grocery Prices

One practical assignment that brings together everything from this week.

**File:** `grocery_prices.py`

---

## The assignment

Build a small grocery price-list program using a **dictionary**.
Each step adds a feature that uses a function, method, or concept you
learned this week.

### Steps

| Step | Task | Concepts used |
|------|------|--------------|
| 1 | Create the `groceries` dictionary with at least 5 items and prices | dict creation |
| 2 | Print the count, total, cheapest, and most expensive prices | `len`, `sum`, `min`, `max` |
| 3 | Print every item in uppercase with its price on its own line | `.items()`, `.upper()`, f-string `:.2f` |
| 4 | Add a new item, update a price, delete one item | `dict[key] = ...`, `del` |
| 5 | List the items priced at €2.00 or less | `filter()` + `lambda` |
| 6 | Build a new list with a 10 % discount applied to every price | `map()` + `lambda` + `round()` |
| 7 | Ask the user for an item and look up the price | `input()`, `in`, dict access |

---

## How to run

```sh
python "fundamentals/week-06-advanced functions/assignments/grocery_prices.py"
```

Uncomment one step at a time and run after each one to see the result.

---

## Tips

- `.items()` gives you both the key and the value inside a for-loop.
- `groceries.values()` is a list-like view of just the prices — perfect for
  `sum`, `min`, `max`.
- A `lambda` is just an expression: `lambda price: price * 0.9`.
- `input()` always returns a `str` — convert with `float()` if you need a number,
  and `.lower()` is handy to make the lookup case-insensitive.
- When you are done, commit your work:
  `"Week 06: grocery prices assignment complete"`
