# Week 07 — Dictionaries

This week you meet Python's most flexible data structure: the **dictionary**
— a collection of **key → value** pairs. Where a list stores values by
*position*, a dict stores them by *label*. Most real-world data shapes
(spreadsheet rows, API responses, contacts) are lists of dicts.

---

## What you will learn

- **Creating** dictionaries with `{key: value, ...}`
- **Reading** values with `dict[key]` and the safer `.get(key, default)`
- **Adding**, **updating**, and **deleting** keys (`del`)
- **Membership** with the `in` keyword
- **Looping** over a dict three ways:
  - keys (`for k in d:`)
  - values (`for v in d.values():`)
  - pairs (`for k, v in d.items():`)
- The **counter pattern** — using a dict to tally items in a list
- **Lists of dicts** — the shape of real-world data

---

## How to run the materials

**Option 1 — Marimo VS Code extension (easiest)**
Open this file in VS Code:

```
fundamentals/week-07-dictionaries/notebooks/nb_dictionaries.py
```

**Option 2 — Terminal (Marimo in the browser)**

```sh
marimo run fundamentals/week-07-dictionaries/notebooks/nb_dictionaries.py
```

**Option 3 — Plain script (press F5 in VS Code)**

```sh
python fundamentals/week-07-dictionaries/scripts/dictionaries.py
```

---

## After the lesson

Head to the `assignments/` folder for the **Grocery Prices** assignment —
build a small price-list program using a dictionary together with
`for`-loops and the functions you wrote last week.
