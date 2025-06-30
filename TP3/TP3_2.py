from __future__ import annotations
from abc import ABC, abstractmethod


class Estado(ABC):
    def activar(self):
        print("No se puede activar en este estado.")

    def desactivar(self):
        print("No se puede desactivar en este estado.")

    def configurar(self):
        print("No se puede configurar en este estado.")


class Activada(Estado):
    def desactivar(self):
        ...


class Desactivada(Estado):
    def activar(self):
        ...

    def configurar(self):
        ...


class Configuracion(Estado):
    def activar(self):
        ...

    def desactivar(self):
        ...


class CajaFuerte:

    def __init__(self, PIN: int = 0):
        _estado: Estado = Desactivada()
        _PIN: int = PIN

    def activar(self):
        ...

    def desactivar(self):
        ...

    def configurar(self):
        ...

    def _cambiar_estado(self, estado: Estado):
        _estado = estado

    def _cambiar_PIN(self, PIN: int):
        _PIN = PIN


def main() -> None:
    pass


if __name__ == "__main__":
    main()
