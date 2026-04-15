import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Hello World — Week 01

    Welcome to the first notebook. This one introduces basic Python I/O, simple variables, and an interactive exercise for beginners.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learning Objectives

    - Understand how to print text to the console.
    - Assign and use variables.
    - Try a short exercise at the end.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Prerequisites

    You only need a Python interpreter. If running this as a Marimo notebook, press Run on the code cells or use `marimo run filename.py`.
    """)
    return


@app.cell
def _():
    # Print a simple message
    print('Hello, world!')

    # You can change the text above and re-run the cell to see different output.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your Name (editable variable)

    This cell used to prompt with `input()` but some notebook frontends handle interactive prompts unreliably.
    Instead, edit the `user_name` variable in the code cell below to set your name, then run the cell.
    (Tip: replace the placeholder with your own name.)
    """)
    return


@app.cell
def _():
    # Define your name here (edit this value)
    user_name = 'Your Name'
    print('Nice to meet you, ' + user_name + '!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Variables

    Variables let you store values to use later. Below is a short example showing numbers and strings.
    """)
    return


@app.cell
def _(age):
    # Variables example — edit the values below to try different outputs
    greeting = 'Hello'
    example_name = 'Ada'  # change this to your name
    example_age = 25  # change this number to your age
    print(greeting + ', ' + example_name + '!')
    print('In two years you will be', age + 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercises

    1. Modify the print message to include your favorite hobby.
    2. Ask the user for their age and print what year they will turn 100.
    3. (Optional) Combine `input()` and variables to make a short interactive dialog.
    """)
    return


@app.cell
def _():
    # Example solution for exercise 2 (no input).
    # Edit the `age` variable below to your age, then run the cell.
    age = 25
    current_year = 2026
    year_when_100 = current_year + (100 - age)
    print(f'You will turn 100 in the year {year_when_100}.')
    return (age,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    If you finished the exercises, great job! Move on to the Week 02 materials when you're ready.
    """)
    return


if __name__ == "__main__":
    app.run()
