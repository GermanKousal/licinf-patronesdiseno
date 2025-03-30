from __future__ import annotations
from abc import ABC


class Producto:

    def __init__(self, nombre: str, precio: float) -> None:

        # Instance Attributes

        self.__nombre: str = nombre
        self.__precio: float = precio

    # Methods

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def precio(self) -> float:
        return self.__precio


class Estado(ABC):

    # Methods
    def agregar_producto(self) -> bool:
        return False

    def cancelar(self) -> Estado | None:
        print("El carrito no puede cancelarse en su estado actual.")
        return None

    def pagar(self) -> Estado | None:
        print("El carrito no puede pagarse en su estado actual.")
        return None

    def activar(self) -> Estado | None:
        print("El carrito no puede activarse en su estado actual.")
        return None


class Activo(Estado):

    # Methods
    def agregar_producto(self) -> bool:
        return True

    def cancelar(self):
        pass

    def pagar(self):
        pass


class Cancelado(Estado):

    # Methods
    def agregar_producto(self):
        pass

    def activar(self):
        pass


class Pagado(Estado):
    pass


class Carrito:

    # Class Atributes

    ESTADO_ACTIVO: Activo = Activo()
    ESTADO_CANCELADO: Cancelado = Cancelado()
    ESTADO_PAGADO: Pagado = Pagado()

    def __init__(self) -> None:

        # Instance Attributes

        self.__estado_actual: Estado = Carrito.ESTADO_ACTIVO
        self.__productos: list[Producto] = []

    # Public Methods
    def agregar_producto(self, producto: Producto):
        pass

    def cancelar(self) -> None:
        self.__cambiar_estado(self.__estado_actual.cancelar())

    def pagar(self) -> None:
        self.__cambiar_estado(self.__estado_actual.pagar())

    def activar(self) -> None:
        self.__cambiar_estado(self.__estado_actual.activar())
    
    # Private Methods
    def __cambiar_estado(self, nuevo_estado: Estado | None):
        if nuevo_estado:
            self.__estado_actual = nuevo_estado


def main() -> None:

    carrito: Carrito = Carrito()


if __name__ == "__main__":
    main()
