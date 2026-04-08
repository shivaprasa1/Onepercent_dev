# Python_Learning

## The Python Interactive Shell (REPL)

This is the **REPL** — Read, Evaluate, Print, Loop.

- **Read** — Python reads what you type
- **Evaluate** — Python executes it
- **Print** — Python shows the result
- **Loop** — Python waits for the next input

The REPL is useful for quick experiments and testing small pieces of code. It is not meant for building applications.

Try this:

```python
>>> 2 + 3
5
>>> "hello"
'hello'
```

To exit the REPL:

```python
>>> exit()
```


---

## print() — Sending Output to the Screen

`print()` is the most basic way to send data from your program to the screen.

```python
print("Hello, World")
```

Output:

```
Hello, World
```

You can print numbers, text, or results of calculations:

```python
print(10)
print(2 + 3)
print("Python is powerful")
```
### repr() — Reveal Hidden Characters

When a string "looks right" but behaves wrong, `repr()` shows what's really inside.

```python
text = "Hello\tWorld\n"

print(text)
# Output:
# Hello	World
#

print(repr(text))
# Output: 'Hello\tWorld\n'
```

Tabs (`\t`) and newlines (`\n`) become visible. Very useful for debugging.


### Quick Reference: All print() Combinations

| What You Want | Code | Output |
|---|---|---|
| Basic output | `print("hello")` | `hello` |
| Multiple values | `print("a", "b", "c")` | `a b c` |
| Custom separator | `print("a", "b", sep="-")` | `a-b` |
| No newline | `print("hi", end="")` | `hi` (no line break) |
| Custom ending | `print("hi", end="!")` | `hi!` |
| Print to file | `print("log", file=f)` | (writes to file) |
| Force instant output | `print("ok", flush=True)` | `ok` (immediately) |
| Empty line | `print()` | (blank line) |
| Visual separator | `print("=" * 30)` | `==============================` |
| Repeat string | `print("Ha" * 3)` | `HaHaHa` |
| Reveal hidden chars | `print(repr(text))` | Shows `\n`, `\t` etc. |

---
