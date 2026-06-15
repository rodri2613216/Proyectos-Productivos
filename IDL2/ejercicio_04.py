"""
Ejercicio 04 - Compra de N camisas con descuento por tramos
============================================================
Objetivo:
    Usar una cadena if/elif/else para seleccionar un descuento segun el
    RANGO (tramo) en el que cae la cantidad comprada.

Nivel: Intermedio (seleccion por rangos)

Reglas: 1 a 4 camisas -> 12.5%; 5 a 8 -> 20%; mas de 8 -> 31.5%.
Nota:   El enunciado no da el precio unitario, asi que se solicita.
Ejemplo de uso:
    Entrada: 6 camisas a S/50
    Salida : Sin descuento S/300.00, descuento (20%) S/60.00, con descuento S/240.00
"""


def porcentaje_descuento(cantidad):
    """Devuelve la fraccion de descuento segun la cantidad de camisas."""
    if 1 <= cantidad <= 4:
        return 0.125
    elif 5 <= cantidad <= 8:
        return 0.20
    else:                       # mas de 8
        return 0.315


def main():
    cantidad = int(input("Numero de camisas: "))
    precio = float(input("Precio por camisa (S/): "))

    subtotal = cantidad * precio
    descuento = porcentaje_descuento(cantidad)
    monto_descuento = subtotal * descuento
    total = subtotal - monto_descuento

    print(f"Compra sin descuento: S/{subtotal:.2f}")
    print(f"Descuento ({descuento * 100:.1f}%): S/{monto_descuento:.2f}")
    print(f"Compra con descuento: S/{total:.2f}")


if __name__ == "__main__":
    main()
