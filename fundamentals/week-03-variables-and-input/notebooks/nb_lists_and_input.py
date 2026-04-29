import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Lists and Console Input 📋

        Welcome to Week 3 of the CodeMasters Fundamentals Program!

        This week you learn about **data structures** — ways to group related
        data together — and how to interact with your program through the terminal.
        """
    )
    return


# ── Data structures concept ────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Why group data?

        Imagine you are carrying 12 eggs. Without a tray you must hold each
        egg separately — 12 items, 12 hands. An **egg tray** is a data structure:
        one container that organises related values together.

        Python's most common data structure is the **list**.

        Without a list — one variable per quiz score:
        ```python
        score_day_1 = 85
        score_day_2 = 92
        score_day_3 = 78
        # ... 27 more lines for a full month
        ```

        With a list — all scores in one variable, ready for calculations:
        ```python
        quiz_scores = [85, 92, 78, 90, 88]
        ```

        Lists also let you apply operations to every item at once — that is why
        they pair naturally with algorithms (sorting, averaging, searching).
        """
    )
    return


# ── Creating lists ─────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating lists

        A list is created with **square brackets** `[]`.
        Elements are separated by commas.
        Python lists can hold any mix of types.
        """
    )
    return


@app.cell
def _():
    groceries   = ["apples", "milk", "bread", "cheese"]   # str
    quiz_scores = [85, 92, 78, 90, 88]                    # int
    prices      = [2.49, 1.89, 3.99, 0.75]               # float
    mixed       = ["hello", 42, 3.14, True]               # mixed

    # A list can contain other lists — useful for grids and egg trays!
    egg_tray = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
    ]

    # Expressions are evaluated when the list is created:
    computed = [1 + 2, "ha" * 3, 10 / 2]

    print("groceries  :", groceries)
    print("scores     :", quiz_scores)
    print("prices     :", prices)
    print("mixed      :", mixed)
    print("egg_tray   :", egg_tray)
    print("computed   :", computed)
    return (groceries, quiz_scores)


# ── Index positions ─────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Index positions

        Every element has a fixed **index** — its position in the list.

        Python uses **0-based indexing**: the first element is at index `0`.
        Think of the index as the *distance from the start*, not the position number.

        ```
        index:    0          1        2         3
                "apples"  "milk"  "bread"  "cheese"
        ```

        Why start at 0? It matches how memory works inside a computer,
        and almost every major language (C, Java, JavaScript, Go) does the same.

        **Negative index** counts from the end — `-1` is always the last element.
        """
    )
    return


@app.cell
def _(mo):
    items = ["apples", "milk", "bread", "cheese", "eggs"]
    index_slider = mo.ui.slider(
        start=-(len(items)),
        stop=len(items) - 1,
        value=0,
        label="Index",
    )
    index_slider
    return (index_slider, items)


@app.cell
def _(index_slider, items, mo):
    idx = index_slider.value
    element = items[idx]
    direction = "from start →" if idx >= 0 else "← from end"
    mo.md(
        f"""
        `items[{idx}]` = **`"{element}"`** &nbsp;&nbsp; *({direction})*

        ```
        index:  {" | ".join(
            f"[{i}]" if i == idx or (idx < 0 and i == len(items) + idx)
            else f" {i} "
            for i in range(len(items))
        )}
        value:  {" | ".join(
            f"**{v}**" if i == idx or (idx < 0 and i == len(items) + idx)
            else f"  {v}  "
            for i, v in enumerate(items)
        )}
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### f-strings + index access

        You can embed a list element directly inside an f-string using `{list[index]}`.
        """
    )
    return


@app.cell
def _():
    days  = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    temps = [12, 14, 11, 9, 13, 15, 10]   # °C, one per day

    print(f"Temperature on {days[0]}: {temps[0]}°C")
    print(f"Temperature on {days[2]}: {temps[2]}°C")
    print(f"Temperature on {days[6]}: {temps[6]}°C  (last day, same as days[-1])")
    return


# ── Modifying elements ─────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Modifying elements

        Assign a new value to a specific index to overwrite that element.

        ```python
        scores[2] = 95   # replaces whatever was at index 2
        ```
        """
    )
    return


@app.cell
def _(quiz_scores):
    scores = quiz_scores[:]         # make a copy so we don't change the original
    print(f"Before : {scores}")
    scores[2] = 95
    print(f"After  : {scores}  ← index 2 updated from 78 → 95")
    return (scores,)


# ── Methods ────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Methods

        A **method** is a function that belongs to a specific type.
        You call it with a dot: `list_name.method_name()`

        Think of it as asking the list to do something for itself.

        | Method | What it does |
        |--------|-------------|
        | `len(lst)` | Returns the number of elements |
        | `lst.append(x)` | Adds `x` to the end |
        | `lst.insert(i, x)` | Inserts `x` at index `i` |
        | `lst.remove(x)` | Removes the first occurrence of `x` |
        | `sorted(lst)` | Returns a new sorted copy |

        Use the input below to add items to a live list.
        """
    )
    return


