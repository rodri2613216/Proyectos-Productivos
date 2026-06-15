"""
Ejercicio 03 - Mayor y menor de tres numeros
=============================================
Objetivo:
    Practicar la comparacion con condicionales para hallar el mayor y el
    menor sin usar las funciones max()/min() (se hace 'a mano').

Nivel: Basico-Intermedio (logica de comparacion)

Ejemplo de uso:
    Entrada: 5, 9, 2
    Salida : Mayor: 9.0 | Menor: 2.0
"""


def mayor_y_menor(a, b, c):
    """Devuelve (mayor, menor) de tres valores usando comparaciones."""
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c

    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c

    return mayor, menor


def main():
    a = float(input("Numero 1: "))
    b = float(input("Numero 2: "))
    c = float(input("Numero 3: "))

    mayor, menor = mayor_y_menor(a, b, c)
    print(f"Mayor: {mayor} | Menor: {menor}")


if __name__ == "__main__":
    main()
