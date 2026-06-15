"""
Ejercicio 07 - Sueldo del vendedor con comision
================================================
Objetivo:
    Calcular un porcentaje (comision) sobre la SUMA de varias ventas y
    sumarlo a un sueldo base. Se practica acumular valores en una lista.

Nivel: Intermedio-Avanzado

Comision: 25% sobre el total de ventas.
Ejemplo de uso:
    Entrada: base = 1200, ventas = 2000, 1500, 2500
    Salida : Comisiones S/1500.00, Total S/2700.00
"""

PORCENTAJE_COMISION = 0.25  # 25%


def calcular_comision(ventas):
    """Comision del 25% sobre el total de las ventas."""
    return sum(ventas) * PORCENTAJE_COMISION


def main():
    base = float(input("Sueldo base: "))

    # El vendedor realiza 3 ventas en el mes
    ventas = []
    for numero in range(1, 4):
        venta = float(input(f"Monto de la venta {numero}: "))
        ventas.append(venta)

    comision = calcular_comision(ventas)
    total = base + comision

    print(f"Comisiones del mes: S/{comision:.2f}")
    print(f"Total a recibir:    S/{total:.2f}")


if __name__ == "__main__":
    main()
