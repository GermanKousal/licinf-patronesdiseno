from abc import ABC, abstractmethod


class Orden(ABC):

    @abstractmethod
    def ordenar(self, arreglo_a_ordenar):
        pass


class OrdenAscendente(Orden):

    def ordenar(self, arreglo_a_ordenar):
        arreglo_a_ordenar.sort()

