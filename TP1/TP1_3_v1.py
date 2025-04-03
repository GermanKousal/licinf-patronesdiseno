from __future__ import annotations
from abc import ABC, abstractmethod


class Conexion:

    __INSTANCIA_UNICA: Conexion | None = None

    def __init__(self, nombre_servidor: str, nombre_usuario: str, contrasenha: str, nombre_DB: str) -> None:

        # Instance Attributes

        self.__nombre_servidor: str = nombre_servidor
        self.__nombre_usuario: str = nombre_usuario
        self.__contrasenha: str = contrasenha
        self.__nombre_DB: str = nombre_DB

    # Methods

    def create(self) -> None:
        pass

    def read(self) -> None:
        pass

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass


def main() -> None:
    conexion = Conexion("Servidor K", "German", "123", "Canciones")


if __name__ == "__main__":
    main()
