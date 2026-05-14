import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Functions 🧩

        Welcome to Week 5 of the CodeMasters Fundamentals Program!

        This week you learn to **write your own functions** — mini-programs
        with their own inputs (parameters) and outputs (return values).

        You will meet:

        - `def` — defining a function
        - **Parameters** and **arguments**
        - **`return` values** and the special **`None`**
        - **Keyword arguments** (`end=`, `sep=`)
        - **Local vs global scope**
        - **`try` / `except`** for graceful error handling
        """
    )
    return


# ── Defining and calling ─────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Defining and calling

        A `def` statement defines a function. The indented block below it is
        the **body** — code that runs only when the function is **called**.

        ```python
        def hello():
            print("Howdy!")

        hello()    # ← this line actually runs the body
        ```

        Calling once runs the body once. Calling three times runs it three times.
        """
    )
    return


@app.cell
def _():
    def hello():
        print("Howdy!")
        print("Howdy!!!")
        print("Hello there.")

    hello()
    hello()
    return


# ── DRY ─────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Why functions? — DRY

        **DRY = Don't Repeat Yourself.**
        Without a function you would copy-paste the same lines everywhere.
        With a function:

        - shorter code, easier to read
        - fix a bug **once**, in one place
        - re-use the same logic from many spots
        """
    )
    return


# ── Parameters ───────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Parameters and arguments

        A **parameter** is a variable that lives inside the function and
        receives a value when the function is called.
        The value you pass is the **argument**.

        ```python
        def greet(name):       # `name` is the parameter
            print(f"Hello, {name}!")

        greet("Alice")         # "Alice" is the argument
        ```

        Type a name below to call `greet()` live.
        """
    )
    return


@app.cell
def _(mo):
    name_input = mo.ui.text(value="Alice", label="Argument for greet()")
    name_input
    return (name_input,)


@app.cell
def _(name_input):
    def greet(name):
        print(f"Hello, {name}!")

    greet(name_input.value or "stranger")
    return


# ── Return values ────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Return values

        Use `return` to send a value back to the place that called the function.
        The call **evaluates to** that value, exactly like `5 + 3` evaluates to `8`.

        ```python
        def add(a, b):
            return a + b

        total = add(3, 5)        # → 8
        print(add(10, 20) * 2)   # → 60   (use the return inline)
        ```

        Try the sliders below — the cell calls `add(a, b)` for you.
        """
    )
    return


@app.cell
def _(mo):
    a_slider = mo.ui.slider(start=-10, stop=20, value=3, label="a")
    b_slider = mo.ui.slider(start=-10, stop=20, value=5, label="b")
    mo.vstack([a_slider, b_slider])
    return (a_slider, b_slider)


@app.cell
def _(a_slider, b_slider, mo):
    def add(a, b):
        return a + b
    total = add(a_slider.value, b_slider.value)
    mo.md(
        f"""
        `add({a_slider.value}, {b_slider.value})` → **{total}**
        """
    )
    return


# ── Magic 8-Ball ─────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Magic 8-Ball — multiple `return` statements

        A function can have **many** `return` statements; the first one Python
        reaches ends the function.

        Pick a number 1–9 to see which fortune comes back.
        """
    )
    return


@app.cell
def _(mo):
    answer_slider = mo.ui.slider(start=1, stop=9, value=1, label="answer_number")
    answer_slider
    return (answer_slider,)


@app.cell
def _(answer_slider, mo):
    def get_answer(answer_number):
        if answer_number == 1:
            return "It is certain"
        elif answer_number == 2:
            return "It is decidedly so"
        elif answer_number == 3:
            return "Yes"
        elif answer_number == 4:
            return "Reply hazy, try again"
        elif answer_number == 5:
            return "Ask again later"
        elif answer_number == 6:
            return "Concentrate and ask again"
        elif answer_number == 7:
            return "My reply is no"
        elif answer_number == 8:
            return "Outlook not so good"
        elif answer_number == 9:
            return "Very doubtful"

    fortune = get_answer(answer_slider.value)
    mo.md(f"""**Magic 8-Ball ({answer_slider.value})** → *{fortune}*""")
    return


