"""
Ejercicio 03 - Velocidad final de un auto (MRUA)
=================================================
Objetivo:
    Aplicar una formula fisica (movimiento rectilineo uniformemente
    acelerado) e introducir la conversion de unidades entre km/h y m/s.

Nivel: Basico-Intermedio (formula + conversion de unidades)

Formula: vf = v0 + a * t
Ejemplo de uso:
    Entrada: v0 = 0 km/h, a = 0.8 m/s2, t = 30 s
    Salida : Velocidad final: 24.00 m/s (86.40 km/h)
"""

# Factor de conversion: 1 km/h equivale a 1/3.6 m/s
KMH_A_MS = 1 / 3.6


def velocidad_final(v0_kmh, aceleracion, tiempo):
    """Calcula la velocidad final en m/s a partir de v0 (km/h), a (m/s2) y t (s)."""
    v0_ms = v0_kmh * KMH_A_MS              # convertimos la inicial a m/s
    return v0_ms + aceleracion * tiempo    # MRUA


def main():
    v0 = float(input("Velocidad inicial (km/h): "))
    aceleracion = float(input("Aceleracion (m/s2): "))
    tiempo = float(input("Tiempo (s): "))

    vf_ms = velocidad_final(v0, aceleracion, tiempo)
    vf_kmh = vf_ms * 3.6                    # convertimos el resultado a km/h

    print(f"Velocidad final: {vf_ms:.2f} m/s ({vf_kmh:.2f} km/h)")


if __name__ == "__main__":
    main()
