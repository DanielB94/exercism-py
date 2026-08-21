# Learned: Difference of Squares

## Sintaxis y Conceptos Clave

* **List / Generator Comprehensions:**
  * Para iterar y aplicar operaciones a cada elemento antes de sumarlos, es más eficiente y limpio usar una expresión generadora:
    `sum(i ** 2 for i in range(1, number + 1))`
  * Evitar aplicar exponentes directamente al objeto `range` o al límite superior (`number`).

* **Inclusión en `range()`:**
  * El límite superior en `range(start, stop)` es exclusivo. Para incluir hasta el número $N$, se debe usar `range(1, N + 1)`.

* **Reutilización de Funciones (DRY):**
  * Cuando un problema pide calcular la diferencia de dos resultados previos, no se necesita recursividad ni reescribir lógica; basta con llamar a las funciones ya creadas y restar sus resultados.

* **Formatos de Docstrings (Google Style & PEP 257):**
  * Los docstrings deben mantener la misma sangría (4 espacios) que el cuerpo interno de la función.
  * Estructura estándar para documentar argumentos y retornos:
    ```python
    """Breve descripción de la función.

    Args:
        param (type): Descripción del parámetro.

    Returns:
        type: Descripción del valor retornado.
    """
    ```