@app.cell
def _(mo):
    new_item = mo.ui.text(placeholder="type an item…", label="Add to list")
    new_item
    return (new_item,)


@app.cell
def _(mo, new_item):
    basket = ["banana", "apple", "cherry"]
    if new_item.value:
        basket.append(new_item.value)
    mo.md(
        f"""
        **Basket:** `{basket}`

        `len(basket)` = **{len(basket)}**

        `sorted(basket)` = `{sorted(basket)}`
        """
    )
    return


# ── Slicing ────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Slicing

        `list[start:end]` returns a **new list** containing elements from
        index `start` up to (but **not including**) `end`.

        - Omit `start` → begin from index 0
        - Omit `end` → go to the last element (inclusive)
        - Use negative indices freely

        Use the sliders to explore slices of the score list.
        """
    )
    return


@app.cell
def _(mo, scores):
    n = len(scores)
    start_slider = mo.ui.slider(start=0, stop=n - 1, value=1, label="start")
    end_slider   = mo.ui.slider(start=1, stop=n,     value=4, label="end")
    mo.vstack([start_slider, end_slider])
    return (end_slider, n, start_slider)


@app.cell
def _(end_slider, mo, n, scores, start_slider):
    s = start_slider.value
    e = end_slider.value
    sliced = scores[s:e]
    highlighted = [
        f"**{v}**" if s <= i < e else str(v)
        for i, v in enumerate(scores)
    ]
    mo.md(
        f"""
        Full list: `{scores}`

        `scores[{s}:{e}]` → **`{sliced}`**

        *(elements at indices {list(range(s, min(e, n)))} are selected)*
        """
    )
    return


# ── Strings as sequences ────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Strings are sequences too

        A string behaves like a list of individual characters.
        You can use index access and slicing on strings exactly like lists.
        """
    )
    return


@app.cell
def _(mo):
    str_input = mo.ui.text(value="CodeMasters", label="Your word")
    str_index = mo.ui.slider(start=0, stop=10, value=0, label="Index")
    mo.vstack([str_input, str_index])
    return (str_index, str_input)


@app.cell
def _(mo, str_index, str_input):
    w   = str_input.value or "CodeMasters"
    idx = min(str_index.value, len(w) - 1)
    mo.md(
        f"""
        | Operation | Result |
        |-----------|--------|
        | `word[0]` | `"{w[0]}"` |
        | `word[{idx}]` | `"{w[idx]}"` |
        | `word[-1]` | `"{w[-1]}"` |
        | `word[0:4]` | `"{w[0:4]}"` |
        | `word[4:]` | `"{w[4:]}"` |
        | `len(word)` | `{len(w)}` |
        """
    )
    return


# ── Console input ───────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Console input

        `input()` pauses the program and waits for the user to type something.
        It **always returns a string** — convert with `int()` or `float()` when needed.

        ```python
        user_name = input("What is your name? ")
        print(f"Hello, {user_name}!")

        raw_age  = input("How old are you? ")
        user_age = int(raw_age)   # str → int so we can do maths
        print(f"Next year you will be {user_age + 1} years old.")
        ```

        > In the Marimo notebook the terminal is replaced by a text box.
        > Run the **script** (`scripts/lists_and_input.py`) to experience
        > `input()` live in the terminal.

        Try it here with a text box:
        """
    )
    return


@app.cell
def _(mo):
    sim_name = mo.ui.text(placeholder="Type your name…", label="What is your name?")
    sim_age  = mo.ui.number(value=20, start=1, stop=120, label="How old are you?")
    mo.vstack([sim_name, sim_age])
    return (sim_age, sim_name)


@app.cell
def _(mo, sim_age, sim_name):
    name_val = sim_name.value or "there"
    age_val  = int(sim_age.value)
    mo.md(
        f"""
        **Output:**

        Hello, {name_val}!

        Next year you will be {age_val + 1} years old.
        """
    )
    return


# ── Summary ─────────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        This week you learned:

        - **Data structures** — containers that group related values together
        - **Lists** — created with `[]`, can hold any type, including other lists
        - **Index positions** — 0-based, negative indexing with `-1`
        - **f-strings + indexing** — `f"{my_list[2]}"` embeds a list element in text
        - **Modifying elements** — `list[index] = new_value`
        - **Methods** — `len()`, `.append()`, `.insert()`, `.remove()`, `sorted()`
        - **Slicing** — `list[start:end]` returns a new sub-list
        - **Strings as sequences** — index and slice strings just like lists
        - **`input()`** — pause and collect a string from the user

        Head to the `assignments/` folder when you are ready to practise. 💪
        """
    )
    return


if __name__ == "__main__":
    app.run()
