# Fraction Class — Python Operator Overloading

A Python class that represents mathematical fractions and supports arithmetic operations using operator overloading.

---

## Features

- Automatic simplification using GCD
- Arithmetic operations: `+`, `-`, `*`, `/`
- Clean string output: `1/3`, `7/18`

---

## How It Works

### Auto-simplification
Every fraction is reduced automatically on creation:
```python
Fraction(2, 4)  # becomes 1/2
Fraction(3, 9)  # becomes 1/3
```


## Operators Implemented

| Operator | Method | Example | Result |
|---|---|---|---|
| `+` | `__add__` | `1/3 + 1/6` | `1/2` |
| `-` | `__sub__` | `1/3 - 1/6` | `1/6` |
| `*` | `__mul__` | `1/3 * 2` | `2/3` |
| `/` | `__truediv__` | `1/6 / 3` | `1/18` |

---

## Division Rules

**Fraction ÷ Fraction** — multiply by the reciprocal:
```
1/3 ÷ 1/6  =  1/3 × 6/1  =  6/3  =  2
```

**Fraction ÷ int** — multiply the denominator:
```
1/6 ÷ 3  =  1/18
```

---

## Requirements

- Python 3.x
- `math` module (built-in)