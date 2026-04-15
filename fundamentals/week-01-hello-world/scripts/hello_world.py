#!/usr/bin/env python3
"""Week 01 — Hello, World!

Run this script to see your first Python program in action.
    python scripts/hello_world.py
"""


def greet(name: str) -> str:
    """Return a personalised greeting for the given name."""
    # If the user didn't type anything, fall back to a friendly default.
    if not name:
        name = "there"
    return f"Hello, {name}! 🎉"


if __name__ == "__main__":
    # Ask the participant to type their name and store it in a variable.
    user_name = input("What is your name? ")

    # Pass the name to our greet function and print what it returns.
    print(greet(user_name))
