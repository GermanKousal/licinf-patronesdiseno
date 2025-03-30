from abc import ABC, abstractmethod


class Producto:

    # Attributes
    __nombre: str = ""
    __precio: float = 0.0

    # Methods

    def __init__(self, nombre: str, precio: float):
        self.__nombre = nombre
        self.__precio = precio

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

    # Attributes
    def __init__(self):
        self.__estado: Estado = Activo()
        self.__productos = [Producto]

    # Methods
    def agregar_producto(self, producto: Producto):
        return False

    def cancelar(self):
        pass

    def pagar(self):
        pass

    def activar(self):
        pass
