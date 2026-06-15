"""
Ejercicio 07 - Porcentajes respecto a un numero X
===================================================
Objetivo:
    Leer N numeros y un valor X, y contar de forma INDEPENDIENTE varias
    condiciones, expresando cada una como porcentaje del total.

Nivel: Intermedio-Avanzado (multiples condiciones + porcentajes)

Nota:
    Las condiciones "menor / mayor / igual" a X ya cubren todos los casos,
    por lo que "no cumple ninguna" normalmente resulta 0%.

Ejemplo de uso:
    Entrada: N = 5, X = 10, numeros = 5, 10, 15, 8, 10
    Salida : Menores 40%, Mayores 20%, Iguales 40%, Entre 1 y X 80%, Ninguna 0%
"""


def contar_condiciones(numeros, x):
    """Devuelve un diccionario con la cantidad de numeros que cumple cada condicion."""
    contadores = {"menores": 0, "mayores": 0, "iguales": 0, "entre": 0, "ninguna": 0}

    for numero in numeros:
        es_menor = numero < x
        es_mayor = numero > x
        es_igual = numero == x
        esta_entre = 1 <= numero <= x

        if es_menor:
            contadores["menores"] += 1
        if es_mayor:
            contadores["mayores"] += 1
        if es_igual:
            contadores["iguales"] += 1
        if esta_entre:
            contadores["entre"] += 1
        if not (es_menor or es_mayor or es_igual or esta_entre):
            contadores["ninguna"] += 1

    return contadores


def main():
    cantidad = int(input("Cuantos numeros ingresara (N): "))
    x = float(input("Ingrese el numero X: "))

    numeros = []
    for indice in range(1, cantidad + 1):
        numeros.append(float(input(f"Numero {indice}: ")))

    contadores = contar_condiciones(numeros, x)
    total = len(numeros)

    print(f"Menores que X:     {contadores['menores'] / total * 100:.2f}%")
    print(f"Mayores que X:     {contadores['mayores'] / total * 100:.2f}%")
    print(f"Iguales a X:       {contadores['iguales'] / total * 100:.2f}%")
    print(f"Entre 1 y X:       {contadores['entre'] / total * 100:.2f}%")
    print(f"No cumple ninguna: {contadores['ninguna'] / total * 100:.2f}%")


if __name__ == "__main__":
    main()
