import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Hello, World! 🌍

        Welcome to Week 1 of the CodeMasters Fundamentals Program!

        You are about to run your very first Python program. By the end of this
        notebook you will have made the computer greet you by name — interactively,
        right here in your browser.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## What is Python?

        Python is a programming language — a way of giving instructions to a computer.
        It was designed to be as easy to read as plain English, which makes it a great
        first language to learn.

        When you write Python code, you are writing a recipe. The computer follows the
        recipe step by step, from top to bottom.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## The `print()` function

        The most important tool in a beginner's toolkit is `print()`.
        It tells Python to display something on the screen.

        Run the cell below to see it in action!
        """
    )
    return


@app.cell
def _():
    print("Hello, World!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You just ran your first Python program. 🎉

        `print("Hello, World!")` tells Python:
        > "Show the text `Hello, World!` on the screen."

        The text inside the quotes is called a **string** — programmers use that word
        for any piece of text.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Functions — tiny helpers you can reuse

        A **function** is a small, named block of code that does one job.
        You write it once and can call it as many times as you like.

        Below is a function called `greet`. It takes a name and gives back a
        personalised greeting.
        """
    )
    return


@app.cell
def _():
    def greet(name: str) -> str:
        """Return a friendly greeting for the given name."""
        return f"Hello, {name}! 🎉"

    # Try calling greet right now with a fixed name:
    print(greet("World"))
    return (greet,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Try it yourself — type your name!

        Use the box below to enter your name.
        The greeting will update automatically as you type.
        """
    )
    return


@app.cell
def _(mo):
    name_input = mo.ui.text(placeholder="Type your name here…", label="Your name")
    name_input
    return (name_input,)


@app.cell
def _(greet, mo, name_input):
    # Use the value from the text box; fall back to "there" when it is empty.
    display_name = name_input.value if name_input.value else "there"
    mo.md(f"## {greet(display_name)}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        Amazing work! You have just:

        - Used `print()` to display text
        - Read and called a function (`greet`)
        - Interacted with live Python code in your browser

        When you are ready, head to the `assignments/` folder and make the greeting
        your own. See you in Week 2! 🚀
        """
    )
    return


if __name__ == "__main__":
    app.run()
