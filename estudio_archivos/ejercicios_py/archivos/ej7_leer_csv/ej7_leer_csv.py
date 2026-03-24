# =============================================================================
# EJERCICIO 7 - Leer archivo CSV linea por linea
# =============================================================================
# Consigna: Leer el archivo datos.csv (formato CSV con header:
# nombre,edad,ciudad). Saltear la linea de encabezado, y luego imprimir
# cada registro formateado. NO usar el modulo csv, solo for + split(',').
# Al final, mostrar la edad promedio de todas las personas.
# =============================================================================
# Reglas de la cursada:
# - NUNCA usar readlines(), read() sin parametro, ni list(arch) -> PROHIBIDO
# - Usar readline() con while, o for linea in arch
# - Siempre try/except/finally con close() protegido por except NameError
# - FileNotFoundError ANTES de OSError
# - Usar seek(0) en vez de cerrar y reabrir en el mismo modo
# =============================================================================

print("=" * 60)
print("EJERCICIO 7 - Leer archivo CSV linea por linea")
print("=" * 60)

try:
    arch = open("datos.csv", "r")

    # Leer y descartar la linea de encabezado
    header = arch.readline()

    suma_edades = 0
    cantidad = 0
    for linea in arch:
        linea = linea.strip()
        if linea != "":
            campos = linea.split(",")
            nombre = campos[0]
            edad = int(campos[1])
            ciudad = campos[2]
            suma_edades += edad
            cantidad += 1
            print(f"  {nombre} tiene {edad} anios y vive en {ciudad}")

    if cantidad > 0:
        promedio = suma_edades / cantidad
        print(f"Cantidad de registros: {cantidad}")
        print(f"Edad promedio: {promedio:.2f} anios")
    else:
        print("No se encontraron registros en el archivo.")
except FileNotFoundError:
    print("Error: no se encontro el archivo datos.csv")
except OSError:
    print("Error al acceder al archivo datos.csv")
finally:
    try:
        arch.close()
    except NameError:
        pass
