from abc import ABC


class Orden(ABC):

    # Public:
    def ordenar(self, arreglo, orden):
        
        n = len(arreglo)

        for i in range(n):
            for j in range (n - 1):
                match orden:
                    case 'ascendente':
                        if arreglo[j] > arreglo[j+1]:
                            self.__intercambiar(arreglo, j)
                    
                    case 'descendente':
                        if arreglo[j] < arreglo[j+1]:
                            self.__intercambiar(arreglo, j)
    
    # Private:
    def __intercambiar(self, arreglo, j):
        aux = arreglo[j]
        arreglo[j] = arreglo[j+1]
        arreglo[j+1] = aux



class OrdenAscendente(Orden):

    def ordenar(self, arreglo):
        Orden.ordenar(self, arreglo, 'ascendente')



class OrdenDescendente(Orden):
    
    def ordenar(self, arreglo):
        Orden.ordenar(self, arreglo, 'descendente')



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

    ordenar = OrdenAscendente()
    ordenar.ordenar(arreglo)
    print(arreglo)

    ordenar = OrdenDescendente()
    ordenar.ordenar(arreglo)
    print(arreglo)

if __name__ == "__main__":
    main()