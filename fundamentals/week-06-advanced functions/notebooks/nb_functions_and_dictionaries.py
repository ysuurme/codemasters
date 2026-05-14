import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Advanced Functions and Dictionaries 🛠️

        Welcome to Week 6 of the CodeMasters Fundamentals Program!

        This week you expand your toolkit with **built-in functions**, **methods**,
        the **higher-order functions** `map` and `filter`, **lambdas**, and a
        brand new data structure: the **dictionary**.
        """
    )
    return


# ── Built-in functions ────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Built-in functions

        Python ships with many functions you can use without importing anything.
        You met a few in Week 3 — here is a wider toolbox.

        | Function | What it does |
        |----------|-------------|
        | `len(x)` | Number of items |
        | `sum(x)` | Total of all numbers |
        | `min(x)` / `max(x)` | Smallest / largest value |
        | `abs(x)` | Absolute value — drops the minus sign |
        | `round(x, n)` | Round to `n` decimals |
        | `sorted(x)` | A new sorted copy |
        | `type(x)` | The type of a value |

        Move the slider to change the list and see every built-in update live.
        """
    )
    return


@app.cell
def _(mo):
    extra = mo.ui.slider(start=-20, stop=20, value=12, label="Add a number")
    extra
    return (extra,)


@app.cell
def _(extra, mo):
    numbers = [3, 8, 1, -5, 7, extra.value]
    mo.md(
        f"""
        `numbers` = `{numbers}`

        | Call | Result |
        |------|--------|
        | `len(numbers)` | **{len(numbers)}** |
        | `sum(numbers)` | **{sum(numbers)}** |
        | `min(numbers)` | **{min(numbers)}** |
        | `max(numbers)` | **{max(numbers)}** |
        | `abs(min(numbers))` | **{abs(min(numbers))}** |
        | `sorted(numbers)` | `{sorted(numbers)}` |
        """
    )
    return


# ── Methods ───────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Methods — functions that belong to a value

        A **method** is a function that belongs to a specific type of value.
        You call it with a **dot**: `value.method_name()`

        - Built-in function works **on** a value: `len(my_list)`
        - Method is called **on** a value: `my_list.append("x")`

        Different types have different methods. In VS Code, type a `.` after a
        variable to see what is available.
        """
    )
    return


@app.cell
def _():
    fruits = ["banana", "apple", "cherry"]
    print(f"start             : {fruits}")

    fruits.append("mango")
    print(f"after .append     : {fruits}")

    fruits.sort()
    print(f"after .sort()     : {fruits}")

    fruits.reverse()
    print(f"after .reverse()  : {fruits}")

    print(f".count('banana')  : {fruits.count('banana')}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### String methods

        Strings have their own set of methods. Type a sentence to try them.
        """
    )
    return


@app.cell
def _(mo):
    sentence = mo.ui.text(value="Good Morning, CodeMasters!", label="Your sentence")
    sentence
    return (sentence,)


@app.cell
def _(mo, sentence):
    s = sentence.value or "Good Morning, CodeMasters!"
    mo.md(
        f"""
        | Call | Result |
        |------|--------|
        | `s.upper()` | `{s.upper()!r}` |
        | `s.lower()` | `{s.lower()!r}` |
        | `s.replace('Morning', 'Evening')` | `{s.replace('Morning', 'Evening')!r}` |
        | `s.split(' ')` | `{s.split(' ')}` |
        | `len(s)` | `{len(s)}` |
        """
    )
    return


# ── map() ─────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `map()` — do this to each one

        `map(function, list)` applies the function to every item in the list.
        Wrap it in `list(...)` to see the values.

        ```python
        def squared(x):
            return x * x

        list(map(squared, [1, 2, 3]))   # → [1, 4, 9]
        ```
        """
    )
    return


@app.cell
def _():
    def squared(x):
        return x * x

    numbers = [1, 2, 3, 5, 7, 11]
    squares = list(map(squared, numbers))

    groceries = ["apples", "milk", "bread"]
    shouted   = list(map(str.upper, groceries))

    print(f"numbers   : {numbers}")
    print(f"squared   : {squares}")
    print(f"groceries : {groceries}")
    print(f"SHOUTED   : {shouted}")
    return


# ── filter() ──────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `filter()` — keep only the ones where this is true

        `filter(function, list)` keeps every item for which the function returns `True`.

        Move the slider to change the cutoff and see which numbers pass through.
        """
    )
    return


