from __future__ import annotations
from abc import ABC, abstractmethod


class Estado(ABC):
    def activar(self, caja_fuerte: CajaFuerte):
        print("No se puede activar en este estado.")

    def desactivar(self, caja_fuerte: CajaFuerte):
        print("No se puede desactivar en este estado.")

    def configurar(self, caja_fuerte: CajaFuerte):
        print("No se puede configurar en este estado.")

    def _mensaje_cambio_estado(self, desde: str, hacia: str):
        print(f"{desde} -> {hacia}")


class Activada(Estado):
    def desactivar(self, caja_fuerte: CajaFuerte):
        self._mensaje_cambio_estado("ACTIVADA", "DESACTIVADA")
        caja_fuerte._cambiar_estado(Desactivada())


class Desactivada(Estado):
    def activar(self, caja_fuerte: CajaFuerte):
        self._mensaje_cambio_estado("DESACTIVADA", "ACTIVADA")
        caja_fuerte._cambiar_estado(Activada())

    def configurar(self, caja_fuerte: CajaFuerte):
        self._mensaje_cambio_estado("DESACTIVADA", "CONFIGURACION")
        caja_fuerte._cambiar_estado(Configuracion())


class Configuracion(Estado):
    def activar(self, caja_fuerte: CajaFuerte):
        self._mensaje_cambio_estado("CONFIGURACION", "ACTIVADA")
        caja_fuerte._cambiar_estado(Activada())

    def desactivar(self, caja_fuerte: CajaFuerte):
        self._mensaje_cambio_estado("CONFIGURACION", "DESACTIVADA")
        caja_fuerte._cambiar_estado(Desactivada())


class CajaFuerte:

    def __init__(self, PIN: int = 0):
        self._estado: Estado = Desactivada()
        self._PIN: int = PIN

    def activar(self):
        self._estado.activar(self)

    def desactivar(self):
        self._estado.desactivar(self)

    def configurar(self):
        self._estado.configurar(self)

    def _cambiar_estado(self, estado: Estado):
        self._estado = estado

    def _cambiar_PIN(self, PIN: int):
        self._PIN = PIN


def main() -> None:
    pass


if __name__ == "__main__":
    main()
