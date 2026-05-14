#!/usr/bin/env python3
"""Assignment — Grocery Prices

Build a tiny price-list program that uses dictionaries together with
built-in functions, methods, map, filter, and lambda.

Work through the steps one by one — uncomment each block, run the script,
and check the output before moving on.

Run with:
    python "fundamentals/week-06-advanced functions/assignments/grocery_prices.py"
"""


# ── Step 1: Create the grocery dictionary ────────────────────────────────────
# Create a dictionary called `groceries` with at least 5 items.
# Keys are the item names (str), values are the prices in euros (float).
# Example shape:
#   groceries = {"apples": 2.49, "milk": 0.99, "bread": 1.89, ...}

groceries = {}   # ← replace with your own items and prices


# ── Step 2: Print a summary using built-in functions ─────────────────────────
# Print:
#   - the number of items                  → len()
#   - the total of all prices              → sum() on .values()
#   - the cheapest and most expensive      → min() / max() on .values()
# Format the prices to 2 decimal places using :.2f in the f-string.

# print(f"Items     : {len(groceries)}")
# print(f"Total     : €{sum(groceries.values()):.2f}")
# print(f"Cheapest  : €{min(groceries.values()):.2f}")
# print(f"Priciest  : €{max(groceries.values()):.2f}")


# ── Step 3: Loop with .items() ───────────────────────────────────────────────
# Print every item and its price on its own line, like:
#   APPLES   €2.49
# Use the .upper() string method on the name and :.2f for the price.

# for name, price in groceries.items():
#     print(f"{name.upper():10} €{price:.2f}")


# ── Step 4: Modify the dictionary ────────────────────────────────────────────
# - Add a new item ("eggs", for example) with its price.
# - Update the price of one existing item.
# - Remove one item using `del`.
# Print the dictionary after each change.

# groceries["eggs"] = 3.20
# print(f"After add    : {groceries}")
# groceries["bread"] = 2.10
# print(f"After update : {groceries}")
# del groceries["milk"]
# print(f"After delete : {groceries}")


# ── Step 5: filter() + lambda — items under a budget ─────────────────────────
# Use filter() with a lambda to keep only the (name, price) pairs where the
# price is at most 2.00 euro. Hint: filter over groceries.items().
# Print the result as a list of pairs.

# affordable = list(filter(lambda pair: pair[1] <= 2.00, groceries.items()))
# print(f"Under €2.00 : {affordable}")


# ── Step 6: map() + lambda — apply a 10% discount ────────────────────────────
# Use map() with a lambda to make a NEW list of discounted prices
# (each price multiplied by 0.9). Print the original and discounted lists.

# prices            = list(groceries.values())
# discounted_prices = list(map(lambda p: round(p * 0.9, 2), prices))
# print(f"Original    : {prices}")
# print(f"-10% prices : {discounted_prices}")


# ── Step 7: Console input — look up an item ──────────────────────────────────
# Ask the user to type an item name.
# Use `in` to check whether the item is in the dictionary.
# If it is, print the price; otherwise print a friendly "not found" message.

# query = input("Which item do you want the price of? ").lower()
# if query in groceries:
#     print(f"{query} costs €{groceries[query]:.2f}")
# else:
#     print(f"Sorry, '{query}' is not in the list.")
