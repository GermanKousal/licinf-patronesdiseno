from __future__ import annotations
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
        self.__nombre_DB: str = "nombre_DB"

    # Methods

    def create(self) -> None:
        pass

    def read(self) -> None:
        pass

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass

    @property
    def nombre_DB(self) -> str:
        return self.__nombre_DB


def main() -> None:
    conexion = Conexion()
    print(conexion.nombre_DB)


if __name__ == "__main__":
    main()
