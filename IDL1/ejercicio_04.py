"""
Ejercicio 04 - Area de un terreno (trapecio rectangulo)
========================================================
Objetivo:
    Aplicar la formula del area de un trapecio rectangulo a partir de la
    longitud de sus tres lados. El terreno equivale a un rectangulo de
    altura C mas un triangulo de altura (A - C), ambos de base B.

Nivel: Intermedio (formula geometrica)

Formula: area = (A + C) / 2 * B
Ejemplo de uso:
    Entrada: A = 10, B = 8, C = 6
    Salida : Area del terreno: 64.00
"""


def area_trapecio(lado_a, base_b, lado_c):
    """Area del trapecio rectangulo con lados verticales A y C y base B."""
    return (lado_a + lado_c) / 2 * base_b


def main():
    lado_a = float(input("Lado A (vertical izquierdo): "))
    base_b = float(input("Lado B (base): "))
    lado_c = float(input("Lado C (vertical derecho): "))

    area = area_trapecio(lado_a, base_b, lado_c)
    print(f"Area del terreno: {area:.2f}")


if __name__ == "__main__":
    main()
