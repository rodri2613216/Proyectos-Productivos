"""
Ejercicio 05 - Maximo y minimo de N numeros
============================================
Objetivo:
    Leer N numeros y determinar simultaneamente el maximo y el minimo,
    inicializando ambos con el PRIMER valor leido y actualizandolos en
    un unico recorrido.

Nivel: Intermedio (seguimiento de valores extremos)

Ejemplo de uso:
    Entrada: 5 numeros -> 7, 2, 9, 4, 1
    Salida : Maximo: 9.0 | Minimo: 1.0
"""


def maximo_minimo(numeros):
    """Devuelve (maximo, minimo) recorriendo la lista una sola vez."""
    maximo = minimo = numeros[0]      # se inicializan con el primer numero
    for numero in numeros[1:]:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    return maximo, minimo


def main():
    cantidad = int(input("Cuantos numeros ingresara: "))

    numeros = []
    for indice in range(1, cantidad + 1):
        numeros.append(float(input(f"Numero {indice}: ")))

    maximo, minimo = maximo_minimo(numeros)
    print(f"Maximo: {maximo} | Minimo: {minimo}")


if __name__ == "__main__":
    main()
