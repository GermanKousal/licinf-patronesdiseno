from __future__ import annotations
from abc import ABC

"""
Modelo de Caja Fuerte utilizando el Patrón State.

Este programa modela el comportamiento de una caja fuerte en un hotel, la cual puede encontrarse en distintos estados: 
- Desactivada
- Activada
- Configuración

El comportamiento de la caja depende de su estado actual. Cada estado permite o restringe ciertas operaciones, y las transiciones entre estados se manejan mediante delegación utilizando el patrón de diseño State.

Características principales:
- La clase `CajaFuerte` delega su comportamiento en un objeto `Estado`, que representa su estado actual.
- Cada estado concreto (`Desactivada`, `Activada`, `Configuracion`) define qué operaciones son válidas y cómo responder.
- Las operaciones de activar y desactivar requieren un PIN, que es validado antes de permitir la transición.
- El PIN puede cambiarse solo en el estado de Configuración.
- Se muestra un mensaje cada vez que la caja cambia de estado, en el formato: "ESTADO_ANTERIOR -> ESTADO_NUEVO".

Principios de diseño aplicados:
- SRP: Cada clase tiene una única responsabilidad.
- OCP: Se pueden agregar nuevos estados sin modificar los existentes.
- DRY: La validación del PIN está centralizada.
- KISS y YAGNI: La implementación es directa y sin lógica innecesaria.

Esta solución es la primera parte del ejercicio, que será extendida para incluir un nuevo estado de Bloqueo.
"""


class Estado(ABC):
    def activar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        print("No se puede activar en este estado.")

    def desactivar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        print("No se puede desactivar en este estado.")

    def configurar(self, caja_fuerte: CajaFuerte, nuevo_PIN: int) -> None:
        print("No se puede configurar en este estado.")

    def _mensaje_cambio_estado(self, desde: str, hacia: str) -> None:
        print(f"{desde} -> {hacia}")

    def _validar_PIN(self, caja_fuerte: CajaFuerte, PIN: int) -> bool:
        return True if caja_fuerte._PIN == PIN else False


class Activada(Estado):
    def desactivar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        if self._validar_PIN(caja_fuerte, PIN):
            self._mensaje_cambio_estado("ACTIVADA", "DESACTIVADA")
            caja_fuerte._cambiar_estado(Desactivada())
        else:
            print("PIN incorrecto")


class Desactivada(Estado):
    def activar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        if self._validar_PIN(caja_fuerte, PIN):
            self._mensaje_cambio_estado("DESACTIVADA", "ACTIVADA")
            caja_fuerte._cambiar_estado(Activada())
        else:
            print("PIN incorrecto")

    def configurar(self, caja_fuerte: CajaFuerte, nuevo_PIN: int) -> None:
        self._mensaje_cambio_estado("DESACTIVADA", "CONFIGURACION")
        caja_fuerte._cambiar_estado(Configuracion())


class Configuracion(Estado):
    def activar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        if self._validar_PIN(caja_fuerte, PIN):
            self._mensaje_cambio_estado("CONFIGURACION", "ACTIVADA")
            caja_fuerte._cambiar_estado(Activada())
        else:
            print("PIN incorrecto")

    def desactivar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        self._mensaje_cambio_estado("CONFIGURACION", "DESACTIVADA")
        caja_fuerte._cambiar_estado(Desactivada())

    def configurar(self, caja_fuerte: CajaFuerte, nuevo_PIN: int) -> None:
        caja_fuerte._cambiar_PIN(nuevo_PIN)
        print("Nuevo PIN configurado.")


class CajaFuerte:

    def __init__(self, PIN: int = 0) -> None:
        self._estado: Estado = Desactivada()
        self._PIN: int = PIN

    def activar(self, PIN: int) -> None:
        self._estado.activar(self, PIN)

    def desactivar(self, PIN: int) -> None:
        self._estado.desactivar(self, PIN)

    def configurar(self, nuevo_PIN: int) -> None:
        self._estado.configurar(self, nuevo_PIN)

    def _cambiar_estado(self, estado: Estado) -> None:
        self._estado = estado

    def _cambiar_PIN(self, PIN: int) -> None:
        self._PIN = PIN


def main() -> None:
    caja = CajaFuerte(PIN=1234)

    print("\n--- Intentar activar con PIN incorrecto ---")
    caja.activar(1111)  # PIN incorrecto

    print("\n--- Activar con PIN correcto ---")
    caja.activar(1234)

    print("\n--- Desactivar con PIN incorrecto ---")
    caja.desactivar(9999)

    print("\n--- Desactivar con PIN correcto ---")
    caja.desactivar(1234)

    print("\n--- Configurar nuevo PIN ---")
    caja.configurar(5678)  # Entra a estado Configuracion

    print("\n--- Cambiar el PIN en estado CONFIGURACION ---")
    caja.configurar(5678)

    print("\n--- Activar con PIN antiguo (debería fallar) ---")
    caja.activar(1234)  # PIN antiguo

    print("\n--- Activar con PIN nuevo ---")
    caja.activar(5678)

    print("\n--- Desactivar con PIN nuevo ---")
    caja.desactivar(5678)


if __name__ == "__main__":
    main()
