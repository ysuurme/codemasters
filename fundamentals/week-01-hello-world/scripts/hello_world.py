#!/usr/bin/env python3
"""Minimal hello world script for beginners.

This script defines a single `greet` function, asks the user for their name,
and prints the returned greeting. It's intentionally tiny so it is easy to read.
"""

def greet(name: str) -> str:
    """Return a friendly greeting for `name`.

    Keep this function tiny and clear for beginners.
    """
    if not name:
        name = "there"
    return f"Hello, {name}! 🎉"


if __name__ == "__main__":
    # Ask the participant for their name using the built-in input().
    user_name = input("What's your name? ")
    # Call the small greet function and print the result.
    print(greet(user_name))
