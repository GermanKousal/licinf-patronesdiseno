from __future__ import annotations
from abc import ABC, abstractmethod


class Estado(ABC):
    def activar(self):
        ...

    def desactivar(self):
        ...

    def configurar(self):
        ...


class CajaFuerte:
    ...


def main() -> None:
    pass


if __name__ == "__main__":
    main()
