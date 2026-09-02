# Learned: Square Root

## Key Concepts
* Exponents for Roots: En Python, el operador `**` calcula potencias. Elevar un número a 0.5 (o 1/2) es el equivalente matemático directo a calcular su raíz cuadrada, evitando la necesidad de importar librerías externas como `math`.
* Standard Math Avoidance: Resolver operaciones matemáticas básicas usando operadores nativos permite mantener un código ligero sin dependencias externas.

## Implementation
```python
def square_root(number):
    return number ** 0.5