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

    def __init__(self) -> None:
        self.__nombre: str = "Clase Abstracta Estado"

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


class Activado(Estado):

    def __init__(self) -> None:
        self.__nombre: str = "ACTIVADO"
    
    # Methods
    
    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        pass
    
    
    def cancelar(self, carrito: Carrito) -> None:
        pass

    
    def pagar(self, carrito: Carrito) -> None:
        pass

    
    def activar(self, carrito: Carrito) -> None:
        print("No se puede activar el carrito: el carrito ya está activado.")


class Cancelado(Estado):

        
    def __init__(self) -> None:
        self.__nombre: str = "CANCELADO"

    # Methods
    
    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        pass
    
    
    def cancelar(self, carrito: Carrito) -> None:
        pass

    
    def pagar(self, carrito: Carrito) -> None:
        pass

    
    def activar(self, carrito: Carrito) -> None:
        carrito.__estado_actual = Carrito.ESTADO_ACTIVADO
        print("El carrito fue activado.")


class Pagado(Estado):

    def __init__(self) -> None:
        self.__nombre: str = "PAGADO"
    
    # Methods
    
    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        pass
    
    
    def cancelar(self, carrito: Carrito) -> None:
        pass

    
    def pagar(self, carrito: Carrito) -> None:
        pass

    
    def activar(self, carrito: Carrito) -> None:
        print("No se puede activar el carrito: el carrito ya está pagado.")


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
        pass

    def cancelar(self) -> None:
        pass

    def pagar(self) -> None:
        pass

    def activar(self) -> None:
        self.__estado_actual.activar(self)



def main() -> None:

    # Crear productos
    producto1 = Producto("Producto 1", 100.0)
    producto2 = Producto("Producto 2", 200.0)
    producto3 = Producto("Producto 3", 300.0)

    # Crear carrito en estado Activado
    carrito = Carrito()


if __name__ == "__main__":
    main()
