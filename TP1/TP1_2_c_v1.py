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
        raise NotImplementedError

    @abstractmethod
    def cancelar(self, carrito: Carrito) -> None:
        raise NotImplementedError

    @abstractmethod
    def pagar(self, carrito: Carrito) -> None:
        raise NotImplementedError

    @abstractmethod
    def activar(self, carrito: Carrito) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def archivar(self, carrito: Carrito) -> None:
        raise NotImplementedError


class Activado(Estado):

    # Methods

    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        carrito._productos.append(producto)
        print(f"Se agregó producto {producto.nombre} por ${producto.precio}")

    def cancelar(self, carrito: Carrito) -> None:
        carrito._productos.clear()
        carrito._estado_actual = Carrito.ESTADO_CANCELADO
        print("Carrito CANCELADO.")

    def pagar(self, carrito: Carrito) -> None:
        total: float = 0.0

        print("--- Lista de productos ---")

        for producto in carrito._productos:
            total += producto.precio
            print(f"{producto.nombre}: ${producto.precio}")

        print("--- --- Fin lista  --- ---")

        print(f"Total a pagar: ${total}")

        carrito._estado_actual = Carrito.ESTADO_PAGADO

        print("Carrito PAGADO.")

    def activar(self, carrito: Carrito) -> None:
        print("No se puede activar el carrito: el carrito ya está ACTIVADO.")

    def archivar(self, carrito: Carrito) -> None:
        pass


class Cancelado(Estado):

    # Methods

    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        carrito.activar()
        carrito.agregar_producto(producto)

    def cancelar(self, carrito: Carrito) -> None:
        print("No se puede cancelar el carrito: el carrito ya está CANCELADO.")

    def pagar(self, carrito: Carrito) -> None:
        print("No se puede pagar el carrito: el carrito está CANCELADO.")

    def activar(self, carrito: Carrito) -> None:
        carrito._estado_actual = Carrito.ESTADO_ACTIVADO
        print("Carrito ACTIVADO")
    
    def archivar(self, carrito: Carrito) -> None:
        pass


class Pagado(Estado):

    # Methods

    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        print("No se pueden agregar mas productos al carrito: el carrito está PAGADO.")

    def cancelar(self, carrito: Carrito) -> None:
        print("No se puede cancelar el carrito: el carrito está PAGADO.")

    def pagar(self, carrito: Carrito) -> None:
        print("No se puede pagar el carrito: el carrito ya está PAGADO.")

    def activar(self, carrito: Carrito) -> None:
        print("No se puede activar el carrito: el carrito está PAGADO.")
    
    def archivar(self, carrito: Carrito) -> None:
        pass


class Archivado(Estado):

    # Methods

    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        #print("No se pueden agregar mas productos al carrito: el carrito está PAGADO.")
        pass

    def cancelar(self, carrito: Carrito) -> None:
        #print("No se puede cancelar el carrito: el carrito está PAGADO.")
        pass

    def pagar(self, carrito: Carrito) -> None:
        #print("No se puede pagar el carrito: el carrito ya está PAGADO.")
        pass

    def activar(self, carrito: Carrito) -> None:
        #print("No se puede activar el carrito: el carrito está PAGADO.")
        pass
    
    def archivar(self, carrito: Carrito) -> None:
        pass


class Carrito:

    # Class Atributes

    ESTADO_ACTIVADO: Activado = Activado()
    ESTADO_CANCELADO: Cancelado = Cancelado()
    ESTADO_PAGADO: Pagado = Pagado()
    ESTADO_ARCHIVADO: Archivado = Archivado()

    def __init__(self) -> None:

        # Instance Attributes

        self._estado_actual: Estado = Carrito.ESTADO_ACTIVADO
        self._productos: list[Producto] = []

    # Public Methods
    def agregar_producto(self, producto: Producto) -> None:
        self._estado_actual.agregar_producto(carrito=self, producto=producto)

    def cancelar(self) -> None:
        self._estado_actual.cancelar(self)

    def pagar(self) -> None:
        self._estado_actual.pagar(self)

    def activar(self) -> None:
        self._estado_actual.activar(self)
    
    def archivar(self) -> None:
        self._estado_actual.archivar(self)


def main() -> None:
    # Crear productos
    producto1 = Producto("Producto 1", 100.0)
    producto2 = Producto("Producto 2", 200.0)
    producto3 = Producto("Producto 3", 300.0)

    # Crear carrito en estado Activado
    carrito = Carrito()

    # Agregar productos en estado Activado
    print("\n--- Agregando productos en estado ACTIVADO ---")
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)

    # Cancelar carrito
    print("\n--- Cancelando carrito ---")
    carrito.cancelar()

    # Intentar agregar un producto en estado Cancelado (debería activarse primero)
    print("\n--- Intentando agregar producto en estado CANCELADO ---")
    carrito.agregar_producto(producto3)

    # Pagar carrito
    print("\n--- Pagando carrito ---")
    carrito.pagar()

    # Intentar agregar producto en estado Pagado (debería fallar)
    print("\n--- Intentando agregar producto en estado PAGADO ---")
    carrito.agregar_producto(producto1)


if __name__ == "__main__":
    main()
