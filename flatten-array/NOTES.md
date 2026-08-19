---

## What I Learned & Notes

* **Recursion on Nested Structures:** Handled arbitrary depth by recursively calling `flatten()` when encountering a `list`.
* **`extend` vs. `append`:** 
  * `.append()` inserts the element as-is (including whole lists).
  * `.extend()` unpacks the iterable and adds elements individually.
* **Memory Efficiency (Generators vs. Lists):** Analyzed `yield` ($O(d)$ space) vs. accumulating lists in memory ($O(n)$ space).
* **Type Hints & Docstrings:** Applied Python 3.9+ native type hints (`list`) and reStructuredText docstrings.