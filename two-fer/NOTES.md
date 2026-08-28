# Learned: Two-fer

## Key Concepts
* **Default Parameter Values:** Permiten definir un valor predeterminado para los argumentos de una función `def func(param='default'):`. Si no se pasa un valor al llamar la función, Python utiliza el predeterminado automáticamente.
* **f-Strings (Formatted String Literals):** Simplifican la interpolación de variables dentro de cadenas de texto usando la sintaxis `f"Texto {variable}"`.

## Implementation
```python
def two_fer(name='you'):
    return f'One for {name}, one for me.'