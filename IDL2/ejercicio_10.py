"""
Ejercicio 10 - Notas de N estudiantes (validacion + estadisticas)
==================================================================
Objetivo:
    Ejercicio integrador. Valida N (entre 5 y 20) y cada nota (entre 0 y
    20) mediante bucles de validacion, y calcula 11 estadisticas del
    salon. Reutiliza una funcion generica de lectura validada.

Nivel: Avanzado (validacion robusta + agregacion de resultados)

Ejemplo de uso:
    Entrada: N = 5 -> notas 20, 13, 12, 20, 8
    Salida : mayor 20, menor 8, prom 14.60, aprobados 3 (60%), etc.
"""

NOTA_APROBATORIA = 13


def leer_entero_en_rango(mensaje, minimo, maximo):
    """Lee un entero y repite la pregunta hasta que este dentro de [minimo, maximo]."""
    while True:
        valor = int(input(mensaje))
        if minimo <= valor <= maximo:
            return valor
        print(f"  El valor debe estar entre {minimo} y {maximo}.")


def calcular_estadisticas(notas):
    """Devuelve un diccionario con las 11 estadisticas solicitadas (a-k)."""
    total = len(notas)
    mayor = max(notas)
    menor = min(notas)
    aprobados = sum(1 for nota in notas if nota >= NOTA_APROBATORIA)
    pares = sum(1 for nota in notas if nota % 2 == 0)

    return {
        "mayor": mayor,
        "menor": menor,
        "cant_mayor": notas.count(mayor),
        "cant_menor": notas.count(menor),
        "promedio": sum(notas) / total,
        "pares": pares,
        "impares": total - pares,
        "aprobados": aprobados,
        "desaprobados": total - aprobados,
        "porc_aprob": aprobados / total * 100,
        "porc_desap": (total - aprobados) / total * 100,
    }


def main():
    cantidad = leer_entero_en_rango("Cantidad de estudiantes (5 a 20): ", 5, 20)

    notas = []
    for indice in range(1, cantidad + 1):
        nota = leer_entero_en_rango(f"Nota del estudiante {indice} (0-20): ", 0, 20)
        notas.append(nota)

    est = calcular_estadisticas(notas)

    print("\n----- RESULTADOS -----")
    print(f"a) Mayor nota: {est['mayor']}")
    print(f"b) Menor nota: {est['menor']}")
    print(f"c) Alumnos con la mayor nota: {est['cant_mayor']}")
    print(f"d) Alumnos con la menor nota: {est['cant_menor']}")
    print(f"e) Promedio del salon: {est['promedio']:.2f}")
    print(f"f) Notas pares: {est['pares']}")
    print(f"g) Notas impares: {est['impares']}")
    print(f"h) Aprobados: {est['aprobados']}")
    print(f"i) Desaprobados: {est['desaprobados']}")
    print(f"j) Porcentaje aprobados: {est['porc_aprob']:.2f}%")
    print(f"k) Porcentaje desaprobados: {est['porc_desap']:.2f}%")


if __name__ == "__main__":
    main()
