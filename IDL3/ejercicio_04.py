"""
Ejercicio 04 - Clasificar 10 numeros (paridad y signo)
=======================================================
Objetivo:
    Usar un bucle de cantidad fija (10 lecturas) manteniendo VARIOS
    contadores a la vez. Cada numero se clasifica por paridad
    (par/impar) y por signo (positivo/negativo/neutro).

Nivel: Intermedio (multiples contadores simultaneos)

Ejemplo de uso:
    Entrada: 3, -2, 0, 7, -5, 8, 1, -1, 4, 0
    Salida : Pares 5, Impares 5, Positivos 5, Negativos 3, Neutros 2
"""


def clasificar(numeros):
    """Devuelve un diccionario con los conteos por paridad y por signo."""
    conteo = {"pares": 0, "impares": 0,
              "positivos": 0, "negativos": 0, "neutros": 0}

    for numero in numeros:
        # Clasificacion por paridad
        if numero % 2 == 0:
            conteo["pares"] += 1
        else:
            conteo["impares"] += 1

        # Clasificacion por signo
        if numero > 0:
            conteo["positivos"] += 1
        elif numero < 0:
            conteo["negativos"] += 1
        else:
            conteo["neutros"] += 1

    return conteo


def main():
    numeros = []
    for indice in range(1, 11):       # exactamente 10 numeros
        numeros.append(int(input(f"Numero {indice}: ")))

    conteo = clasificar(numeros)
    print(f"Pares:     {conteo['pares']}")
    print(f"Impares:   {conteo['impares']}")
    print(f"Positivos: {conteo['positivos']}")
    print(f"Negativos: {conteo['negativos']}")
    print(f"Neutros:   {conteo['neutros']}")


if __name__ == "__main__":
    main()
