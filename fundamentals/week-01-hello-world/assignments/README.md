# Week 01 — Assignment

Your setup is working — now make the program your own!
Open `scripts/hello_world.py` and complete the tasks below.

---

## Task 1 — Personalise the greeting

Change the text returned by `greet()` to something more creative.

For example, instead of `"Hello, {name}! 🎉"` you could write:

```python
return f"Hey {name}, so happy you're here!"
```

Run the script after your change to make sure it still works:

```sh
python scripts/hello_world.py
```

---

## Task 2 — Add a farewell function

Add a second function called `farewell` that returns a short goodbye message.
Then call it in the `if __name__ == "__main__"` block, after the greeting.

Here is a starting point:

```python
def farewell(name: str) -> str:
    return f"Goodbye, {name} — see you soon!"
```

---

## Stretch goal (optional) ⭐

Add your favourite emoji somewhere in the greeting or farewell output.
There are no rules — make it fun!

---

## Hints

- You only need functions — no classes required.
- Use only built-in Python — no extra imports needed.
- Run your script after every change so you can see the result straight away.
- When you are happy with your changes, commit them with a short, clear message,
  for example: `"Week 01: personalised greeting and added farewell"`.
