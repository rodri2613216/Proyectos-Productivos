"""
Ejercicio 08 - Porcentaje de inversion de tres socios
======================================================
Objetivo:
    Calcular porcentajes RELATIVOS al total a partir de varios valores.
    Se introduce el recorrido de una lista con enumerate y las
    comprensiones de listas.

Nivel: Avanzado (porcentajes relativos + listas)

Ejemplo de uso:
    Entrada: 2000, 3000, 5000  (total 10000)
    Salida : Persona 1: 20.00%, Persona 2: 30.00%, Persona 3: 50.00%
"""


def calcular_porcentajes(inversiones):
    """Devuelve la lista de porcentajes de cada inversion sobre el total."""
    total = sum(inversiones)
    return [inversion / total * 100 for inversion in inversiones]


def main():
    inversiones = []
    for numero in range(1, 4):
        inversion = float(input(f"Inversion de la persona {numero}: "))
        inversiones.append(inversion)

    porcentajes = calcular_porcentajes(inversiones)
    for numero, porcentaje in enumerate(porcentajes, start=1):
        print(f"Persona {numero}: {porcentaje:.2f}%")


if __name__ == "__main__":
    main()
