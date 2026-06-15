"""
Ejercicio 09 - Cronometro (hh:mm:ss)
=====================================
Objetivo:
    Usar el modulo 'time' y el formateo hh:mm:ss, actualizando la salida
    en la MISMA linea de la terminal con '\\r'. Es referencial: usa
    time.sleep(1), por lo que no es exacto a un cronometro real.

Nivel: Avanzado (modulo externo + salida en tiempo real)

Ejemplo de uso:
    Entrada: 5 (segundos)
    Salida : 00:00:00 -> 00:00:01 -> ... -> 00:00:05
"""

import time


def formato_hms(total_segundos):
    """Convierte una cantidad de segundos al formato hh:mm:ss."""
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


def main():
    duracion = int(input("Cuantos segundos debe correr el cronometro: "))

    for transcurridos in range(duracion + 1):
        # end="\r" reescribe la linea; flush fuerza la actualizacion inmediata
        print(f"\r{formato_hms(transcurridos)}", end="", flush=True)
        time.sleep(1)

    print("\nCronometro detenido.")


if __name__ == "__main__":
    main()
