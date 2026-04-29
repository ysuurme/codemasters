import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Python Syntax 🐍

        Welcome to Week 2 of the CodeMasters Fundamentals Program!

        This week you learn the building blocks of Python: how to print output,
        what kinds of data Python understands, how to do operations on that data,
        and how to convert between types.
        """
    )
    return


# ── Comments ──────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Comments

        A **comment** starts with `#` and is completely ignored by Python.
        Use comments to explain *why* you did something — not *what*
        (the code already shows the what).

        ```python
        # This entire line is a comment — Python skips it.
        savings = 20   # you can also comment at the end of a line
        ```

        Good comments make your code readable six months from now.
        """
    )
    return


@app.cell
def _():
    # This is a comment — it does not affect the output at all.
    name = "CodeMasters"   # the variable stores the program name
    print(name)            # this line prints the value of name
    return


# ── print() ───────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `print()`

        `print()` displays whatever you put inside its brackets.
        It is the most useful tool for a beginner: it shows results,
        helps you follow along, and lets you check values while debugging.
        """
    )
    return


@app.cell
def _():
    print("Hello, World!")      # text
    print(42)                   # whole number
    print(3.14)                 # decimal number
    print(10 + 5)               # Python calculates first, then prints
    print()                     # blank line
    print("The answer is", 42)  # comma → Python adds a space
    return


# ── Variable types ─────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Variable types

        A **variable** is a named box that stores a value.
        Every value has a **type** — it tells Python what kind of data it is.

        | Type | What it stores | Example |
        |------|---------------|---------|
        | `str` | Text — always in quotes | `"hello"` |
        | `int` | Whole number — no decimal | `42` |
        | `float` | Decimal number | `3.14` |
        | `bool` | True or False — nothing else | `True` |

        Python figures out the type automatically.
        Use `type()` to check.
        """
    )
    return


@app.cell
def _():
    name       = "Sam"     # str
    age        = 27        # int
    height_cm  = 182.5     # float
    is_student = True      # bool  ← "is_" prefix is the convention for booleans

    print(f"name       = {name!r:<12}  type: {type(name).__name__}")
    print(f"age        = {age:<12}  type: {type(age).__name__}")
    print(f"height_cm  = {height_cm:<12}  type: {type(height_cm).__name__}")
    print(f"is_student = {is_student!r:<12}  type: {type(is_student).__name__}")
    return


# ── Operations on types ────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Operations on strings

        The same operator behaves differently depending on the type.

        | Operator | On strings | Example | Result |
        |----------|-----------|---------|--------|
        | `+` | Joins strings | `"Code" + "Masters"` | `"CodeMasters"` |
        | `*` | Repeats a string | `"ha" * 3` | `"hahaha"` |

        **The classic beginner surprise:** `"5" + "3"` is `"53"` — not `8`!
        Python joins strings, it does not add them as numbers.
        """
    )
    return


@app.cell
def _():
    print("Code" + "Masters")       # join
    print("Code" + " " + "Masters") # join with space
    print("ha" * 3)                 # repeat
    print("-" * 30)                 # handy divider trick
    print()
    print("'5' + '3'  =", "5" + "3")   # "53" — strings are joined!
    print(" 5  +  3   =", 5 + 3)        #  8   — integers are added
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Operations on numbers

        Use the sliders to explore the seven arithmetic operators on any two numbers.
        Notice that `/` always returns a **float**, even when the result is whole.
        """
    )
    return


@app.cell
def _(mo):
    num_a = mo.ui.slider(start=1, stop=20, value=10, label="a")
    num_b = mo.ui.slider(start=1, stop=10, value=3, label="b")
    mo.vstack([num_a, num_b])
    return (num_a, num_b)


@app.cell
def _(mo, num_a, num_b):
    a = num_a.value
    b = num_b.value
    mo.md(
        f"""
        | Operation | Expression | Result | Note |
        |-----------|-----------|--------|------|
        | Addition | `{a} + {b}` | **{a + b}** | |
        | Subtraction | `{a} - {b}` | **{a - b}** | |
        | Multiplication | `{a} * {b}` | **{a * b}** | |
        | Division | `{a} / {b}` | **{a / b:.4f}** | always float |
        | Floor division | `{a} // {b}` | **{a // b}** | rounds down |
        | Remainder | `{a} % {b}` | **{a % b}** | |
        | Power | `{a} ** {b}` | **{a ** b}** | |

        **int + float → float:** `{a} + 0.5 = {a + 0.5}` — Python promotes automatically.
        """
    )
    return


# ── Type conversion ────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Type conversion

        You can convert between types using `int()`, `float()`, `str()`, and `bool()`.
        This is called **type conversion** (or *casting*).

        | Function | Converts to | Example |
        |----------|------------|---------|
        | `int(x)` | Whole number | `int("42")` → `42` |
        | `float(x)` | Decimal | `float(20)` → `20.0` |
        | `str(x)` | Text | `str(42)` → `"42"` |

        ### Why does it matter?

        Imagine you count your personal savings as a whole number — `20` — but you want
        to calculate interest. Interest rates are decimals, so you need a **float**.
        Use the slider to see how the conversion works.
        """
    )
    return


@app.cell
def _(mo):
    savings_input = mo.ui.slider(start=0, stop=1000, value=20, step=5, label="Savings (€)")
    savings_input
    return (savings_input,)


@app.cell
def _(mo, savings_input):
    savings_int   = savings_input.value           # int
    savings_float = float(savings_int)            # float
    rate          = 0.035                         # 3.5% annual interest
    interest      = savings_float * rate
    balance       = savings_float + interest

    mo.md(
        f"""
        | Step | Value | Type |
        |------|-------|------|
        | Your savings | `{savings_int}` | `int` |
        | As float | `{savings_float}` | `float` |
        | Interest at 3.5% | `{interest:.4f}` | `float` |
        | Balance after 1 year | **€{balance:.2f}** | `float` |

        Converting to `float` is important here — `int` cannot represent cents (e.g. `€{interest:.2f}`).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Converting strings to numbers

        `input()` always returns a **string** — even if the user types a number.
        You must convert it before you can do arithmetic.
        """
    )
    return


@app.cell
def _():
    text_number = "42"                # str — looks like a number but is text
    as_int      = int(text_number)    # → 42  (int)
    as_float    = float(text_number)  # → 42.0 (float)

    print(f'"42" → int   : {as_int}    type: {type(as_int).__name__}')
    print(f'"42" → float : {as_float}  type: {type(as_float).__name__}')
    print(f'int × 2      : {as_int * 2}    ← arithmetic works now')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### The truncation trap

        `int()` does **not** round — it **drops** the decimal part entirely.
        """
    )
    return


