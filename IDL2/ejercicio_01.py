"""
Ejercicio 01 - Suma y promedio de pares e impares (1 a N)
==========================================================
Objetivo:
    Introducir el bucle 'for' sobre un rango conocido y el uso de
    acumuladores separados controlados por una condicion (la paridad).

Nivel: Basico (primer contacto con bucles + acumuladores)

Ejemplo de uso:
    Entrada: N = 10
    Salida : PARES   -> Suma: 30 | Promedio: 6.00
             IMPARES -> Suma: 25 | Promedio: 5.00
"""


def sumar_pares_impares(n):
    """Recorre 1..n y devuelve (suma_pares, cant_pares, suma_impares, cant_impares)."""
    suma_pares = cant_pares = 0
    suma_impares = cant_impares = 0

    for numero in range(1, n + 1):
        if numero % 2 == 0:          # par
            suma_pares += numero
            cant_pares += 1
        else:                        # impar
            suma_impares += numero
            cant_impares += 1

    return suma_pares, cant_pares, suma_impares, cant_impares


def promedio_seguro(suma, cantidad):
    """Promedio que evita la division entre cero."""
    return suma / cantidad if cantidad > 0 else 0


def main():
    n = int(input("Ingrese N: "))
    suma_pares, cant_pares, suma_impares, cant_impares = sumar_pares_impares(n)

    print(f"PARES   -> Suma: {suma_pares} | Promedio: {promedio_seguro(suma_pares, cant_pares):.2f}")
    print(f"IMPARES -> Suma: {suma_impares} | Promedio: {promedio_seguro(suma_impares, cant_impares):.2f}")


if __name__ == "__main__":
    main()
