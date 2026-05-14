import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Dictionaries 📚

        Welcome to Week 7 of the CodeMasters Fundamentals Program!

        A **dictionary** is a collection of **key → value** pairs. Where a
        list stores values by *position*, a dict stores them by a *label*
        you choose. Most real-world data shapes (spreadsheet rows, API
        responses, contacts) are *lists of dicts*.

        > **This notebook is a minimal companion to the script.** The
        > definitive walkthrough lives in `scripts/dictionaries.py`.
        """
    )
    return


# ── Creating and reading ─────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating and reading

        ```python
        teacher = {
            "name": "Marijn",
            "age": 48,
            "city": "Eindhoven",
        }

        teacher["name"]            # "Marijn"
        teacher.get("country", "?")  # safer: returns "?" if the key is missing
        ```
        """
    )
    return


@app.cell
def _():
    teacher = {
        "name": "Marijn",
        "age": 48,
        "city": "Eindhoven",
    }

    print(teacher["name"])
    print(teacher.get("country", "unknown"))
    print(f"len: {len(teacher)}")
    return (teacher,)


# ── Modifying ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Adding, updating, deleting

        ```python
        teacher["job"] = "Engineer"   # add
        teacher["age"] = 49           # update
        del teacher["city"]           # remove
        ```
        """
    )
    return


@app.cell
def _(teacher):
    teacher["job"] = "Engineer"
    teacher["age"] = 49
    if "city" in teacher:
        del teacher["city"]
    print(teacher)
    return


# ── Looping ──────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Looping over a dict

        - `for k in d:` — keys
        - `for v in d.values():` — values
        - `for k, v in d.items():` — pairs (the most useful one)
        """
    )
    return


@app.cell
def _(teacher):
    for key, value in teacher.items():
        print(f"  {key:5} → {value}")
    return


# ── Counter pattern ──────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## A dict as a counter

        A classic pattern — count how often each item appears in a list.
        """
    )
    return


@app.cell
def _():
    words   = ["red", "green", "red", "blue", "green", "red"]
    counts  = {}
    for w in words:
        if w in counts:
            counts[w] = counts[w] + 1
        else:
            counts[w] = 1
    print(counts)
    return


# ── Lists of dicts ───────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Lists of dicts — real-world shaped data

        Each dict is one **record**; each key is one **field**.
        This is the shape of almost every real-world data source.
        """
    )
    return


@app.cell
def _():
    students = [
        {"name": "Sam",   "age": 19, "score": 72},
        {"name": "Iris",  "age": 21, "score": 48},
        {"name": "Tom",   "age": 24, "score": 88},
    ]
    for s in students:
        print(f"  {s['name']:6} ({s['age']}) → {s['score']}")
    return


# ── Summary ──────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        This week you learned:

        - **Creating** dictionaries with `{key: value, ...}`
        - **Reading** with `d[key]` and `.get(key, default)`
        - **Adding**, **updating**, **deleting** keys
        - **Membership** with `in`
        - **Looping** with keys, `.values()`, and `.items()`
        - The **counter pattern** with a dict
        - **Lists of dicts** for real-world shaped data

        Head to the `assignments/` folder for the **Grocery Prices** assignment. 🛒
        """
    )
    return


if __name__ == "__main__":
    app.run()
