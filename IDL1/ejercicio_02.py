"""
Ejercicio 02 - Tiempo vivido segun la edad
===========================================
Objetivo:
    Reforzar el uso de la multiplicacion y la reutilizacion de un
    resultado intermedio (los dias) para calcular las horas.

Nivel: Basico

Ejemplo de uso:
    Entrada: 20
    Salida : 240 meses, 1040 semanas, 7300 dias, 175200 horas
"""


def calcular_tiempo_vivido(edad_anios):
    """Devuelve (meses, semanas, dias, horas) aproximados para una edad."""
    meses = edad_anios * 12
    semanas = edad_anios * 52
    dias = edad_anios * 365
    horas = dias * 24            # se reutiliza 'dias' para no repetir el calculo
    return meses, semanas, dias, horas


def main():
    edad = int(input("Ingrese la edad en años: "))
    meses, semanas, dias, horas = calcular_tiempo_vivido(edad)

    print(f"Meses vividos:   {meses}")
    print(f"Semanas vividas: {semanas}")
    print(f"Dias vividos:    {dias}")
    print(f"Horas vividas:   {horas}")


if __name__ == "__main__":
    main()
