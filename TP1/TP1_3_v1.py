from __future__ import annotations

"""
Clase Conexion: Garantiza una única instancia activa para optimizar el uso de recursos en la gestión de la base de datos.

Aplicación de principios de diseño:

- **SRP (Responsabilidad Única - SOLID)**: La clase se encarga exclusivamente de manejar la conexión.
- **DRY (No te repitas)**: Se centraliza la instancia en un atributo de clase, evitando código redundante.
- **KISS (Mantenlo simple)**: Se usa `__new__` para controlar la instancia sin agregar lógica innecesaria.
- **YAGNI (No agregar funcionalidades innecesarias)**: Solo se implementan los métodos CRUD esenciales.

La instancia se crea solo una vez y se reutiliza en cada nueva solicitud. Se evita la reinicialización con `_inicializado`.  
El método `drop()` permite liberar la instancia para crear una nueva si es necesario.
"""


class Conexion:
    """
    Clase que maneja una única conexión a la base de datos.

    Se usa __new__ para garantizar que solo exista una instancia a la vez.
    Además, __init__ verifica con _inicializado para evitar la reinicialización 
    de atributos cada vez que se llame al constructor.
    """

    __INSTANCIA_UNICA: Conexion | None = None

    def __new__(cls):

        if cls.__INSTANCIA_UNICA is None:
            cls.__INSTANCIA_UNICA = super().__new__(cls)

        return cls.__INSTANCIA_UNICA

    def __init__(self) -> None:

        # Instance Attributes
        if not hasattr(self, "_inicializado"):  # Evita reinicialización
            self.__nombre_servidor: str = "nombre_servidor"
            self.__nombre_usuario: str = "nombre_usuario"
            self.__contrasenha: str = "contrasenha"
            self.__nombre_DB: str = "nombre_DB"
            self._inicializado: bool = True  # Marca que ya se inicializó

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

    def drop(self) -> None:
        Conexion.__INSTANCIA_UNICA = None


def main() -> None:
    conexion1 = Conexion()
    print(id(conexion1), conexion1.nombre_DB)

    conexion2 = Conexion()
    print(id(conexion2), conexion2.nombre_DB)  # Misma instancia

    conexion1.drop()

    conexion3 = Conexion()
    print(id(conexion3), conexion3.nombre_DB)  # Nueva instancia


if __name__ == "__main__":
    main()
