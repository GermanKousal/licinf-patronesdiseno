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
    def renombrar(self, nombre: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def abrir(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def tamaño(self) -> int:
        raise NotImplementedError


class Archivo(ElementoSistema):

    def __init__(self, nombre: str, tamaño: int) -> None:
        super().__init__(nombre)
        self._tamaño: int = tamaño
        self._extension: str = nombre.split(".")[-1]

    def copiar(self) -> Archivo:
        return Archivo(self._nombre, self._tamaño)

    def borrar(self) -> None:
        # Liberar memoria y otras tareas de mantenimiento antes de borrar objeto
        print(f"{self._nombre} fue borrado.")

    def renombrar(self, nombre: str) -> None:
        self._nombre = nombre
        self._extension = nombre.split(".")[-1]

    def abrir(self) -> None:
        print(
            f"Este archivo se abre con un programa que acepte la extension {self._extension}")

    def tamaño(self) -> int:
        return self._tamaño


class Directorio(ElementoSistema):

    def __init__(self, nombre: str, elementos: list[ElementoSistema] | None = None) -> None:
        super().__init__(nombre)

        self._elementos: list[ElementoSistema] = elementos if elementos is not None else [
        ]

    def copiar(self) -> Directorio:
        elementos: list[ElementoSistema] = []

        for elemento in self._elementos:
            elementos.append(elemento.copiar())

        return Directorio(self._nombre, elementos)

    def borrar(self) -> None:
        for elemento in self._elementos:
            elemento.borrar()
            self._elementos.remove(elemento)

    def renombrar(self, nombre: str) -> None:
        self._nombre = nombre

    def abrir(self) -> None:
        for elemento in self._elementos:
            print(elemento._nombre)

    def tamaño(self) -> int:
        suma: int = 32   # Tamaño de un Directorio vacío

        for elemento in self._elementos:
            suma = + elemento.tamaño()

        return suma

    def agregar(self, elemento: ElementoSistema) -> None:
        if elemento not in self._elementos:
            self._elementos.append(elemento)
        else:
            print("El elemento ya se encuentra en el directorio")

    def quitar(self, elemento: ElementoSistema) -> None:
        if elemento in self._elementos:
            self._elementos.remove(elemento)
        else:
            print("El elemento no se encuentra en el directorio")


def main() -> None:
    pass


if __name__ == "__main__":
    main()
