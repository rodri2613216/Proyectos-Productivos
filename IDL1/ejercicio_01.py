"""
Ejercicio 01 - Promedio de cuatro examenes
============================================
Objetivo:
    Practicar la lectura de datos por teclado, las operaciones aritmeticas
    basicas (suma y division) y la presentacion de resultados.

Nivel: Basico (punto de partida)

Ejemplo de uso:
    Entrada: 15, 18, 12, 17
    Salida : Promedio de las calificaciones: 15.50
"""


def calcular_promedio(notas):
    """Devuelve el promedio aritmetico de una lista de notas."""
    return sum(notas) / len(notas)


def main():
    # Leemos las 4 calificaciones (todas con la misma ponderacion)
    notas = []
    for numero in range(1, 5):
        nota = float(input(f"Ingrese la nota {numero}: "))
        notas.append(nota)

    promedio = calcular_promedio(notas)
    print(f"Promedio de las calificaciones: {promedio:.2f}")


if __name__ == "__main__":
    main()
