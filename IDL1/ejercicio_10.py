"""
Ejercicio 10 - Denominaciones del cajero automatico
====================================================
Objetivo:
    Usar listas, un bucle y una estrategia voraz (greedy) para entregar
    una cantidad de dinero con el menor numero de piezas posible.
    Es el ejercicio mas avanzado: combina division entera, residuo,
    recorrido de lista y un diccionario de resultados.

Nivel: Avanzado (estructura iterativa + estrategia greedy)

Denominaciones disponibles: 200, 100, 50, 20, 10, 5, 1
Ejemplo de uso:
    Entrada: 388
    Salida : 1 x S/200, 1 x S/100, 1 x S/50, 1 x S/20,
             1 x S/10, 1 x S/5, 3 x S/1
"""

# De mayor a menor: clave para que la estrategia voraz sea optima
DENOMINACIONES = [200, 100, 50, 20, 10, 5, 1]


def desglosar(cantidad, denominaciones=DENOMINACIONES):
    """Devuelve un diccionario {denominacion: numero_de_piezas}."""
    desglose = {}
    restante = cantidad
    for valor in denominaciones:
        desglose[valor] = restante // valor   # piezas que caben de esta denominacion
        restante %= valor                      # residuo para la siguiente
    return desglose


def main():
    cantidad = int(input("Cantidad a retirar: S/"))

    desglose = desglosar(cantidad)
    print("Entrega del cajero:")
    for valor, piezas in desglose.items():
        if piezas > 0:                          # solo mostramos las que se usan
            print(f"  {piezas} x S/{valor}")


if __name__ == "__main__":
    main()
