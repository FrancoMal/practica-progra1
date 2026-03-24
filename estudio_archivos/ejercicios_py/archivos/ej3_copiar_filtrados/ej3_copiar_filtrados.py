# =============================================================================
# EJERCICIO 3 - Copiar alumnos con legajo par a aprobados.txt
# =============================================================================
# Consigna: Leer el archivo alumnos.txt (formato: legajo;nombre) y copiar
# a un nuevo archivo llamado aprobados.txt solamente aquellos alumnos cuyo
# legajo sea par.
# =============================================================================
# Reglas de la cursada:
# - NUNCA usar readlines(), read() sin parametro, ni list(arch) -> PROHIBIDO
# - Usar readline() con while, o for linea in arch
# - Siempre try/except/finally con close() protegido por except NameError
# - FileNotFoundError ANTES de OSError
# - Un write() por registro, agregar \n manualmente
# - Usar seek(0) en vez de cerrar y reabrir en el mismo modo
# =============================================================================

print("=" * 60)
print("EJERCICIO 3 - Copiar legajos pares a aprobados.txt")
print("=" * 60)

try:
    arch_entrada = open("alumnos.txt", "r")
    arch_salida = open("aprobados.txt", "w")
    cantidad = 0
    for linea in arch_entrada:
        linea = linea.strip()
        if linea != "":
            campos = linea.split(";")
            legajo = int(campos[0])
            nombre = campos[1]
            if legajo % 2 == 0:
                arch_salida.write(campos[0] + ";" + nombre + "\n")
                cantidad += 1
                print(f"  Copiado: {legajo} - {nombre}")
    print(f"Se copiaron {cantidad} alumnos con legajo par a aprobados.txt")
except FileNotFoundError:
    print("Error: no se encontro el archivo alumnos.txt")
except OSError:
    print("Error al acceder a los archivos")
finally:
    try:
        arch_entrada.close()
    except NameError:
        pass
    try:
        arch_salida.close()
    except NameError:
        pass
