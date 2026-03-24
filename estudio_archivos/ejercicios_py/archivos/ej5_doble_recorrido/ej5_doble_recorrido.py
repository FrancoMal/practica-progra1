# =============================================================================
# EJERCICIO 5 - Numeros mayores al promedio (doble recorrido con seek)
# =============================================================================
# Consigna: Leer el archivo numeros.txt (un numero por linea), calcular el
# promedio de todos los numeros. Luego, usando seek(0), volver a leer el
# archivo e imprimir solo aquellos numeros que sean mayores al promedio.
# =============================================================================
# Reglas de la cursada:
# - NUNCA usar readlines(), read() sin parametro, ni list(arch) -> PROHIBIDO
# - Usar readline() con while, o for linea in arch
# - Siempre try/except/finally con close() protegido por except NameError
# - FileNotFoundError ANTES de OSError
# - Usar seek(0) en vez de cerrar y reabrir en el mismo modo
# =============================================================================

print("=" * 60)
print("EJERCICIO 5 - Numeros mayores al promedio (usando seek)")
print("=" * 60)

try:
    arch = open("numeros.txt", "r")

    # Primera pasada: calcular el promedio
    suma = 0
    cantidad = 0
    for linea in arch:
        linea = linea.strip()
        if linea != "":
            numero = float(linea)
            suma += numero
            cantidad += 1

    if cantidad > 0:
        promedio = suma / cantidad
        print(f"Promedio calculado: {promedio:.2f}")

        # Volver al inicio del archivo con seek(0) en vez de cerrar y reabrir
        arch.seek(0)

        # Segunda pasada: mostrar numeros mayores al promedio
        print("Numeros mayores al promedio:")
        for linea in arch:
            linea = linea.strip()
            if linea != "":
                numero = float(linea)
                if numero > promedio:
                    print(f"  {numero:.0f}")
    else:
        print("El archivo esta vacio.")
except FileNotFoundError:
    print("Error: no se encontro el archivo numeros.txt")
except OSError:
    print("Error al acceder al archivo numeros.txt")
finally:
    try:
        arch.close()
    except NameError:
        pass
