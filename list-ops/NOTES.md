# Learned: List Ops

## Key Concepts

### 1. Functional Accumulation (`foldl` vs `foldr`)
* **`foldl` (Fold Left):** Iterates through the list sequentially from left to right, combining elements using `function(acc, item)`.
* **`foldr` (Fold Right):** Iterates in reverse (e.g., using slicing `list[::-1]`), processing elements from right to left while passing arguments as `function(item, acc)`.

### 2. Concise Iteration & Flattening
* **List Comprehensions:** Provide a clean, Pythonic alternative to `map`, `filter`, and `concat` without invoking built-in functional utilities.
* **Flat Concatenation:** Combining lists with `list1 + list2` produces a single flat list. Wrapping the expression in extra brackets `[list1 + list2]` causes unintended nesting (`[[...]]`).

### 3. Type Hint Pragmatism
* For highly generic functions that operate on arbitrary types and callables, complex type hints (`Callable[[Any, Any], Any]`) often introduce unnecessary boilerplate without adding runtime value. Omitting them keeps higher-order function implementations readable and lightweight.