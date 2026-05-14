import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Loops and Iteration 🔁

        Welcome to Week 5 of the CodeMasters Fundamentals Program!

        Last week (`while` loops) you repeated work *while a condition is true*.
        This week you repeat work *for every item in a collection* — the
        natural pattern for working with lists.

        > **This notebook is a minimal companion to the script.** The
        > definitive walkthrough lives in
        > `scripts/loops_and_iteration.py` — open it side-by-side, or run it
        > with **F5** to see every cell in action.
        """
    )
    return


# ── Looping over a list ───────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `for item in list`

        ```python
        for item in collection:
            do_something_with(item)
        ```

        Python walks the collection one item at a time, names it `item`
        (you pick the name), and runs the indented block for each.
        """
    )
    return


@app.cell
def _():
    groceries = ["apples", "milk", "bread", "tofu"]
    for item in groceries:
        print(f"  - {item}")
    return


# ── range() ───────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `range()` — when you need a counter

        | Call | Produces |
        |------|----------|
        | `range(stop)` | `0, 1, ..., stop - 1` |
        | `range(start, stop)` | `start, ..., stop - 1` |
        | `range(start, stop, step)` | `start, start + step, ...` |
        """
    )
    return


@app.cell
def _(mo):
    start_input = mo.ui.number(value=0,  start=-10, stop=20, label="start")
    stop_input  = mo.ui.number(value=10, start=-10, stop=30, label="stop")
    step_input  = mo.ui.number(value=2,  start=-5,  stop=10, label="step")
    mo.vstack([start_input, stop_input, step_input])
    return start_input, step_input, stop_input


@app.cell
def _(mo, start_input, step_input, stop_input):
    step = step_input.value or 1
    values = list(range(start_input.value, stop_input.value, step))
    mo.md(
        f"""
        `range({start_input.value}, {stop_input.value}, {step})` →
        **`{values}`** ({len(values)} value(s))
        """
    )
    return


# ── Four loop patterns ───────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## The four patterns you'll use forever

        1. **Count** items that match a rule — start a counter at `0`, add 1 inside the loop.
        2. **Sum / average** — start `total = 0`, add each item inside the loop.
        3. **Build a new list** — start `result = []`, `.append()` inside the loop.
        4. **Find first match** — walk the list, `break` when you find it.

        See the script for fully-worked examples of each.
        """
    )
    return


@app.cell
def _():
    scores = [72, 48, 88, 55, 34, 91, 67]

    passed = 0
    for s in scores:
        if s >= 55:
            passed = passed + 1
    print(f"  passed: {passed} of {len(scores)}")

    total = 0
    for s in scores:
        total = total + s
    print(f"  average: {total / len(scores):.1f}")
    return


# ── break / continue ─────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `break` and `continue`

        Same as inside a `while` loop:
        - `break` — leave the loop immediately.
        - `continue` — skip the rest of this iteration, go to the next item.
        """
    )
    return


@app.cell
def _():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    for n in numbers:
        if n % 2 == 1:
            continue
        print(f"  even: {n}")
    return


# ── Summary ──────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        This week you learned:

        - **`for item in list`** — walk a collection naturally
        - **`range(stop)`, `range(start, stop)`, `range(start, stop, step)`**
        - **`break`** and **`continue`** inside a `for` loop
        - The four patterns: **count**, **sum**, **build**, **find first**
        - **Nested loops** for multi-dimensional work

        Head to the `assignments/` folder for the **Grade Analyzer**. 📊
        """
    )
    return


if __name__ == "__main__":
    app.run()
