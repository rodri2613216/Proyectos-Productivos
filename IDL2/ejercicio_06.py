"""
Ejercicio 06 - Ahorro anual con depositos variables
====================================================
Objetivo:
    Manejar un acumulador que muestra el saldo PARCIAL en cada iteracion.
    Se simulan 12 meses; cada mes se deposita una cantidad distinta y se
    informa cuanto se lleva ahorrado, mas el total final del año.

Nivel: Intermedio (acumulador con salida parcial)

Ejemplo de uso:
    Entrada: depositos de cada mes (100, 150, 200, ...)
    Salida : saldo acumulado mes a mes y ahorro final de los 12 meses
"""

MESES_DEL_ANIO = 12


def main():
    acumulado = 0

    for mes in range(1, MESES_DEL_ANIO + 1):
        deposito = float(input(f"Deposito del mes {mes}: S/"))
        acumulado += deposito                     # acumulamos
        print(f"  Ahorro acumulado al mes {mes}: S/{acumulado:.2f}")

    print(f"\nAHORRO FINAL DEL AÑO ({MESES_DEL_ANIO} meses): S/{acumulado:.2f}")


if __name__ == "__main__":
    main()
