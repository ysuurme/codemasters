#!/usr/bin/env python3
"""Assignment — Grocery Prices

Build a tiny price-list program using a DICTIONARY together with `for`
loops and the functions you wrote last week.

Work through the steps one by one — uncomment each block, run the script,
and check the output before moving on.

Run with:
    python fundamentals/week-07-dictionaries/assignments/grocery_prices.py
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


# ── Step 5: Filter with a for-loop — items under a budget ────────────────────
# Walk the dictionary with `.items()` and build a NEW dict that contains
# only the (name, price) pairs where the price is at most 2.00 euro.
# Print the result.

# affordable = {}
# for name, price in groceries.items():
#     if price <= 2.00:
#         affordable[name] = price
# print(f"Under €2.00 : {affordable}")


# ── Step 6: Apply a 10 % discount with a function ────────────────────────────
# Write a small function `discount(price, percentage=0.10)` that returns the
# discounted price (rounded to 2 decimals). Then use a for-loop to build a
# NEW dict where every price has the discount applied.

# def discount(price, percentage=0.10):
#     return round(price * (1 - percentage), 2)
#
# discounted = {}
# for name, price in groceries.items():
#     discounted[name] = discount(price)
# print(f"Original   : {groceries}")
# print(f"-10%       : {discounted}")


# ── Step 7: Console input — look up an item ──────────────────────────────────
# Ask the user to type an item name.
# Use `in` to check whether the item is in the dictionary.
# If it is, print the price; otherwise print a friendly "not found" message.

# query = input("Which item do you want the price of? ").lower()
# if query in groceries:
#     print(f"{query} costs €{groceries[query]:.2f}")
# else:
#     print(f"Sorry, '{query}' is not in the list.")


# ── Step 8 (bonus): Count items by price band ────────────────────────────────
# Walk the dictionary and use a small counter dict to track how many items
# fall into each band: "cheap" (< €1.50), "medium" (€1.50–€3.00), and
# "expensive" (> €3.00). Print the counts.

# bands = {"cheap": 0, "medium": 0, "expensive": 0}
# for price in groceries.values():
#     if price < 1.50:
#         bands["cheap"] = bands["cheap"] + 1
#     elif price <= 3.00:
#         bands["medium"] = bands["medium"] + 1
#     else:
#         bands["expensive"] = bands["expensive"] + 1
# print(bands)
