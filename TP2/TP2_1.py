from abc import ABC, abstractmethod
"""
Este módulo implementa el algoritmo de ordenamiento burbuja utilizando el patrón de diseño Template Method.

PATRÓN: Template Method

PROBLEMA:
Queremos reutilizar un algoritmo de ordenamiento (burbuja), permitiendo cambiar el criterio de comparación
(ascendente, descendente, etc.) sin duplicar código ni alterar la estructura del algoritmo.

SOLUCIÓN:
- La clase abstracta `Orden` define el método plantilla `ordenar()`, que implementa el algoritmo burbuja completo.
- Dentro del método `ordenar()`, la decisión de intercambio depende del método abstracto `_orden(m, n)`, que 
  define el criterio de comparación.
- Las subclases (`OrdenAscendente`, `OrdenDescendente`) redefinen el método `_orden()` según el criterio deseado.
- La operación auxiliar `__intercambiar()` está encapsulada para proteger la lógica de intercambio.

CONSECUENCIAS:
- El algoritmo general está centralizado en un solo lugar (`ordenar()`).
- Se evita la duplicación de código entre distintos tipos de orden.
- Es fácil agregar nuevos criterios de comparación sin modificar clases existentes.
- Se encapsula la variabilidad de comportamiento y se protege la estructura general del algoritmo.
- Se controla cómo las subclases extienden la funcionalidad, manteniendo el orden lógico del proceso.

Este diseño maximiza la reutilización de código, respeta principios como el abierto/cerrado (OCP)
y favorece una estructura limpia y extensible.
"""


class Orden(ABC):

    # Public:
    def ordenar(self, arreglo):

        n = len(arreglo)

        for i in range(n):
            for j in range(n - i - 1):
                if self._orden(arreglo[j], arreglo[j+1]):
                    self.__intercambiar(arreglo, j)

    # Protected:
    @abstractmethod
    def _orden(self, m, n):
        pass

    # Private:
    def __intercambiar(self, arreglo, j):
        aux = arreglo[j]
        arreglo[j] = arreglo[j+1]
        arreglo[j+1] = aux


class OrdenAscendente(Orden):

    def _orden(self, m, n):
        return m > n


class OrdenDescendente(Orden):

    def _orden(self, m, n):
        return m < n


def main():

    arreglo = list()

    while True:
        try:
            item = input("Ingrese un numero ('-' para terminar): ").strip()

            if item == "-":
                raise EOFError

            item = int(item)
            arreglo.append(item)

        except KeyError:
            pass

        except ValueError:
            print("Solo se puede ingresar numeros")

        except EOFError:
            break

        else:
            print(f"El arreglo ingresado es: {arreglo}")

    ordenarA = OrdenAscendente()
    ordenarD = OrdenDescendente()

    ordenarA.ordenar(arreglo)
    print(arreglo)

    ordenarD.ordenar(arreglo)
    print(arreglo)


if __name__ == "__main__":
    main()
