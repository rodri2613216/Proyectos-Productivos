"""
Ejercicio 03 - Factorial de dos numeros y prefijo comun
========================================================
Objetivo:
    Calcular el factorial con un bucle (acumulador de producto) y comparar
    dos factoriales: como ambos comparten el inicio 1x2x3..., son iguales
    hasta el multiplo minimo(a, b).

Nivel: Basico-Intermedio (acumulador + logica de comparacion)

Ejemplo de uso:
    Entrada: 7 y 10
    Salida : 7!  = 1x2x3x4x5x6x7 = 5040
             10! = 1x2x...x10 = 3628800
             >> Son iguales hasta el multiplo 7
"""


def factorial(n):
    """Factorial de n calculado con un bucle."""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def expansion(n):
    """Cadena de la forma '1x2x3x...xn'."""
    return "x".join(str(i) for i in range(1, n + 1))


def main():
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))

    print(f"{a}! = {expansion(a)} = {factorial(a)}")
    print(f"{b}! = {expansion(b)} = {factorial(b)}")
    print(f">> Son iguales hasta el multiplo {min(a, b)}")


if __name__ == "__main__":
    main()
