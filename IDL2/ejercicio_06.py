"""
Ejercicio 06 - Hora N segundos despues
=======================================
Objetivo:
    Aplicar aritmetica modular (division entera y modulo) para sumar
    segundos a una hora y normalizar el resultado a un dia de 24 horas.

Nivel: Intermedio (tecnica de aritmetica modular)

Ejemplo de uso:
    Entrada: 23:59:50 + 20 segundos
    Salida : Hora resultante: 00:00:10
"""

SEGUNDOS_POR_DIA = 86400   # 24 * 60 * 60


def sumar_segundos(horas, minutos, segundos, n):
    """Suma n segundos a una hora y devuelve (h, m, s) en formato 24h."""
    total = (horas * 3600 + minutos * 60 + segundos + n) % SEGUNDOS_POR_DIA
    nuevas_horas = total // 3600
    nuevos_minutos = (total % 3600) // 60
    nuevos_segundos = total % 60
    return nuevas_horas, nuevos_minutos, nuevos_segundos


def main():
    horas = int(input("Horas (HH): "))
    minutos = int(input("Minutos (MM): "))
    segundos = int(input("Segundos (SS): "))
    n = int(input("Segundos a sumar (N): "))

    h, m, s = sumar_segundos(horas, minutos, segundos, n)
    print(f"Hora resultante: {h:02d}:{m:02d}:{s:02d}")


if __name__ == "__main__":
    main()
