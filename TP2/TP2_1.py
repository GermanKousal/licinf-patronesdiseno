from abc import ABC, abstractmethod


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