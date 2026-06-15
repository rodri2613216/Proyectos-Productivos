"""
Ejercicio 05 - Colegiatura con descuento por promedio
======================================================
Objetivo:
    Decision if/else en la que UNA de las ramas realiza un calculo
    adicional (el descuento de beca) y la otra no.

Nivel: Intermedio (rama con calculo condicional)

Reglas: cada materia cuesta S/100. Si el promedio >= 18 se aplica 50% de
        descuento sobre la mitad de los cursos; si es < 18 se paga todo.
Ejemplo de uso:
    Entrada: 8 materias, promedio 18
    Salida : Colegiatura S/800.00, descuento S/200.00, a pagar S/600.00
"""

COSTO_MATERIA = 100
PROMEDIO_BECA = 18


def calcular_pago(materias, promedio):
    """Devuelve (pago_final, descuento, costo_total)."""
    costo_total = materias * COSTO_MATERIA

    if promedio >= PROMEDIO_BECA:
        # 50% de descuento aplicado solo a la mitad de los cursos
        descuento = (materias / 2 * COSTO_MATERIA) * 0.50
        return costo_total - descuento, descuento, costo_total

    return costo_total, 0, costo_total


def main():
    materias = int(input("Numero de materias: "))
    promedio = float(input("Promedio del ultimo periodo: "))

    pago, descuento, costo_total = calcular_pago(materias, promedio)

    print(f"Colegiatura completa: S/{costo_total:.2f}")
    print(f"Descuento aplicado:   S/{descuento:.2f}")
    print(f"Total a pagar:        S/{pago:.2f}")


if __name__ == "__main__":
    main()
