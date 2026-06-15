"""
Ejercicio 02 - Producto con arrays (100 x 98 x 96 x ... x 2)
============================================================
Objetivo:
    Construir una lista (array) con range() usando un paso, y recorrerla
    acumulando un PRODUCTO. No requiere datos del usuario.

Nivel: Basico (listas + acumulador de producto)

Nota:
    El enunciado termina en "x 1"; como la secuencia baja de 2 en 2 desde
    100, llega hasta 2, y multiplicar por 1 no altera el resultado.

Ejemplo de uso:
    Salida: Array: [100, 98, 96, ..., 4, 2]
            Producto total: (numero muy grande)
"""


def construir_secuencia(inicio=100, paso=2):
    """Lista descendente desde 'inicio' hasta el menor positivo, de 'paso' en 'paso'."""
    return list(range(inicio, 0, -paso))


def producto_lista(numeros):
    """Devuelve el producto de todos los elementos de la lista."""
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


def main():
    numeros = construir_secuencia()
    print("Array:", numeros)
    print("Producto total:", producto_lista(numeros))


if __name__ == "__main__":
    main()
