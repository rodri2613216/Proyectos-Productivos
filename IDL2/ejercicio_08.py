"""
Ejercicio 08 - Costo de llamadas internacionales por zona
==========================================================
Objetivo:
    Usar un DICCIONARIO como tabla de datos (clave -> zona y costo) y
    validar que la clave ingresada exista antes de calcular.

Nivel: Avanzado (estructura de datos tipo diccionario + busqueda)

Tabla:
    10 America del Norte (2.2)   12 America del Centro (2.5)
    20 America del Sur   (1.2)   22 Asia              (3.5)
    30 Europa            (3.0)   32 Africa            (3.2)
Ejemplo de uso:
    Entrada: clave = 20, minutos = 10
    Salida : Zona America del Sur | Costo total: S/12.00
"""

# clave -> (nombre de la zona, costo por minuto)
ZONAS = {
    10: ("America del Norte", 2.2),
    12: ("America del Centro", 2.5),
    20: ("America del Sur", 1.2),
    22: ("Asia", 3.5),
    30: ("Europa", 3.0),
    32: ("Africa", 3.2),
}


def costo_llamada(clave, minutos):
    """Devuelve (nombre_zona, costo_total) o None si la clave no existe."""
    if clave not in ZONAS:
        return None
    nombre, costo_por_minuto = ZONAS[clave]
    return nombre, minutos * costo_por_minuto


def main():
    clave = int(input("Clave de la zona geografica: "))
    minutos = int(input("Minutos hablados: "))

    resultado = costo_llamada(clave, minutos)
    if resultado is None:
        print("Clave de zona no valida.")
    else:
        nombre, total = resultado
        print(f"Zona: {nombre}")
        print(f"Costo total de la llamada: S/{total:.2f}")


if __name__ == "__main__":
    main()
