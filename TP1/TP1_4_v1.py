from __future__ import annotations
from abc import ABC, abstractmethod


class ElementoSistema(ABC):

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @abstractmethod
    def copiar(self) -> ElementoSistema:
        raise NotImplementedError

    @abstractmethod
    def borrar(self):
        raise NotImplementedError

    @abstractmethod
    def renombrar(self, _nuevo_nombre: str):
        raise NotImplementedError

    @abstractmethod
    def abrir(self):
        raise NotImplementedError
    
    @abstractmethod
    def tamaño(self) -> int:
        raise NotImplementedError


class Archivo(ElementoSistema):

    def __init__(self, nombre: str, tamaño: int) -> None:
        self._tamaño: int = tamaño
        super().__init__(nombre)

    def mostrar_tipo(self):
        pass


class Directorio(ElementoSistema):

    def __init__(self, nombre: str, elementos: list[ElementoSistema] | None = None) -> None:
        super().__init__(nombre)

        self._elementos: list[ElementoSistema] | None = elementos


def main() -> None:
    pass


if __name__ == "__main__":
    main()
