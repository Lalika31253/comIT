
# comIT# 🐍 Python List & Dictionary Methods — Beginner Challenges

## 🎯 What You Will Learn

By completing these exercises you will practice:

- Using the most common **list methods** to manage and manipulate data
- Using the most common **dictionary methods** to store and retrieve data
- Understanding the difference between **in-place** methods and methods that **return new values**
- Writing cleaner, more Pythonic code

---

## 📋 List Methods — 10 Challenges

### Quick Reference

| Method | What it does | Returns |
|---|---|---|
| `append(item)` | Add one item to the end | `None` |
| `extend(list)` | Add all items from another list | `None` |
| `insert(i, item)` | Insert item at position i | `None` |
| `remove(item)` | Remove first occurrence of item | `None` |
| `pop(index)` | Remove and return item at index | removed item |
| `sort()` | Sort list in place | `None` |
| `sorted()` | Return new sorted list | new list |
| `reverse()` | Reverse list in place | `None` |
| `count(item)` | Count occurrences of item | integer |
| `index(item)` | Find index of first occurrence | integer |

---

### Challenge Breakdown

**Challenge 1 — Build Your Grocery List**
- Start with an empty list
- Add `"eggs"`, `"milk"`, `"bread"` one at a time
- Method: `append()`

**Challenge 2 — Merge the Shelves**
- Combine two lists without creating a new one
- Method: `extend()`

**Challenge 3 — VIP Guest**
- Insert `"Diana"` at position 1
- Method: `insert()`

**Challenge 4 — Remove the Duplicate**
- Remove the FIRST occurrence of `7`, keep the second
- Method: `remove()`

**Challenge 5 — Stack Simulation**
- Push 3 items, pop the top 2, print each popped value
- Methods: `append()`, `pop()`

**Challenge 6 — Sort the Scores**
- Sort from highest to lowest
- Method: `sort(reverse=True)`

**Challenge 7 — Alphabetical, but Fair**
- Sort case-insensitively
- Method: `sort(key=str.lower)`

**Challenge 8 — Find & Count**
- Count how many times `"yes"` appears
- Find the index of the first `"no"`
- Methods: `count()`, `index()`

**Challenge 9 — Reverse Without Sorting**
- Reverse the list in place
- Method: `reverse()`

**Challenge 10 — Sort Without Touching the Original**
- Create a new sorted list, keep original unchanged
- Method: `sorted()`

---

## 📖 Dictionary Methods — 10 Challenges

### Quick Reference

| Method | What it does | Returns |
|---|---|---|
| `get(key, default)` | Safe key access | value or default |
| `update(dict)` | Update/add multiple keys | `None` |
| `setdefault(key, val)` | Set key only if missing | value |
| `pop(key)` | Remove and return value | removed value |
| `keys()` | View all keys | view object |
| `values()` | View all values | view object |
| `items()` | View all key-value pairs | view object |
| `dict1 \| dict2` | Merge two dicts (right wins) | new dict |
| `dict.fromkeys(list, val)` | Create dict from list | new dict |
| `sorted(dict.items())` | Sort by key or value | sorted list |

---

### Challenge Breakdown

**Challenge 1 — Build a Profile**
- Create a dict and print each value using `get()`

**Challenge 2 — Safe Access**
- Retrieve a missing key safely with a default value
- Method: `get()`

**Challenge 3 — Update the Record**
- Update and add keys in a single call
- Method: `update()`

**Challenge 4 — Set Only If Missing**
- Set a key only if it doesn't exist yet
- Method: `setdefault()`

**Challenge 5 — Remove and Reuse**
- Remove a key and store its value
- Method: `pop()`

**Challenge 6 — Inspect the Dictionary**
- Print all keys, values, and pairs
- Methods: `keys()`, `values()`, `items()`

**Challenge 7 — Merge Preferences**
- Merge two dicts, right side wins on conflict
- Method: `|` operator

**Challenge 8 — Initialize from a List**
- Create a dict from a list with a default value
- Method: `dict.fromkeys()`

**Challenge 9 — Count Word Frequency**
- Count occurrences of each word
- Method: `get()` inside a loop

**Challenge 10 — Sort by Value**
- Sort a dict from highest to lowest value
- Method: `sorted()` with `key` + `dict()`

---

## ✅ Checklist

**List Methods**
- [ ] `append()` — adds one item
- [ ] `extend()` — merges another list
- [ ] `insert()` — adds at specific position
- [ ] `remove()` — removes first match
- [ ] `pop()` — removes and returns item
- [ ] `sort()` — sorts in place
- [ ] `sorted()` — returns new sorted list
- [ ] `reverse()` — reverses in place
- [ ] `count()` — counts occurrences
- [ ] `index()` — finds first position

**Dictionary Methods**
- [ ] `get()` — safe key access
- [ ] `update()` — add/update multiple keys
- [ ] `setdefault()` — set only if missing
- [ ] `pop()` — remove and return value
- [ ] `keys()` / `values()` / `items()` — view methods
- [ ] `|` operator — merge dicts
- [ ] `dict.fromkeys()` — initialize from list
- [ ] `sorted()` with `items()` — sort by value