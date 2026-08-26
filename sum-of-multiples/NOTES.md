# LEARNED.md

## Sum of Multiples

* **Operador de Salto con `range()`:**
  * Se puede usar `range(inicio, limite, salto)` para generar únicamente los múltiplos de un número sin evaluar uno a uno con el operador módulo `%`.

* **Estructura de Set Comprehension:**
  * Sintaxis básica: `{expresion for item in iterable}`. Usa llaves `{}` sin pares `clave: valor`.
  * Elimina duplicados automáticamente antes de procesar o sumar los elementos.

* **Bucles Anidados en Comprehensions:**
  * El orden de ejecución se lee de izquierda a derecha, imitando la estructura de bucles `for` tradicionales:
    ```python
    {sub_item for item in lista for sub_item in range(...)}
    ```

* **Ubicación Eficiente de Filtros `if` (sin `else`):**
  * Para evaluar condiciones específicas por ciclo, el `if` se coloca inmediatamente después del `for` al que aplica.
  * Colocar `if numbers > 0` justo tras el primer `for` evita ejecutar el segundo ciclo `range()` con paso `0` (el cual lanzaría un `ValueError`).

* **Resolución de Errores de Entorno:**
  * Retornos insospechados de `None` al ejecutar `pytest` en la terminal suelen indicar cambios sin guardar en el editor de código.

---

## Diferenciación de Estructuras con Llaves `{}`

* **Set:** `{x for x in iterable}` -> Colección de valores únicos.
* **Diccionario:** `{clave: valor for x in iterable}` -> Colección de pares clave-valor.
* **Excepción de Vacíos:** `{}` crea un diccionario vacío por defecto. Para definir un conjunto vacío se debe llamar a `set()`.