# What I Learned - ETL Exercise (Exercism Python)

### Key Concepts & Syntax

* **Iterating Dictionaries (`dict.items()`):** 
  * Use `.items()` when looping through a dictionary to access both key and value simultaneously (e.g., `for points, letters in legacy_data.items()`).
  * In Python, trying to iterate over a dictionary directly only yields keys, leading to `TypeError` if treated as a collection.

* **Dict Comprehension with Nested Loops:**
  * Syntax for nested comprehensions matches the order of standard nested `for` loops:
    ```python
    {
        key_expr: value_expr
        for outer_item in outer_sequence
        for inner_item in inner_sequence
    }
    ```
  * Keys and values inside dictionary comprehensions are separated by a colon (`key: value`), whereas assignments use `=`.

* **Modern Type Hints (Python 3.9+):**
  * Built-in collections like `dict` and `list` accept type parameters using square brackets `[]` instead of curly braces `{}` (e.g., `dict[int, list[str]]`).
  * Square brackets indicate type parameterization; curly braces are reserved for data literals.

* **Documentation:**
  * Clean Google-style docstrings structure function descriptions, `Args`, and `Returns` clearly for maintainability.