@app.cell
def _():
    print(f"int(3.9)  = {int(3.9)}   ← drops .9, does NOT round up")
    print(f"int(3.1)  = {int(3.1)}   ← same")
    print(f"int(-3.9) = {int(-3.9)}  ← rounds towards zero, not down!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### What if the conversion is impossible?

        `int("hello")` crashes with a **ValueError** — Python cannot turn
        the word "hello" into a number. Try uncommenting the line in the cell
        below to see the error message.
        """
    )
    return


@app.cell
def _():
    # int("hello world")   ← uncomment this line to see the ValueError
    print("Conversion only works when the value actually makes sense as that type.")
    return


# ── f-strings ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## f-strings

        An **f-string** lets you embed variables and expressions directly inside text.
        Put `f` before the opening quote and wrap anything you want inserted in `{}`.

        ```python
        price = 9.99
        print(f"Price: €{price:.2f}")   # :.2f → two decimal places
        ```
        """
    )
    return


@app.cell
def _(mo):
    product_input = mo.ui.text(value="laptop", label="Product name")
    price_input2  = mo.ui.number(value=999.0, start=0.01, stop=9999.99, step=0.01, label="Price (€)")
    stock_input   = mo.ui.number(value=14, start=0, stop=999, label="Units in stock")
    mo.vstack([product_input, price_input2, stock_input])
    return (price_input2, product_input, stock_input)


@app.cell
def _(mo, price_input2, product_input, stock_input):
    product = product_input.value or "item"
    price   = price_input2.value
    stock   = int(stock_input.value)
    mo.md(
        f"""
        ```
        Product : {product}
        Price   : €{price:.2f}
        In stock: {stock} units
        Total value: €{price * stock:,.2f}
        ```
        """
    )
    return


# ── Naming conventions ────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Naming conventions

        Good names make code readable — for you and for everyone else.
        Python follows **PEP 8**:

        | Style | When to use | Example |
        |-------|-------------|---------|
        | `snake_case` | Variables and functions | `user_age`, `full_name` |
        | `UPPER_SNAKE_CASE` | Constants (never change) | `TAX_RATE`, `MAX_SPEED` |
        | `PascalCase` | Class names (Week 8) | `UserProfile` |

        - ✅ `user_age` — clear, descriptive
        - ✅ `is_active` — booleans often start with `is_` or `has_`
        - ✅ `TAX_RATE` — constant, never reassigned
        - ❌ `a`, `x`, `tmp` — too short or vague
        - ❌ `userAge` — camelCase (JavaScript, not Python)

        > A good name is one you can read six months later and still understand.
        """
    )
    return


# ── Personal profile ──────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## A realistic example — personal profile

        Every value lives in a well-named variable.
        Python calculates **age automatically** from the birthdate — change the
        `birthdate` line to your own and run the cell.
        """
    )
    return


@app.cell
def _():
    from datetime import date

    full_name      = "Sam de Vries"      # str
    birthdate      = date(1998, 6, 15)   # ← change to your own birthdate!
    height_cm      = 182.5               # float
    weight_kg      = 78.0                # float
    favourite_food = "stroopwafel"       # str
    has_siblings   = True                # bool

    today     = date.today()
    age_years = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )

    print(
        f"Name     : {full_name}\n"
        f"Age      : {age_years} years  (born {birthdate})\n"
        f"Height   : {height_cm} cm\n"
        f"Weight   : {weight_kg} kg\n"
        f"Food     : {favourite_food}\n"
        f"Siblings : {has_siblings}"
    )
    return


# ── Debugging ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `print()` for debugging

        When something is not working, `print()` is the fastest way to check
        what value a variable actually holds at that point in the program.
        """
    )
    return


@app.cell
def _():
    total_price     = 100
    discount_pct    = 0.15      # 15%
    discount_amount = total_price * discount_pct
    final_price     = total_price - discount_amount

    print(f"total_price     = {total_price}")
    print(f"discount_pct    = {discount_pct}")
    print(f"discount_amount = {discount_amount}")
    print(f"final_price     = {final_price}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        This week you learned:

        - **Comments** — `#` lines ignored by Python, notes for humans
        - **`print()`** — show text, numbers, results, blank lines
        - **`\n`** — start a new line inside a string
        - **Variable types** — `str`, `int`, `float`, `bool`
        - **Operations** — `+` and `*` on strings vs numbers, all arithmetic operators
        - **Type conversion** — `int()`, `float()`, `str()` and why it matters
        - **f-strings** — embed values directly inside text
        - **Naming conventions** — `snake_case`, `UPPER_SNAKE_CASE`

        Head to the `assignments/` folder when you are ready to practise on your own. 💪
        """
    )
    return


if __name__ == "__main__":
    app.run()
