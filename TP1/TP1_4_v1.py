from __future__ import annotations
from abc import ABC, abstractmethod


class ElementoSistema(ABC):

    def __init__(self, nombre: str, contenedor: Directorio | None) -> None:
        self._nombre = nombre
        self._contenedor: Directorio | None = contenedor

    def _asignar_contenedor(self, contenedor: Directorio) -> None:
        self._contenedor = contenedor

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

    def __init__(self, nombre: str, tamaño: int, contenedor: Directorio | None = None) -> None:
        super().__init__(nombre, contenedor)
        self._tamaño: int = tamaño
        self._extension: str = nombre.split(".")[-1]

    def copiar(self) -> Archivo:
        return Archivo(self._nombre, self._tamaño)

    def borrar(self) -> None:
        pass

    def renombrar(self, _nuevo_nombre: str) -> None:
        pass

    def abrir(self) -> None:
        pass

    def tamaño(self) -> int:
        return self._tamaño


class Directorio(ElementoSistema):

    def __init__(self, nombre: str, elementos: list[ElementoSistema] | None = None, contenedor: Directorio | None = None) -> None:
        super().__init__(nombre, contenedor)

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
        if elemento not in self._elementos:
            if elemento._contenedor is not None:
                elemento._contenedor.quitar(elemento)
            elemento._asignar_contenedor(self)
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
