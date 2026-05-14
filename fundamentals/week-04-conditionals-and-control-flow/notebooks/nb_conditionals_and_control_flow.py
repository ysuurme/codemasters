import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Conditionals and Control Flow 🚦

        Welcome to Week 4 of the CodeMasters Fundamentals Program!

        Until now your programs ran straight from top to bottom. This week
        they learn to **decide** what to do (`if` / `elif` / `else`) and to
        **repeat** work (`while` loops, `break`, `continue`).

        Together these are called **flow control**.

        > `for` loops arrive next week, paired with lists.
        """
    )
    return


# ── Boolean values ───────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Boolean values

        The `bool` type has just **two** values: `True` and `False`.

        - Always capitalised — `true` is a `NameError`.
        - Booleans are how Python answers a yes/no question.

        ```python
        is_raining   = True
        has_umbrella = False
        ```
        """
    )
    return


@app.cell
def _():
    is_raining   = True
    is_sunny     = False
    has_umbrella = True

    print(f"is_raining   = {is_raining}    type: {type(is_raining).__name__}")
    print(f"is_sunny     = {is_sunny}")
    print(f"has_umbrella = {has_umbrella}")
    return (is_raining,)


# ── Comparison operators ─────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Comparison operators

        A **comparison** compares two values and evaluates to `True` or `False`.

        | Operator | Meaning |
        |----------|---------|
        | `==` | equal to |
        | `!=` | not equal to |
        | `<`  | less than |
        | `>`  | greater than |
        | `<=` | less than or equal |
        | `>=` | greater than or equal |

        > **Watch out:** `==` is the comparison; `=` is assignment.
        > `age == 18` asks *"is age the same as 18?"*; `age = 18` *stores* 18.

        Move the slider — every comparison updates live.
        """
    )
    return


@app.cell
def _(mo):
    age_slider = mo.ui.slider(start=0, stop=40, value=19, label="age")
    age_slider
    return (age_slider,)


@app.cell
def _(age_slider, mo):
    age = age_slider.value
    voting_age = 18
    mo.md(
        f"""
        With `age = {age}` and `voting_age = {voting_age}`:

        | Expression | Result |
        |-----------|--------|
        | `age == voting_age` | **{age == voting_age}** |
        | `age != voting_age` | **{age != voting_age}** |
        | `age <  voting_age` | **{age <  voting_age}** |
        | `age >= voting_age` | **{age >= voting_age}** |
        """
    )
    return


# ── Boolean operators ────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Boolean operators: `and`, `or`, `not`

        | A | B | `A and B` | `A or B` |
        |---|---|-----------|----------|
        | `True` | `True` | `True` | `True` |
        | `True` | `False` | `False` | `True` |
        | `False` | `True` | `False` | `True` |
        | `False` | `False` | `False` | `False` |

        | A | `not A` |
        |---|---------|
        | `True` | `False` |
        | `False` | `True` |

        Toggle the switches and watch the live truth table fill in.
        """
    )
    return


@app.cell
def _(mo):
    a_switch = mo.ui.switch(value=True, label="A")
    b_switch = mo.ui.switch(value=False, label="B")
    mo.hstack([a_switch, b_switch])
    return (a_switch, b_switch)


@app.cell
def _(a_switch, b_switch, mo):
    a = a_switch.value
    b = b_switch.value
    mo.md(
        f"""
        | Expression | Result |
        |-----------|--------|
        | `A and B` | **{a and b}** |
        | `A or B`  | **{a or b}** |
        | `not A`   | **{not a}** |
        | `not B`   | **{not b}** |
        | `(A or B) and not (A and B)` (XOR) | **{(a or b) and not (a and b)}** |
        """
    )
    return


# ── Mixing comparisons and boolean ops ───────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Mixing them together

        Comparisons return booleans, so they combine freely with `and` / `or` / `not`.
        Python also lets you write the math-style chain `low < x < high`.

        ```python
        take_jacket = temp_c < 15 or is_raining
        in_b_range  = 60 <= score < 80
        ```
        """
    )
    return


# ── if / else / elif ─────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `if` / `else` / `elif`

        An `if` statement runs its **clause** only when the condition is `True`.
        Add `else` for the otherwise case, and `elif` ("else if") for more options.

        ```python
        if condition:        # ← colon, then…
            do_something()   # ← indented block (the clause)
        ```

        Indentation tells Python which lines belong inside.
        Four spaces is the convention.

        Use the sliders below to try a small umbrella-advisor.
        """
    )
    return


