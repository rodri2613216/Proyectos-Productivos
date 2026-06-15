"""
Ejercicio 08 - Asistentes a una fiesta
=======================================
Objetivo:
    Usar un bucle INDEFINIDO (no se sabe cuantas personas habra): se
    registra al menos una persona y, tras cada registro, se pregunta si
    se desea ingresar otra. Se mantienen acumuladores por sexo, promedios
    y las edades minima y maxima.

Nivel: Avanzado (bucle controlado por el usuario + multiples acumuladores)

Ejemplo de uso:
    Entrada: (25, M), (30, F), (20, M) y luego 'n' para terminar
    Salida : Total 3 | Hombres 2, Mujeres 1 | Promedios por sexo | edad min/max
"""


def main():
    total = 0
    hombres = mujeres = 0
    suma_edad_h = suma_edad_m = 0
    edad_min = edad_max = None

    continuar = "s"
    while continuar == "s":                  # se ejecuta al menos una vez
        edad = int(input("Edad de la persona: "))
        sexo = input("Sexo (M=masculino / F=femenino): ").strip().upper()

        total += 1
        if sexo == "M":
            hombres += 1
            suma_edad_h += edad
        elif sexo == "F":
            mujeres += 1
            suma_edad_m += edad

        # Actualizacion de edades extremas
        if edad_min is None or edad < edad_min:
            edad_min = edad
        if edad_max is None or edad > edad_max:
            edad_max = edad

        continuar = input("Desea registrar a otra persona? (s/n): ").strip().lower()

    promedio_h = suma_edad_h / hombres if hombres > 0 else 0
    promedio_m = suma_edad_m / mujeres if mujeres > 0 else 0

    print(f"\nTotal de asistentes: {total}")
    print(f"Hombres: {hombres} | Mujeres: {mujeres}")
    print(f"Promedio de edad (hombres): {promedio_h:.2f}")
    print(f"Promedio de edad (mujeres): {promedio_m:.2f}")
    print(f"Edad menor: {edad_min} | Edad mayor: {edad_max}")


if __name__ == "__main__":
    main()
