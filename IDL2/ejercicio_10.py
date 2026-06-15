"""
Ejercicio 10 - Clasificacion de un triangulo
=============================================
Objetivo:
    Ejercicio integrador: validar primero que los lados formen un triangulo
    (desigualdad triangular), clasificarlo con condiciones anidadas y, segun
    el tipo, mostrar perimetro, los lados iguales o el area (formula de Heron).

Nivel: Avanzado (validacion + clasificacion anidada + formulas)

Ejemplos de uso:
    3, 3, 3 -> Equilatero | Perimetro: 9.0
    5, 5, 8 -> Isosceles  | Lados iguales: a y b
    3, 4, 5 -> Escaleno   | Area: 6.00
"""

import math


def es_triangulo_valido(a, b, c):
    """True si los tres lados cumplen la desigualdad triangular."""
    return a + b > c and a + c > b and b + c > a


def area_heron(a, b, c):
    """Area de un triangulo a partir de sus tres lados (formula de Heron)."""
    s = (a + b + c) / 2     # semiperimetro
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    a = float(input("Lado a: "))
    b = float(input("Lado b: "))
    c = float(input("Lado c: "))

    if not es_triangulo_valido(a, b, c):
        print("Los lados ingresados NO forman un triangulo valido.")
        return

    if a == b == c:
        print("Triangulo EQUILATERO")
        print(f"Perimetro: {a + b + c}")
    elif a == b or b == c or a == c:
        print("Triangulo ISOSCELES")
        if a == b:
            print("Lados iguales: a y b")
        elif b == c:
            print("Lados iguales: b y c")
        else:
            print("Lados iguales: a y c")
    else:
        print("Triangulo ESCALENO")
        print(f"Area: {area_heron(a, b, c):.2f}")


if __name__ == "__main__":
    main()
