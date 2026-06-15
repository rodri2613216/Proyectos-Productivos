"""
Ejercicio 02 - Tributacion de impuestos
========================================
Objetivo:
    Introducir la condicion COMPUESTA con el operador logico 'and': se
    deben cumplir dos requisitos a la vez para tributar.

Nivel: Basico (condicion con 'and' + calculo de porcentaje)

Reglas: tributa quien sea mayor de 18 años Y tenga ingresos >= S/3000.
        El monto a tributar es el 5% del ingreso mensual.
Ejemplo de uso:
    Entrada: edad = 25, ingresos = 4000
    Salida : Debe tributar. Monto: S/200.00
"""

EDAD_MINIMA = 18
INGRESO_MINIMO = 3000
TASA_IMPUESTO = 0.05


def debe_tributar(edad, ingresos):
    """True si cumple ambos requisitos (mayor de 18 e ingresos suficientes)."""
    return edad > EDAD_MINIMA and ingresos >= INGRESO_MINIMO


def main():
    edad = int(input("Edad: "))
    ingresos = float(input("Ingresos mensuales (S/): "))

    if debe_tributar(edad, ingresos):
        monto = ingresos * TASA_IMPUESTO
        print(f"Debe tributar. Monto (5%): S/{monto:.2f}")
    else:
        print("No debe tributar.")


if __name__ == "__main__":
    main()
