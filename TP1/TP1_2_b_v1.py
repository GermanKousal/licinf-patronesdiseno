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
    def agregar_producto(self) -> Estado | None:
        return None

    def cancelar(self) -> Estado | None:
        print("El carrito no puede cancelarse en su estado actual.")
        return None

    def pagar(self) -> Estado | None:
        print("El carrito no puede pagarse en su estado actual.")
        return None

    def activar(self) -> Estado | None:
        print("El carrito no puede activarse en su estado actual.")
        return None


class Activado(Estado):

    # Methods
    def agregar_producto(self) -> Activado:
        return Carrito.ESTADO_ACTIVADO

    def cancelar(self) -> Cancelado:
        print("El carrito ha sido Cancelado.")
        return Carrito.ESTADO_CANCELADO

    def pagar(self) -> Pagado:
        print("El carrito ha sido Pagado.")
        return Carrito.ESTADO_PAGADO


class Cancelado(Estado):

    # Methods
    def agregar_producto(self) -> Activado:
        return Carrito.ESTADO_ACTIVADO

    def activar(self) -> Activado:
        print("El carrito ha sido activado.")
        return Carrito.ESTADO_ACTIVADO


class Pagado(Estado):
    pass


class Carrito:

    # Class Atributes

    ESTADO_ACTIVADO: Activado = Activado()
    ESTADO_CANCELADO: Cancelado = Cancelado()
    ESTADO_PAGADO: Pagado = Pagado()

    def __init__(self) -> None:

        # Instance Attributes

        self.__estado_actual: Estado = Carrito.ESTADO_ACTIVADO
        self.__productos: list[Producto] = []

    # Public Methods
    def agregar_producto(self, producto: Producto) -> None:
        nuevo_estado = self.__estado_actual.agregar_producto()

        if nuevo_estado == self.ESTADO_ACTIVADO:
            self.__estado_actual = self.ESTADO_ACTIVADO
            self.__productos.append(producto)
            print(f"Producto: {producto.nombre} agregado.")
        else:
            print("No se puede agregar producto en el estado actual.")



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
