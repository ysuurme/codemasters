import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Functions 🧩

        Welcome to Week 6 of the CodeMasters Fundamentals Program!

        A **function** is a mini-program inside a program: a named block of
        code that you can run (CALL) whenever you need it. You've already
        used built-in functions like `print()`, `input()`, and `len()`.
        This week you write your own.

        > **This notebook is a minimal companion to the script.** The
        > definitive walkthrough — including the Guess-the-number capstone
        > game — lives in `scripts/functions.py`.
        """
    )
    return


# ── Defining and calling ─────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Defining and calling

        ```python
        def hello():
            print("Howdy!")

        hello()      # ← the parentheses run it
        ```

        Defining a function does **not** run it — calling it does.
        """
    )
    return


@app.cell
def _():
    def hello():
        print("Howdy!")
        print("Hello there.")

    hello()
    hello()
    return


# ── Parameters and return values ─────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Parameters and `return`

        A **parameter** is a variable that receives a value when the
        function is called. `return` sends a value back to the caller.

        ```python
        def add(a, b):
            return a + b

        total = add(3, 5)   # total is 8
        ```
        """
    )
    return


@app.cell
def _():
    def add(a, b):
        return a + b

    def greet(name):
        return f"Hello, {name}!"

    print(add(3, 5))
    print(add(10, 20) * 2)
    print(greet("Alice"))
    return


# ── None and default arguments ───────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `None` and default arguments

        A function with no `return` line silently returns **`None`**.

        Parameters can have a **default value** — the caller can leave them out.

        ```python
        def greet(name, greeting="Hello"):
            print(f"{greeting}, {name}!")

        greet("Alice")              # uses the default
        greet("Bob", greeting="Hi") # overrides it
        ```
        """
    )
    return


@app.cell
def _():
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}!")

    greet("Alice")
    greet("Bob", greeting="Howdy")
    return


# ── Scope ────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Local vs global scope

        Variables defined inside a function live in its **local scope** —
        they vanish when the function ends. The function can read variables
        from the outside (**global scope**), but should prefer to *take what
        it needs* as a parameter and *return what it produces*.
        """
    )
    return


@app.cell
def _():
    shop_name = "CodeMasters Café"   # global

    def show_receipt(item, price):
        tax = price * 0.21           # local
        total = price + tax
        print(f"{shop_name}: {item} — €{total:.2f}")

    show_receipt("coffee", 3.00)
    show_receipt("sandwich", 6.50)
    return


# ── Summary ──────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        This week you learned:

        - **`def`** — defining your own functions
        - **Parameters** and **arguments** — passing data in
        - **`return`** — sending a value back
        - **`None`** — the "no value" value
        - **Keyword arguments** and **default values**
        - **Local vs global scope**

        Head to the `assignments/` folder for the **Tip Calculator** —
        a small bill-splitter made of several cooperating functions.

        > Error handling with `try` / `except` arrives in Week 9.
        """
    )
    return


if __name__ == "__main__":
    app.run()
