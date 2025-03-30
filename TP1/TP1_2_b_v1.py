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

    def cancelar(self) -> None:
        print("El carrito no puede cancelarse en su estado actual.")

    def pagar(self) -> None:
        print("El carrito no puede pagarse en su estado actual.")

    def activar(self) -> None:
        print("El carrito no puede activarse en su estado actual.")


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

    carrito: Carrito = Carrito()


if __name__ == "__main__":
    main()