# ── None ─────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `None` — the value that means "no value"

        - A function with **no `return`** silently returns `None`.
        - `print()` itself returns `None` — it only **displays** text.

        ```python
        result = print("hello")
        print(result)           # → None
        print(type(result))     # → <class 'NoneType'>
        ```
        """
    )
    return


# ── Keyword arguments ────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Keyword arguments — `end=` and `sep=`

        Most arguments are passed by **position**. Some optional ones are passed
        by **name** — keyword arguments.

        Two useful ones on `print()`:

        | Keyword | Default | What it does |
        |---------|---------|--------------|
        | `end=`  | `"\n"`  | What to print AFTER the values |
        | `sep=`  | `" "`   | What to put BETWEEN the values |

        Change the separator below to see the effect.
        """
    )
    return


@app.cell
def _(mo):
    sep_input = mo.ui.text(value=", ", label="sep")
    sep_input
    return (sep_input,)


@app.cell
def _(sep_input):
    sep = sep_input.value if sep_input.value is not None else " "
    print("cats", "dogs", "mice", sep=sep)
    return


# ── Scope ────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Local vs global scope

        A **scope** is a container for variables.

        - Variables defined **outside** any function → **global** scope.
        - Variables defined **inside** a function    → **local** scope of that function.

        ### The rules

        1. Code inside a function CAN read global variables.
        2. Code outside a function CANNOT read a function's local variables.
        3. Each function call has its OWN local scope — gone when the function ends.

        ```python
        shop_name = "CodeMasters Café"   # global

        def show_receipt(item, price):
            tax = price * 0.21           # local — only exists inside
            total = price + tax
            print(f"{shop_name}: {item} — €{total:.2f}")

        show_receipt("coffee", 3.00)
        # print(tax)   ← would crash: tax does not exist out here
        ```
        """
    )
    return


@app.cell
def _():
    shop_name = "CodeMasters Café"

    def show_receipt(item, price):
        tax = price * 0.21
        total = price + tax
        print(f"{shop_name}: {item} — €{total:.2f} (incl. 21% tax)")

    show_receipt("coffee", 3.00)
    show_receipt("sandwich", 6.50)
    return


# ── global statement ─────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### The `global` statement

        Assigning to a name inside a function creates a **local** variable,
        even if a global with that name already exists. To modify the global,
        declare it with `global`:

        ```python
        counter = 0

        def increment():
            global counter
            counter = counter + 1
        ```

        Use it sparingly — most of the time it's cleaner to take an argument
        and `return` a value.
        """
    )
    return


# ── try / except ─────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `try` / `except` — handling errors

        When something risky goes wrong (divide by zero, convert "abc" to `int`),
        Python normally **stops** the program with an error.

        Wrap risky code in a `try:` block and react in `except`:

        ```python
        try:
            number = int(user_text)
        except ValueError:
            print("That was not a whole number.")
        ```

        Try typing a non-number below.
        """
    )
    return


@app.cell
def _(mo):
    user_text = mo.ui.text(value="42", label="Type a value to convert to int")
    user_text
    return (user_text,)


@app.cell
def _(mo, user_text):
    raw = user_text.value
    try:
        number = int(raw)
        msg = f"✓ int(`{raw}`) → **{number}**"
    except ValueError:
        msg = f"✗ `{raw}` is not a whole number — would crash without try/except."
    mo.md(msg)
    return


# ── Capstone ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Putting it together — Guess the number

        The full mini-game uses everything from this week.
        Because `input()` blocks inside Marimo, **run the script** to play it live:

        ```sh
        python fundamentals/week-05-functions/scripts/functions.py
        ```

        The notebook only shows the simulated version below.
        """
    )
    return


@app.cell
def _():
    import random

    secret = random.randint(1, 20)
    fake_guesses = [10, 15, 17, 16, secret]   # pretend the user typed these
    print(f"I am thinking of a number between 1 and 20.   (secret = {secret})")

    def feedback(guess, secret):
        if guess < secret:
            return "Too low."
        elif guess > secret:
            return "Too high."
        else:
            return "Got it!"

    for tries, guess in enumerate(fake_guesses, start=1):
        print(f"  guess {tries}: {guess} → {feedback(guess, secret)}")
        if guess == secret:
            print(f"  ✓ Solved in {tries} tries.")
            break
    return


# ── Summary ──────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        This week you learned:

        - **`def`** — define your own functions
        - **Parameters** and **arguments** — pass data IN
        - **`return`** — pass data OUT
        - **`None`** — value-without-a-value
        - **Keyword arguments** — `end=`, `sep=` on `print()`
        - **Local vs global scope** — and the `global` statement
        - **`try` / `except`** — handle errors without crashing

        Head to the `assignments/` folder for the **Collatz sequence**. 🔁
        """
    )
    return


if __name__ == "__main__":
    app.run()
