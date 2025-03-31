from __future__ import annotations
from abc import ABC, abstractmethod


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
    @abstractmethod
    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        return None
    
    @abstractmethod
    def cancelar(self) -> None:
        return None

    @abstractmethod
    def pagar(self) -> None:
        return None

    @abstractmethod
    def activar(self) -> None:
        return None


class Activado(Estado):

    # Methods
    
    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        return None
    
    
    def cancelar(self) -> None:
        print("El carrito no puede cancelarse en su estado actual.")
        return None

    
    def pagar(self) -> None:
        print("El carrito no puede pagarse en su estado actual.")
        return None

    
    def activar(self) -> None:
        print("El carrito no puede activarse en su estado actual.")
        return None


class Cancelado(Estado):

    # Methods
    
    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        return None
    
    
    def cancelar(self) -> None:
        print("El carrito no puede cancelarse en su estado actual.")
        return None

    
    def pagar(self) -> None:
        print("El carrito no puede pagarse en su estado actual.")
        return None

    
    def activar(self) -> None:
        print("El carrito no puede activarse en su estado actual.")
        return None


class Pagado(Estado):
    # Methods
    
    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        return None
    
    
    def cancelar(self) -> None:
        print("El carrito no puede cancelarse en su estado actual.")
        return None

    
    def pagar(self) -> None:
        print("El carrito no puede pagarse en su estado actual.")
        return None

    
    def activar(self) -> None:
        print("El carrito no puede activarse en su estado actual.")
        return None


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
        self.__estado_actual.agregar_producto(self, producto)

    def cancelar(self) -> None:
        self.__cambiar_estado(self.__estado_actual.cancelar())

    def pagar(self) -> None:
        self.__cambiar_estado(self.__estado_actual.pagar())

    def activar(self) -> None:
        self.__cambiar_estado(self.__estado_actual.activar())

    # Private Methods
    def __cambiar_estado(self, nuevo_estado: Estado | None):
        if nuevo_estado is not None:
            self.__estado_actual = nuevo_estado


def main() -> None:

    # Crear productos
    producto1 = Producto("Producto 1", 100.0)
    producto2 = Producto("Producto 2", 200.0)
    producto3 = Producto("Producto 3", 300.0)

    # Crear carrito en estado Activado
    carrito = Carrito()

    print("\n*** Agregar producto 1 en estado Activado ***")
    carrito.agregar_producto(producto1)  # Debería agregar producto 1

    print("\n*** Cambiar estado a Cancelado y agregar producto 2 ***")
    carrito.cancelar()  # Cambia el estado a Cancelado
    # Debería activar el carrito y luego agregar producto 2
    carrito.agregar_producto(producto2)

    print("\n*** Cambiar estado a Pagado y agregar producto 3 ***")
    carrito.pagar()  # Cambia el estado a Pagado
    # No debería permitir agregar productos
    carrito.agregar_producto(producto3)

    print("\n*** Cambiar estado a Activado y agregar producto 3 ***")
    carrito.activar()  # Cambia el estado a Activado
    carrito.agregar_producto(producto3)  # Debería agregar producto 3


if __name__ == "__main__":
    main()
