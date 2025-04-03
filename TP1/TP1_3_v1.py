from __future__ import annotations
import random
from abc import ABC, abstractmethod


class Conexion:

    __INSTANCIA_UNICA: Conexion | None = None

    def __new__(cls):

        if cls.__INSTANCIA_UNICA is None:
            cls.__INSTANCIA_UNICA = super().__new__(cls)

        return cls.__INSTANCIA_UNICA

    def __init__(self) -> None:

        # Instance Attributes

        self.__nombre_servidor: str = "nombre_servidor"
        self.__nombre_usuario: str = "nombre_usuario"
        self.__contrasenha: str = "contrasenha"
        self.__nombre_DB: str = str(random.getrandbits(32))

    # Methods

    @property
    def nombre_DB(self) -> str:
        return self.__nombre_DB

    def create(self) -> None:
        pass

    def read(self) -> None:
        pass

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass

    def close(self) -> None:
        Conexion.__INSTANCIA_UNICA = None


def main() -> None:
    conexion1 = Conexion()
    print(id(conexion1))

    conexion2 = Conexion()
    print(id(conexion2))

    conexion1.close()

    conexion1 = Conexion()
    print(id(conexion1))

    conexion2 = Conexion()
    print(id(conexion2))


if __name__ == "__main__":
    main()
