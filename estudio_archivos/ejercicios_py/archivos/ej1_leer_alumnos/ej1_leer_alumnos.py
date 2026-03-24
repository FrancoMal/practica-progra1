# =============================================================================
# EJERCICIO 1 - Leer alumnos con legajo menor a 1100000
# =============================================================================
# Consigna: Leer el archivo alumnos.txt (formato: legajo;nombre) e imprimir
# por pantalla solamente aquellos alumnos cuyo legajo sea menor a 1100000.
# =============================================================================
# Reglas de la cursada:
# - NUNCA usar readlines(), read() sin parametro, ni list(arch) -> PROHIBIDO
# - Usar readline() con while, o for linea in arch
# - Siempre try/except/finally con close() protegido por except NameError
# - FileNotFoundError ANTES de OSError
# - Usar seek(0) en vez de cerrar y reabrir en el mismo modo
# =============================================================================

print("=" * 60)
print("EJERCICIO 1 - Alumnos con legajo < 1100000")
print("=" * 60)

try:
    arch = open("alumnos.txt", "rt")
    for linea in arch:
        linea = linea.strip()
        if linea != "":
            campos = linea.split(";")
            legajo = int(campos[0])
            nombre = campos[1]
            if legajo < 1100000:
                print(f"Legajo: {legajo} - Nombre: {nombre}")
except FileNotFoundError:
    print("Error: no se encontro el archivo alumnos.txt")
except OSError:
    print("Error al acceder al archivo alumnos.txt")
finally:
    try:
        arch.close()
    except NameError:
        pass
