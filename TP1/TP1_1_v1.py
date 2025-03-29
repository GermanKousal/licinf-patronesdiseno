from abc import ABC, abstractmethod

class Orden(ABC):
    @abstractmethod
    def ordenar(self, arreglo):
        pass

class OrdenAscendente(Orden):
    def ordenar(self, arreglo):
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-1):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo

class OrdenDescendente(Orden):
    def ordenar(self, arreglo):
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-1):
                if arreglo[j] < arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo



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