@app.cell
def _(mo):
    temp_slider = mo.ui.slider(start=-5, stop=35, value=8, label="Temperature (°C)")
    rain_switch = mo.ui.switch(value=True, label="Raining?")
    mo.vstack([temp_slider, rain_switch])
    return (rain_switch, temp_slider)


@app.cell
def _(mo, rain_switch, temp_slider):
    temp_c = temp_slider.value
    raining = rain_switch.value
    if raining and temp_c < 10:
        advice = "Cold and wet — coat AND umbrella."
    elif raining:
        advice = "Just rain — grab an umbrella."
    elif temp_c < 10:
        advice = "Cold but dry — wear a coat."
    elif temp_c >= 25:
        advice = "Hot! Sunglasses recommended."
    else:
        advice = "Nothing special needed today."
    mo.md(
        f"""
        - **Temperature:** {temp_c}°C
        - **Raining:** {raining}
        - **Advice:** {advice}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Order matters in `elif` chains

        Python checks the branches top-to-bottom and runs the **first** one that
        matches. So put the **most specific** conditions first — otherwise a
        broader condition will swallow the cases below it.
        """
    )
    return


# ── Truthy / falsy ───────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Truthy and falsy

        In a condition, some non-boolean values count as `True` or `False`.

        **Falsy:** `0`, `0.0`, `""` (empty string), `[]` (empty list), `None`.
        **Truthy:** everything else.

        This makes for tidy checks:

        ```python
        if name:           # same as: if name != ""
            print(f"Hello, {name}!")
        ```
        """
    )
    return


# ── while loop ───────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## `while` loops

        A `while` loop repeats its block **as long as the condition is True**.
        Make sure something inside the loop eventually changes the condition,
        or you create an **infinite loop**.

        ```python
        count = 5
        while count > 0:
            print(count)
            count = count - 1
        ```

        Move the slider — the cell counts down from your value.
        """
    )
    return


@app.cell
def _(mo):
    start_slider = mo.ui.slider(start=1, stop=10, value=5, label="Count down from")
    start_slider
    return (start_slider,)


@app.cell
def _(start_slider):
    count = start_slider.value
    while count > 0:
        print(f"  T-minus {count} ...")
        count = count - 1
    print("  Lift off!")
    return


# ── break ────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### `break` — leave a loop early

        `break` jumps out of the loop immediately. Combined with `while True:`
        you get the classic *"loop forever until I say stop"* pattern.

        ```python
        while True:
            pin = input("PIN: ")
            if pin == "1234":
                break
        ```

        > If a real loop ever gets stuck, press **Ctrl + C** in the terminal to stop it.
        """
    )
    return


# ── continue ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### `continue` — skip the rest of this iteration

        `continue` jumps back to the top of the loop and re-checks the condition,
        skipping the remaining lines of the current iteration.

        Useful when you want to **ignore** certain items.
        """
    )
    return


@app.cell
def _():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    for n in numbers:
        if n % 2 == 1:           # odd → skip
            continue
        print(f"  even: {n}")
    return


# ── Putting it together — guess the secret ───────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Putting it together — guess the secret

        A tiny number game that uses nearly every feature from this week:
        a `while True` loop, an `if/elif/else` chain, comparisons, and a
        `break` to leave the loop cleanly.
        """
    )
    return


@app.cell
def _():
    secret        = 7
    max_attempts  = 4
    demo_guesses  = [3, 10, 7]    # pretending the user types these

    attempt = 0
    while True:
        guess = demo_guesses[attempt]
        attempt = attempt + 1
        print(f"  attempt {attempt}: guess = {guess}")

        if guess == secret:
            print(f"  ✓ correct in {attempt} attempts!")
            break
        elif guess < secret:
            print("    too low")
        else:
            print("    too high")

        if attempt >= max_attempts:
            print(f"  ✗ out of tries — the secret was {secret}")
            break
    return


# ── Summary ──────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        This week you learned:

        - **Boolean values** — `True`, `False` (capitalised)
        - **Comparison operators** — `==` `!=` `<` `>` `<=` `>=`
        - **Boolean operators** — `and`, `or`, `not`, and their truth tables
        - **Mixing comparisons** — `0 < age < 18`, operator precedence
        - **`if` / `else` / `elif`** — branching, and why elif order matters
        - **Truthy / falsy** — tidy conditions like `if name:`
        - **`while` loops** — repeat until a condition becomes False
        - **`break` / `continue`** — leave or skip an iteration

        Head to the `assignments/` folder for a **traffic-light advisor** that
        practises all of this. 🚦

        > Next week: `for` loops and iteration — the natural way to walk a list.
        """
    )
    return


if __name__ == "__main__":
    app.run()
