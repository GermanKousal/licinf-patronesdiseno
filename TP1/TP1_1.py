from abc import ABC, abstractmethod


class Orden(ABC):

    @abstractmethod
    def ordenar(self, arreglo_a_ordenar):
        pass



class OrdenAscendente(Orden):

    def ordenar(self, arreglo_a_ordenar):
        
        n = len(arreglo_a_ordenar)

        for i in range(n):
            for j in range (n - 1):
                if arreglo_a_ordenar[j] > arreglo_a_ordenar[j+1]:
                    aux = arreglo_a_ordenar[j]
                    arreglo_a_ordenar[j] = arreglo_a_ordenar[j+1]
                    arreglo_a_ordenar[j+1] = aux



class OrdenDescendente(Orden):

    def ordenar(self, arreglo_a_ordenar):
        
        n = len(arreglo_a_ordenar)

        for i in range(n):
            for j in range (n - 1):
                if arreglo_a_ordenar[j] < arreglo_a_ordenar[j+1]:
                    aux = arreglo_a_ordenar[j]
                    arreglo_a_ordenar[j] = arreglo_a_ordenar[j+1]
                    arreglo_a_ordenar[j+1] = aux



def main():
    arreglo = [2,5,8,1,0,21]

    ordenar = OrdenAscendente()
    ordenar.ordenar(arreglo)
    print(arreglo)

    ordenar = OrdenDescendente()
    ordenar.ordenar(arreglo)
    print(arreglo)

main()
