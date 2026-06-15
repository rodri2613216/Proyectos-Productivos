"""
Ejercicio 07 - Ordenar tres enteros diferentes
===============================================
Objetivo:
    Combinar una VALIDACION (los tres numeros deben ser distintos) con una
    decision que elige el sentido del ordenamiento (ascendente/descendente).

Nivel: Intermedio-Avanzado (validacion + seleccion de orden)

Ejemplo de uso:
    Entrada: 5, 2, 8  y orden 'a'
    Salida : Orden ascendente: [2, 5, 8]
"""


def todos_diferentes(numeros):
    """True si todos los elementos de la lista son distintos entre si."""
    return len(set(numeros)) == len(numeros)


def ordenar(numeros, ascendente=True):
    """Devuelve una nueva lista ordenada en el sentido indicado."""
    return sorted(numeros, reverse=not ascendente)


def main():
    a = int(input("Numero entero 1: "))
    b = int(input("Numero entero 2: "))
    c = int(input("Numero entero 3: "))
    numeros = [a, b, c]

    if not todos_diferentes(numeros):
        print("ERROR: los tres numeros deben ser diferentes entre si.")
        return

    orden = input("Orden ascendente (a) o descendente (d): ").strip().lower()
    if orden == "a":
        print("Orden ascendente:", ordenar(numeros, ascendente=True))
    elif orden == "d":
        print("Orden descendente:", ordenar(numeros, ascendente=False))
    else:
        print("Opcion no valida (use 'a' o 'd').")


if __name__ == "__main__":
    main()
