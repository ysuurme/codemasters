"""
CodeMasters — Example Launcher
===============================
Run this file to browse and launch example projects.

    python main.py
"""

import os
import subprocess
import sys


GRADUATION_EXAMPLES_DIR = os.path.join(os.path.dirname(__file__), "graduation-projects", "examples")


def find_examples(base_dir: str) -> list[tuple[str, str]]:
    """Return a list of (display_name, main_py_path) for each example found."""
    examples = []
    if not os.path.isdir(base_dir):
        return examples
    for folder in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder)
        main_py = os.path.join(folder_path, "main.py")
        if os.path.isdir(folder_path) and os.path.isfile(main_py):
            examples.append((folder, main_py))
    return examples


def print_menu(examples: list[tuple[str, str]], graduation: list[tuple[str, str]]) -> None:
    print()
    print("=" * 50)
    print("  Welcome to CodeMasters Examples")
    print("=" * 50)

    print()
    print("  Examples:")
    for i, (name, _) in enumerate(examples, start=1):
        print(f"    {i}. {name}")

    if graduation:
        print()
        print("  Graduation Project Examples:")
        offset = len(examples)
        for i, (name, _) in enumerate(graduation, start=offset + 1):
            print(f"    {i}. {name}")

    print()
    print("  0. Exit")
    print()


def main() -> None:
    examples = find_examples(GRADUATION_EXAMPLES_DIR)
    graduation: list[tuple[str, str]] = []
    all_projects = examples

    if not all_projects:
        print("No examples found yet. Check the graduation-projects/examples/ folder.")
        return

    while True:
        print_menu(examples, graduation)
        choice = input("  Pick a number to run an example: ").strip()

        if choice == "0":
            print("  Goodbye!")
            break

        if not choice.isdigit() or not (1 <= int(choice) <= len(all_projects)):
            print(f"  Please enter a number between 0 and {len(all_projects)}.")
            continue

        name, path = all_projects[int(choice) - 1]
        print()
        print(f"  Running: {name}")
        print("-" * 50)
        subprocess.run([sys.executable, path])
        print("-" * 50)
        input("  Press Enter to return to the menu...")


if __name__ == "__main__":
    main()
