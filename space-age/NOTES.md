# Learned - Space Age (Exercism Python Track)

## 1. Organización y Convenciones en Clases
* **Constantes (`PEP 8`):** Las variables que no cambian durante la ejecución (como `EARTH_CONSTANT` o `ORBITALS`) deben ir en mayúsculas sostenidas, incluso cuando están declaradas dentro del cuerpo de una clase.
* **Uso de `self`:** Para acceder a atributos (`self.seconds`) o métodos (`self.age_math()`) de la propia clase, **siempre** se debe anteponer `self.`. De lo contrario, Python genera un `NameError` al buscar una función global.

## 2. Métodos Auxiliares y DRYS (Don't Repeat Yourself)
* En lugar de repetir la fórmula matemática en cada uno de los 8 métodos, es mejor centralizar la lógica en un **método auxiliar interno** (`age_math`).
* Los métodos específicos (`on_earth`, `on_mercury`, etc.) actúan solo como wrappers pasando una clave tipo *string* (`'earth'`, `'mercury'`) al método auxiliar.

## 3. Flujo de Datos y Retornos (`return`)
* Cuando un método interno calcula un valor, **debe retornar** ese resultado hacia el método que lo invocó.
* A su vez, el método llamador (`on_earth`) debe hacer `return self.age_math('earth')` para entregar el resultado final al test o cliente externo. Si falta el `return`, el método devuelve `None`.

## 4. Matemáticas y Jerarquía de Operaciones
* Para calcular el período orbital compuesto en el denominador, es imprescindible agrupar la multiplicación entre paréntesis: 
  $$\text{edad} = \frac{\text{segundos}}{\text{constante\_tierra} \times \text{factor\_orbital}}$$
* Aplicar `round(resultado, 2)` al final para asegurar la precisión a dos decimales requerida por las especificaciones.

## 5. Type Hints (Anotaciones de Tipo)
* **`__init__`**: Parámetros tipados (ej. `seconds: int | float`) y tipo de retorno `-> None`.
* **Métodos numéricos**: Retorno `-> float`.
* **Parámetros en cadenas**: Tipados como `planet: str`.