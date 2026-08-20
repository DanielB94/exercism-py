# Notes - Line Up

* **Guard Clause Pattern:** Special two-digit cases (11th, 12th, 13th) must be evaluated first to override standard single-digit ordinal rules.
* **Tuple Membership Check:** Checking `number % 100 in (11, 12, 13)` is cleaner and more explicit than using ranges or multiple `elif` conditions.
* **Dictionary `.get()` Method:** Used `.get(key, default)` on a dictionary to map single-digit remainders (`number % 10`) to suffixes (`'st'`, `'nd'`, `'rd'`) while providing `'th'` as a fallback value for all other cases.
* **Expression Assignment:** Evaluating dictionary lookups inline simplifies the flow, removing redundant variable re-assignments across multiple conditional branches.
* **Type Annotations:** Applied Python 3.9+ type hints (`name: str, number: int -> str`) to functions and internal variables for better code clarity.