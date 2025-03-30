from abc import ABC


class Producto:

    def __init__(self, nombre: str, precio: float) -> None:

        # Attributes

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

    def cancelar(self):
        pass

    def pagar(self):
        pass

    def activar(self):
        pass


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

    def __init__(self, estado: Estado) -> None:

        # Attributes

        self.__estado = estado
        self.__productos: list[Producto] = []

    # Methods
    def agregar_producto(self, producto: Producto):
        return False

    def cancelar(self):
        pass

    def pagar(self):
        pass

    def activar(self):
        pass


def main() -> None:

    estado_activo: Activo = Activo()
    estado_cancelado: Cancelado = Cancelado()
    estado_pagado: Pagado = Pagado()

    carrito: Carrito = Carrito(estado_activo)


if __name__ == "__main__":
    main()
