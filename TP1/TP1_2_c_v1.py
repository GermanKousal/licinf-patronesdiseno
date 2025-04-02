from __future__ import annotations
from abc import ABC, abstractmethod

"""
Resumen del ejercicio:

Este ejercicio consistió en modelar un sistema de carrito de compras con
diferentes estados aplicando principios de diseño SOLID, KISS, DRY y YAGNI.

Principales desafíos y soluciones:

1. **Encapsulación y Delegación de Responsabilidad (Single Responsibility - SRP)**
   - Se creó una clase abstracta `Estado` que define el comportamiento de los estados del carrito.
   - Cada estado (`Activado`, `Cancelado`, `Pagado`, `Archivado`) encapsula su propia lógica de negocio.
   - Esto evita una clase `Carrito` con múltiples condicionales, reduciendo su responsabilidad.

2. **Cumplimiento del Principio Abierto/Cerrado (OCP)**
   - La adición del estado `Archivado` demostró la capacidad del sistema para extenderse sin modificar `Carrito`.
   - Sin embargo, cada vez que se agrega un nuevo estado, es necesario modificar todas las subclases de `Estado`
     para incluir los nuevos métodos, lo que puede ser mejorado en una futura refactorización.

3. **Principio de Sustitución de Liskov (LSP)**
   - Todas las subclases de `Estado` pueden reemplazar a `Estado` sin afectar el funcionamiento del sistema.

4. **Principio de Inversión de Dependencias (DIP)**
   - `Carrito` no depende de implementaciones concretas de los estados, sino de la abstracción `Estado`.
   - Los estados concretos se asignan a través de constantes de clase (`Carrito.ESTADO_ACTIVADO`, etc.).

5. **Aplicación del Principio DRY (Don't Repeat Yourself)**
   - Se encapsularon comportamientos repetidos en los métodos de `Estado`.
   - Se utilizó `_estado_actual` para cambiar de estado de forma centralizada.

6. **Principio KISS (Keep It Simple, Stupid)**
   - La implementación evita estructuras de control complejas (`if` anidados) dentro de `Carrito`.
   - Cada estado maneja su propia lógica de manera sencilla y directa.

7. **Principio YAGNI (You Ain’t Gonna Need It)**
   - Inicialmente se mantuvo el sistema sin el estado `Archivado` hasta que fue requerido.
   - No se agregaron métodos o estructuras innecesarias en `Estado` antes de ser necesarias.

### **Posible Mejora Futura**
   - Actualmente, cada vez que se agrega un nuevo método en `Estado`, todas las subclases deben implementarlo.
   - Se podría definir implementaciones genéricas en `Estado` para evitar modificar todas las subclases 
     cuando se agrega un nuevo método, facilitando la extensibilidad del sistema.
"""

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
        carrito._estado_actual = Carrito.ESTADO_ARCHIVADO
        print("Carrito ARCHIVADO")


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
        print("No se puede archivar el carrito: el carrito está CANCELADO.")


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
        print("No se puede archivar el carrito: el carrito está PAGADO.")


class Archivado(Estado):

    # Methods

    def agregar_producto(self, carrito: Carrito, producto: Producto) -> None:
        carrito.activar()
        carrito.agregar_producto(producto)

    def cancelar(self, carrito: Carrito) -> None:
        carrito._productos.clear()
        carrito._estado_actual = Carrito.ESTADO_CANCELADO
        print("Carrito CANCELADO.")

    def pagar(self, carrito: Carrito) -> None:
        carrito.activar()
        carrito.pagar()

    def activar(self, carrito: Carrito) -> None:
        carrito._estado_actual = Carrito.ESTADO_ACTIVADO
        print("Carrito ACTIVADO")

    def archivar(self, carrito: Carrito) -> None:
        print("No se puede activar el carrito: el carrito ya está ARCHIVADO.")


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

    # Agregar productos en estado ACTIVADO
    print("\n--- Agregando productos en estado ACTIVADO ---")
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)

    # Archivar carrito
    print("\n--- Archivando carrito ---")
    carrito.archivar()

    # Intentar agregar un producto en estado ARCHIVADO (debe activarse automáticamente)
    print("\n--- Intentando agregar producto en estado ARCHIVADO ---")
    carrito.agregar_producto(producto3)

    # Intentar pagar en estado ARCHIVADO (debe activarse automáticamente y pagar)
    print("\n--- Intentando pagar en estado ARCHIVADO ---")
    carrito.pagar()

    # Crear un nuevo carrito y cancelarlo
    print("\n--- Creando nuevo carrito y cancelándolo ---")
    carrito_cancelado = Carrito()
    carrito_cancelado.cancelar()

    # Intentar archivar un carrito CANCELADO (debe fallar)
    print("\n--- Intentando archivar carrito CANCELADO ---")
    carrito_cancelado.archivar()

    # Crear otro carrito y pagarlo
    print("\n--- Creando nuevo carrito y pagándolo ---")
    carrito_pagado = Carrito()
    carrito_pagado.agregar_producto(producto1)
    carrito_pagado.pagar()

    # Intentar archivar un carrito PAGADO (debe fallar)
    print("\n--- Intentando archivar carrito PAGADO ---")
    carrito_pagado.archivar()


if __name__ == "__main__":
    main()
