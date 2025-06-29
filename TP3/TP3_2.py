from __future__ import annotations
from abc import ABC, abstractmethod


class Estado(ABC):
    def activar(self):
        print("No se puede activar en este estado.")

    def desactivar(self):
        print("No se puede activar en este estado.")

    def configurar(self):
        print("No se puede activar en este estado.")


class CajaFuerte:
    ...


def main() -> None:
    pass


if __name__ == "__main__":
    main()
