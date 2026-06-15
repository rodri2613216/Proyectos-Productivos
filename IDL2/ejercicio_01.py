"""
Ejercicio 01 - Total a pagar en una llantera
=============================================
Objetivo:
    Primer contacto con la decision simple if/else: el precio unitario
    depende de la cantidad comprada.

Nivel: Basico (una sola decision binaria)

Reglas: S/150 por llanta si se compran menos de 5; S/120 si se compran 5 o mas.
Ejemplo de uso:
    Entrada: 6 llantas
    Salida : Precio unitario S/120.00 | Total a pagar: S/720.00
"""

PRECIO_MENOS_DE_5 = 150
PRECIO_5_O_MAS = 120


def precio_unitario(cantidad):
    """Devuelve el precio por llanta segun la cantidad comprada."""
    if cantidad < 5:
        return PRECIO_MENOS_DE_5
    return PRECIO_5_O_MAS


def main():
    cantidad = int(input("Cantidad de llantas a comprar: "))

    precio = precio_unitario(cantidad)
    total = cantidad * precio

    print(f"Precio unitario: S/{precio:.2f}")
    print(f"Total a pagar:   S/{total:.2f}")


if __name__ == "__main__":
    main()
