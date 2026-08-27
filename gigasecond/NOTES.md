# Gigasecond - Learnings

## Overview
This exercise focuses on performing date and time arithmetic in Python using the built-in `datetime` module.

## Key Concepts

### 1. `datetime.datetime` vs `datetime.timedelta`
* **`datetime.datetime`**: Represents a specific point in time (year, month, day, hour, minute, second).
* **`datetime.timedelta`**: Represents a duration or the difference between two dates/times.

### 2. Date Arithmetic
* Adding a `timedelta` to a `datetime` object automatically handles all calendar transitions (leap years, month-end days, rollover of hours/minutes/seconds) without needing manual calculations.
* Formula: `resulting_datetime = initial_datetime + timedelta(seconds=1_000_000_000)`

### 3. Python Clean Code Tips
* **Type Hints**: Use `datetime` as the type hint for parameters and return types that include both date and time components.
* **Large Numbers**: Using underscores (`1_000_000_000`) or scientific notation exponentiation (`10**9`) improves readability for large numeric literals like a gigasecond.