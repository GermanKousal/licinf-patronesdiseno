from __future__ import annotations
from abc import ABC, abstractmethod


class ElementoSistema(ABC):

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @abstractmethod
    def copiar(self) -> ElementoSistema:
        raise NotImplementedError

    @abstractmethod
    def borrar(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def renombrar(self, _nuevo_nombre: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def abrir(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def tamaño(self) -> int:
        raise NotImplementedError


class Archivo(ElementoSistema):

    def __init__(self, nombre: str, tamaño: int) -> None:
        self._tamaño: int = tamaño
        self._extension: str = nombre.split(".")[-1]
        super().__init__(nombre)

    def copiar(self) -> Archivo:
        # Impementar adecuadamente!
        return Archivo("", 0)

    def borrar(self) -> None:
        pass

    def renombrar(self, _nuevo_nombre: str) -> None:
        pass

    def abrir(self) -> None:
        pass

    def tamaño(self) -> int:
        return self._tamaño


class Directorio(ElementoSistema):

    def __init__(self, nombre: str, elementos: list[ElementoSistema] | None = None) -> None:
        super().__init__(nombre)

        self._elementos: list[ElementoSistema] = elementos if elementos is not None else []

    def copiar(self) -> Directorio:
        # Impementar adecuadamente!
        return Directorio("")

    def borrar(self) -> None:
        pass

    def renombrar(self, _nuevo_nombre: str) -> None:
        pass

    def abrir(self) -> None:
        pass

    def tamaño(self) -> int:
        # Implementar adecuadamente!
        return 32

    def agregar(self, elemento: ElementoSistema) -> None:
        pass

    def quitar(self, elemento: ElementoSistema) -> None:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
