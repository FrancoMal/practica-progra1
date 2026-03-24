# =============================================================================
# EJERCICIO 8 - Leer archivo JSONL linea por linea
# =============================================================================
# Consigna: Leer el archivo datos.jsonl donde cada linea es un objeto JSON
# con formato {"nombre":"...","edad":...,"nota":...}.
# Usar import json y json.loads() para parsear cada linea individualmente
# (NO se carga todo el archivo de golpe, se procesa linea por linea).
# Imprimir cada registro formateado y calcular la nota promedio.
# =============================================================================
# Reglas de la cursada:
# - NUNCA usar readlines(), read() sin parametro, ni list(arch) -> PROHIBIDO
# - Usar readline() con while, o for linea in arch
# - Siempre try/except/finally con close() protegido por except NameError
# - FileNotFoundError ANTES de OSError
# - Usar seek(0) en vez de cerrar y reabrir en el mismo modo
# =============================================================================

import json

print("=" * 60)
print("EJERCICIO 8 - Leer archivo JSONL linea por linea")
print("=" * 60)

try:
    arch = open("datos.jsonl", "r")

    suma_notas = 0
    cantidad = 0
    for linea in arch:
        linea = linea.strip()
        if linea != "":
            registro = json.loads(linea)
            nombre = registro["nombre"]
            edad = registro["edad"]
            nota = registro["nota"]
            suma_notas += nota
            cantidad += 1
            print(f"  {nombre} (edad: {edad}) - Nota: {nota}")

    if cantidad > 0:
        promedio = suma_notas / cantidad
        print(f"Cantidad de registros: {cantidad}")
        print(f"Nota promedio: {promedio:.2f}")
    else:
        print("No se encontraron registros en el archivo.")
except FileNotFoundError:
    print("Error: no se encontro el archivo datos.jsonl")
except OSError:
    print("Error al acceder al archivo datos.jsonl")
finally:
    try:
        arch.close()
    except NameError:
        pass
