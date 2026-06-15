"""
Ejercicio 09 - Inversion con interes compuesto
===============================================
Objetivo:
    Aplicar el modelo de interes compuesto usando la potenciacion. Se
    parametriza la tasa y el numero de meses mediante constantes.

Nivel: Avanzado (potenciacion / modelo financiero)

Formula: monto_final = capital * (1 + tasa) ** meses
Nota   : Si se pidiera interes SIMPLE seria: capital * tasa * meses.
Ejemplo de uso:
    Entrada: capital = 1000, 2% mensual, 12 meses
    Salida : Monto final S/1268.24, ganancia S/268.24
"""

TASA_MENSUAL = 0.02   # 2% mensual
MESES_ANIO = 12


def interes_compuesto(capital, tasa, meses):
    """Devuelve el monto final tras aplicar interes compuesto."""
    return capital * (1 + tasa) ** meses


def main():
    capital = float(input("Capital a invertir: "))

    monto_final = interes_compuesto(capital, TASA_MENSUAL, MESES_ANIO)
    ganancia = monto_final - capital

    print(f"Monto final tras {MESES_ANIO} meses: S/{monto_final:.2f}")
    print(f"Ganancia obtenida:            S/{ganancia:.2f}")


if __name__ == "__main__":
    main()
