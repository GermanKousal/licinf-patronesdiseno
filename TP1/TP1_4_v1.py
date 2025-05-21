from __future__ import annotations
from abc import ABC, abstractmethod

"""
Resumen del ejercicio: Sistema de Archivos

Se modeló un sistema de archivos compuesto por dos tipos de elementos: Archivo y Directorio.
Ambos heredan de la clase abstracta ElementoSistema, la cual define la interfaz común (copiar, borrar, renombrar, abrir, tamaño)
que permiten operar de manera uniforme sobre cualquier elemento del sistema.

Principios de Diseño Aplicados:

- Abstracción: Se define una interfaz mínima en ElementoSistema que especifica las operaciones esenciales de un elemento.
- Polimorfismo: Tanto Archivo como Directorio implementan los métodos de ElementoSistema, permitiendo que sean tratados de forma homogénea.
- Encapsulamiento: Los atributos internos (como _nombre, _tamaño y _elementos) están protegidos para evitar accesos directos.
- Responsabilidad Única (SRP): Cada clase se ocupa de su propia responsabilidad. Archivo representa y gestiona un archivo individual,
  mientras que Directorio se encarga de contener y gestionar otros elementos.
- Abierto/Cerrado (OCP): El sistema puede extenderse con nuevos tipos de elementos sin modificar la implementación existente.
- DRY: La implementación evita la duplicación, delegando la responsabilidad de copiarse a cada objeto (cada elemento sabe copiarse a sí mismo).
- KISS y YAGNI: La solución se mantiene simple, sin agregar validaciones o complejidades innecesarias, en consonancia con el alcance del problema.

Se garantiza que la copia de un Archivo produce un objeto nuevo con los mismos atributos, y la copia de un Directorio se realiza de forma recursiva,
creando copias profundas de todos sus elementos. Los métodos para agregar y quitar elementos en Directorio permiten modificar de forma controlada el contenido,
respetando el principio de encapsulamiento.

Este diseño permite que el sistema sea extensible, modular y fácil de entender.
"""

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
        self._elementos.clear()

    def renombrar(self, nombre: str) -> None:
        self._nombre = nombre

    def abrir(self) -> None:
        for elemento in self._elementos:
            print(elemento._nombre)

    def tamaño(self) -> int:
        suma: int = 32   # Tamaño de un Directorio vacío

        for elemento in self._elementos:
            suma += elemento.tamaño()

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
    # Crear archivos
    archivo1 = Archivo("documento.txt", 100)
    archivo2 = Archivo("imagen.png", 200)

    # Crear directorio raíz
    raiz = Directorio("raiz")

    # Agregar archivos al directorio raíz
    raiz.agregar(archivo1)
    raiz.agregar(archivo2)

    # Abrir el directorio (listar nombres)
    print("Contenido de raíz:")
    raiz.abrir()  # Debería mostrar documento.txt e imagen.png

    # Mostrar tamaño total del directorio
    print("Tamaño de raíz:", raiz.tamaño())  # 32 + 100 + 200 = 332

    # Copiar el directorio
    copia_raiz = raiz.copiar()
    copia_raiz.renombrar("copia_raiz")

    # Verificar que los archivos copiados son objetos distintos
    print("\nContenido de copia_raiz:")
    copia_raiz.abrir()

    print("Tamaño de copia_raiz:", copia_raiz.tamaño())

    # Renombrar un archivo y abrirlo
    archivo1.renombrar("nuevo_documento.txt")
    archivo1.abrir()

    # Quitar un archivo
    raiz.quitar(archivo1)

    print("\nContenido de raíz después de quitar archivo1:")
    raiz.abrir()

    # Borrar directorio raíz (llama borrar() en cada elemento)
    print("\nBorrando elementos en raíz:")
    raiz.borrar()


if __name__ == "__main__":
    main()