@app.cell
def _(mo):
    cutoff = mo.ui.slider(start=0, stop=10, value=5, label="Keep numbers ≥")
    cutoff
    return (cutoff,)


@app.cell
def _(cutoff, mo):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kept    = list(filter(lambda x: x >= cutoff.value, numbers))
    mo.md(
        f"""
        `numbers` = `{numbers}`

        `filter(lambda x: x >= {cutoff.value}, numbers)` → **`{kept}`**
        """
    )
    return


# ── lambda ────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `lambda` — anonymous one-line functions

        A **lambda** is a small function written on a single line, without `def`.

        ```
        lambda arguments: expression
        ```

        Lambdas are handy when you need a tiny function **once** — typically
        as the first argument to `map()`, `filter()`, or `sorted()`.
        """
    )
    return


@app.cell
def _():
    # Same function, two ways:
    def double(x):
        return x * 2

    double_lam = lambda x: x * 2

    print(f"double(5)      = {double(5)}")
    print(f"double_lam(5)  = {double_lam(5)}")

    numbers = [1, 2, 3, 5, 7, 11]
    print(f"squared (lambda)  : {list(map(lambda x: x ** 2, numbers))}")
    print(f"odd     (lambda)  : {list(filter(lambda x: x % 2, numbers))}")
    return


# ── Dictionaries ──────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Dictionaries — key/value pairs

        A **dictionary** stores data as `key: value` pairs.

        - A **list** is indexed by position: `prices[0]`
        - A **dict** is indexed by key: `prices["milk"]`

        Use a dict when each value has a label — names with ages, products with
        prices, students with grades, etc.

        | Action | Code |
        |--------|------|
        | Create | `{"name": "Marijn", "age": 48}` |
        | Read | `teacher["name"]` |
        | Add / update | `teacher["job"] = "Engineer"` |
        | Delete | `del teacher["city"]` |
        | Check key | `"name" in teacher` |
        | Loop | `for k, v in teacher.items():` |
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

    print(f"teacher           : {teacher}")
    print(f"teacher['name']   : {teacher['name']}")
    print(f"len(teacher)      : {len(teacher)}")

    teacher["job"] = "Engineer"
    teacher["age"] = 49
    del teacher["city"]

    print(f"after changes     : {teacher}")
    print()
    for key, value in teacher.items():
        print(f"  {key:5} → {value}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Live grade book

        Type a student name and a score, then read the live class statistics.
        Behind the scenes the cell uses `sum`, `min`, `max`, `map`, `filter` and `lambda`.
        """
    )
    return


@app.cell
def _(mo):
    new_name  = mo.ui.text(value="Sam", label="Name")
    new_score = mo.ui.number(value=72, start=0, stop=100, label="Score (0-100)")
    mo.vstack([new_name, new_score])
    return (new_name, new_score)


@app.cell
def _(mo, new_name, new_score):
    grades = {
        "Iris": 48,
        "Tom":  88,
        "Aysha": 55,
        "Leo":  34,
    }
    if new_name.value:
        grades[new_name.value] = int(new_score.value)

    scores       = list(grades.values())
    to_dutch     = lambda pct: round(pct / 10, 1)
    dutch_grades = list(map(to_dutch, scores))
    passed       = list(filter(lambda n: to_dutch(grades[n]) >= 5.5, grades))

    mo.md(
        f"""
        **Grades:** `{grades}`

        | Stat | Value |
        |------|-------|
        | Students | **{len(grades)}** |
        | Average | **{sum(scores) / len(grades):.1f}%** |
        | Lowest / highest | **{min(scores)}% / {max(scores)}%** |
        | Dutch grades | `{dutch_grades}` |
        | Passed (≥ 5.5) | `{passed}` |
        """
    )
    return


# ── Summary ───────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        This week you learned:

        - **Built-in functions** — `len`, `sum`, `min`, `max`, `abs`, `round`, `sorted`, `type`
        - **Methods** — `value.method_name()`; different types have different methods
        - **`map()`** — apply a function to every item in a list
        - **`filter()`** — keep only the items that match a condition
        - **`lambda`** — write tiny anonymous functions inline
        - **Dictionaries** — store data as `key: value` pairs; add, update, delete, iterate, `in`

        Head to the `assignments/` folder when you are ready to practise. 💪
        """
    )
    return


if __name__ == "__main__":
    app.run()
