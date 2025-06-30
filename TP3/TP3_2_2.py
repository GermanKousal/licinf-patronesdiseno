from __future__ import annotations
from abc import ABC

"""
Modelo extendido de Caja Fuerte con control de intentos e incorporación del estado BLOQUEADA.

Este código continúa la implementación anterior del sistema de caja fuerte, basado en el Patrón State.
Se ha agregado una nueva fase al ciclo de vida del sistema:

- BLOQUEADA: si se fallan 3 intentos consecutivos al intentar desactivar una caja en estado ACTIVADA,
  la caja entra automáticamente en estado BLOQUEADA. En este estado solo se permite desactivarla,
  siempre que se ingrese el PIN correcto. Al hacerlo, se retorna al estado DESACTIVADA y se reinicia
  el contador de intentos fallidos.

También se introdujo una lógica de control de intentos en el estado ACTIVADA, donde se lleva la cuenta
de los intentos fallidos de desactivación. Esto refuerza la seguridad del sistema.

El diseño mantiene los principios de bajo acoplamiento y alta cohesión a través del Patrón State.
"""


class Estado(ABC):
    def activar(self, caja_fuerte, PIN): self._accion_invalida("activar")

    def desactivar(self, caja_fuerte, PIN): self._accion_invalida("desactivar")

    def configurar(self, caja_fuerte,
                   nuevo_PIN): self._accion_invalida("configurar")

    def _accion_invalida(self, accion: str):
        print(f"No se puede {accion} en este estado.")

    def _mensaje_cambio_estado(self, desde: str, hacia: str) -> None:
        print(f"{desde} -> {hacia}")

    def _validar_PIN(self, caja_fuerte: CajaFuerte, PIN: int) -> bool:
        return True if caja_fuerte._PIN == PIN else False

    def bloquear(self, caja_fuerte: CajaFuerte):
        self._mensaje_cambio_estado("", "BLOQUEADA")
        caja_fuerte._cambiar_estado(Bloqueada())


class Activada(Estado):
    def desactivar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        if self._validar_PIN(caja_fuerte, PIN):
            caja_fuerte._intentos_fallidos = 0  # Reiniciar contador si es correcto
            self._mensaje_cambio_estado("ACTIVADA", "DESACTIVADA")
            caja_fuerte._cambiar_estado(Desactivada())
        else:
            caja_fuerte._intentos_fallidos += 1
            print(
                f"PIN incorrecto. Intentos fallidos: {caja_fuerte._intentos_fallidos}")
            if caja_fuerte._intentos_fallidos >= 3:
                self._mensaje_cambio_estado("ACTIVADA", "BLOQUEADA")
                caja_fuerte._cambiar_estado(Bloqueada())


class Desactivada(Estado):
    def activar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        if self._validar_PIN(caja_fuerte, PIN):
            self._mensaje_cambio_estado("DESACTIVADA", "ACTIVADA")
            caja_fuerte._cambiar_estado(Activada())
        else:
            print("PIN incorrecto")

    def configurar(self, caja_fuerte: CajaFuerte, nuevo_PIN: int) -> None:
        self._mensaje_cambio_estado("DESACTIVADA", "CONFIGURACION")
        caja_fuerte._cambiar_estado(Configuracion())


class Configuracion(Estado):
    def activar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        if self._validar_PIN(caja_fuerte, PIN):
            self._mensaje_cambio_estado("CONFIGURACION", "ACTIVADA")
            caja_fuerte._cambiar_estado(Activada())
        else:
            print("PIN incorrecto")

    def desactivar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        self._mensaje_cambio_estado("CONFIGURACION", "DESACTIVADA")
        caja_fuerte._cambiar_estado(Desactivada())

    def configurar(self, caja_fuerte: CajaFuerte, nuevo_PIN: int) -> None:
        caja_fuerte._cambiar_PIN(nuevo_PIN)
        print("Nuevo PIN configurado.")


class Bloqueada(Estado):
    def desactivar(self, caja_fuerte: CajaFuerte, PIN: int) -> None:
        if self._validar_PIN(caja_fuerte, PIN):
            self._mensaje_cambio_estado("BLOQUEADA", "DESACTIVADA")
            caja_fuerte._cambiar_estado(Desactivada())
            caja_fuerte._intentos_fallidos = 0  # Resetear el contador
        else:
            print("PIN incorrecto. Caja fuerte permanece BLOQUEADA.")


class CajaFuerte:

    def __init__(self, PIN: int = 0) -> None:
        self._estado: Estado = Desactivada()
        self._PIN: int = PIN
        self._intentos_fallidos: int = 0

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
    caja = CajaFuerte(PIN=1234)

    print("\n--- Intentar activar con PIN incorrecto ---")
    caja.activar(1111)  # PIN incorrecto

    print("\n--- Activar con PIN correcto ---")
    caja.activar(1234)

    print("\n--- Desactivar con PIN incorrecto ---")
    caja.desactivar(9999)

    print("\n--- Desactivar con PIN correcto ---")
    caja.desactivar(1234)

    print("\n--- Configurar nuevo PIN ---")
    caja.configurar(5678)  # Entra a estado Configuracion

    print("\n--- Cambiar el PIN en estado CONFIGURACION ---")
    caja.configurar(5678)

    print("\n--- Activar con PIN antiguo (debería fallar) ---")
    caja.activar(1234)  # PIN antiguo

    print("\n--- Activar con PIN nuevo ---")
    caja.activar(5678)

    print("\n--- Desactivar con PIN nuevo ---")
    caja.desactivar(5678)

    print("\n--- Activar con PIN nuevo ---")
    caja.activar(5678)

    print("\n--- Forzar BLOQUEO ---")
    caja.desactivar(0000)
    caja.desactivar(1111)
    caja.desactivar(2222)

    print("\n--- Intentar desactivar BLOQUEADA con PIN incorrecto ---")
    caja.desactivar(9999)

    print("\n--- Desactivar BLOQUEADA con PIN correcto ---")
    caja.desactivar(5678)


if __name__ == "__main__":
    main()
