"""
Ejercicio 06 - Compra con descuento y cambio
=============================================
Objetivo:
    Introducir el calculo de porcentajes (descuento) y el manejo del
    cambio que se devuelve en un pago en efectivo.

Nivel: Intermedio (porcentaje + resta)

Ejemplo de uso:
    Entrada: base = 200, descuento = 10%, paga con 200
    Salida : A pagar S/180.00, cambio S/20.00
"""


def aplicar_descuento(monto_base, porcentaje):
    """Devuelve el monto a pagar tras aplicar el porcentaje de descuento."""
    descuento = monto_base * porcentaje / 100
    return monto_base - descuento


def main():
    base = float(input("Monto base de la compra: "))
    porcentaje = float(input("Porcentaje de descuento (%): "))
    pago = float(input("Con cuanto paga el cliente: "))

    a_pagar = aplicar_descuento(base, porcentaje)
    cambio = pago - a_pagar

    print(f"Monto a pagar: S/{a_pagar:.2f}")
    print(f"Cambio:        S/{cambio:.2f}")


if __name__ == "__main__":
    main()
