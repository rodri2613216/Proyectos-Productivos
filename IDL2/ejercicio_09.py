"""
Ejercicio 09 - Pago de una llamada telefonica
==============================================
Objetivo:
    Resolver un cobro ESCALONADO por tramos acumulativos (if/elif) y
    aplicar un impuesto condicional segun el dia y el turno.

Nivel: Avanzado (tarifas por tramos + impuesto condicional)

Tarifas: min 1-5 -> S/1.00 c/u; 6-8 -> S/0.80; 9-10 -> S/0.70; 11+ -> S/0.50.
Impuesto: 3% si es domingo; 5% si es domingo de turno nocturno.
Ejemplo de uso:
    Entrada: 12 minutos, domingo nocturno
    Salida : Consumo S/9.80, impuesto S/0.49, total S/10.29
"""


def costo_consumo(minutos):
    """Costo de la llamada segun los tramos de tarifa acumulativos."""
    if minutos <= 5:
        return minutos * 1.00
    elif minutos <= 8:
        return 5 * 1.00 + (minutos - 5) * 0.80
    elif minutos <= 10:
        return 5 * 1.00 + 3 * 0.80 + (minutos - 8) * 0.70
    else:
        return 5 * 1.00 + 3 * 0.80 + 2 * 0.70 + (minutos - 10) * 0.50


def calcular_impuesto(costo, es_domingo, es_nocturno):
    """Impuesto: 5% domingo nocturno, 3% domingo normal, 0% otro dia."""
    if es_domingo and es_nocturno:
        return costo * 0.05
    if es_domingo:
        return costo * 0.03
    return 0.0


def main():
    minutos = int(input("Duracion de la llamada (minutos): "))
    es_domingo = input("Es domingo? (s/n): ").strip().lower() == "s"

    es_nocturno = False
    if es_domingo:
        es_nocturno = input("Es turno nocturno? (s/n): ").strip().lower() == "s"

    consumo = costo_consumo(minutos)
    impuesto = calcular_impuesto(consumo, es_domingo, es_nocturno)
    total = consumo + impuesto

    print(f"Costo por consumo: S/{consumo:.2f}")
    print(f"Impuesto:          S/{impuesto:.2f}")
    print(f"Total a pagar:     S/{total:.2f}")


if __name__ == "__main__":
    main()
