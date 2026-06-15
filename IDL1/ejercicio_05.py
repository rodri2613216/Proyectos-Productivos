"""
Ejercicio 05 - Cobro de estacionamiento
========================================
Objetivo:
    Combinar dos tarifas distintas (una por hora completa y otra por
    minuto restante) dentro de un unico calculo. Se introducen constantes
    con nombre para los precios.

Nivel: Intermedio

Tarifas: S/5.00 por hora completa, S/0.10 por minuto restante.
Ejemplo de uso:
    Entrada: 3 horas, 25 minutos
    Salida : Cobro total: S/17.50
"""

PRECIO_HORA = 5.00
PRECIO_MINUTO = 0.10


def calcular_cobro(horas, minutos):
    """Cobro total combinando la tarifa por hora y la tarifa por minuto."""
    return horas * PRECIO_HORA + minutos * PRECIO_MINUTO


def main():
    horas = int(input("Horas completas: "))
    minutos = int(input("Minutos restantes: "))

    cobro = calcular_cobro(horas, minutos)
    print(f"Cobro total: S/{cobro:.2f}")


if __name__ == "__main__":
    main()
