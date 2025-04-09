from __future__ import annotations
from abc import ABC, abstractmethod


class ElementoSistema(ABC):

    def __init__(self, nombre: str, tamaño: int) -> None:
        self._nombre = nombre
        self._tamaño: int = tamaño

    def mostrar_nombre(self) -> str:
        return self._nombre

    def obtener_tamaño(self) -> int:
        return self._tamaño

    def copiar(self):
        pass

    def borrar(self):
        pass

    def renombrar(self):
        pass

    def abrir(seld):
        pass


class Archivo(ElementoSistema):

    def __init__(self, nombre, tamaño) -> None:
        super().__init__(nombre, tamaño)

    def mostrar_tipo(self):
        pass


class Directorio(ElementoSistema):

    def __init__(self, nombre, tamaño) -> None:
        tamaño = 32
        super().__init__(nombre, tamaño)

        self._elementos: list[ElementoSistema] | None = None


def main() -> None:
    pass


if __name__ == "__main__":
    main()
