from __future__ import annotations
from abc import ABC


class Estado(ABC):
    def activar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        print("No se puede activar en este estado.")

    def desactivar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        print("No se puede desactivar en este estado.")

    def configurar(self, caja_fuerte: CajaFuerte, nuevo_PIN: int) -> None:
        print("No se puede configurar en este estado.")

    def _mensaje_cambio_estado(self, desde: str, hacia: str) -> None:
        print(f"{desde} -> {hacia}")
    
    def _validar_PIN(self, caja_fuerte: CajaFuerte, PIN: int) -> bool:
        return True if caja_fuerte._PIN == PIN else False


class Activada(Estado):
    def desactivar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        self._mensaje_cambio_estado("ACTIVADA", "DESACTIVADA")
        caja_fuerte._cambiar_estado(Desactivada())


class Desactivada(Estado):
    def activar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        self._mensaje_cambio_estado("DESACTIVADA", "ACTIVADA")
        caja_fuerte._cambiar_estado(Activada())

    def configurar(self, caja_fuerte: CajaFuerte, nuevo_PIN: int) -> None:
        self._mensaje_cambio_estado("DESACTIVADA", "CONFIGURACION")
        caja_fuerte._cambiar_estado(Configuracion())


class Configuracion(Estado):
    def activar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        self._mensaje_cambio_estado("CONFIGURACION", "ACTIVADA")
        caja_fuerte._cambiar_estado(Activada())

    def desactivar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        self._mensaje_cambio_estado("CONFIGURACION", "DESACTIVADA")
        caja_fuerte._cambiar_estado(Desactivada())


class CajaFuerte:

    def __init__(self, PIN: int = 0) -> None:
        self._estado: Estado = Desactivada()
        self._PIN: int = PIN

    def activar(self, PIN: int) -> None:
        self._estado.activar(self, PIN)

    def desactivar(self, PIN: int) -> None:
        self._estado.desactivar(self, PIN)

    def configurar(self, nuevo_PIN: int) -> None:
        self._estado.configurar(self, nuevo_PIN)

    def _cambiar_estado(self, estado: Estado) -> None:
        self._estado = estado

    def _cambiar_PIN(self, PIN: int) -> None:
        self._PIN = PIN


def main() -> None:
    caja = CajaFuerte()
    print("Hecho.")

if __name__ == "__main__":
    main()
