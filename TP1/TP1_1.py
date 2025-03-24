from abc import ABC, abstractmethod


class Orden(ABC):

    @abstractmethod
    def ordenar(self, arreglo_a_ordenar):
        pass


class OrdenAscendente(Orden):

    def ordenar(self, arreglo_a_ordenar):
        print(id(arreglo_a_ordenar))
        arreglo_a_ordenar.sort()




def main():
    arreglo = [2,5,8,1,0,21]

    ordenar = OrdenAscendente()
    print(id(arreglo))
    ordenar.ordenar(arreglo)

    print(arreglo)
    print('tu mama')


main()
