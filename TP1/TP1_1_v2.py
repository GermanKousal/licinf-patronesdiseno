from abc import ABC, abstractmethod
"""
Mejoras aplicadas en esta versión:

1. **Eliminación de Código Repetido (DRY)**
   - Se centralizó la lógica de ordenamiento en la clase base `Orden`.
   - Se evita la duplicación del intercambio de elementos mediante el método privado `__intercambiar`.

2. **Uso de Métodos Abstractos para la Comparación (OCP - SOLID)**
   - Se delega la comparación de elementos a un método protegido `_orden` en cada subclase.
   - Facilita la extensión del código sin modificar la clase base.

3. **Encapsulación y Abstracción (SRP - SOLID)**
   - La clase `Orden` se encarga del proceso general de ordenamiento.
   - Las subclases `OrdenAscendente` y `OrdenDescendente` solo definen su criterio de comparación.

4. **Aplicación del Principio KISS**
   - Se redujo la cantidad de código en las subclases al mover la estructura del algoritmo a la clase base.
   - Se hizo más legible y mantenible el código.

5. **Mejora en la Eficiencia del Algoritmo de Burbuja**
   - Se optimiza `for j in range(n - 1)` a `for j in range(n - i - 1)` para evitar comparaciones innecesarias.

"""

class Orden(ABC):

    # Public:
    def ordenar(self, arreglo):
        
        n = len(arreglo)

        for i in range(n):
            for j in range (n - i - 1):
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