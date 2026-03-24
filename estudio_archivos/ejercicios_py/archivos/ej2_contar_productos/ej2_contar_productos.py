# =============================================================================
# EJERCICIO 2 - Contar productos con precio mayor a 1000
# =============================================================================
# Consigna: Leer el archivo productos.txt (formato: codigo;descripcion;precio)
# y contar cuantos productos cuestan mas de 1000 pesos. Mostrar la cantidad
# total y listar esos productos.
# =============================================================================
# Reglas de la cursada:
# - NUNCA usar readlines(), read() sin parametro, ni list(arch) -> PROHIBIDO
# - Usar readline() con while, o for linea in arch
# - Siempre try/except/finally con close() protegido por except NameError
# - FileNotFoundError ANTES de OSError
# - Usar seek(0) en vez de cerrar y reabrir en el mismo modo
# =============================================================================

print("=" * 60)
print("EJERCICIO 2 - Productos con precio > 1000")
print("=" * 60)

try:
    arch = open("productos.txt", "r")
    contador = 0
    for linea in arch:
        linea = linea.strip()
        if linea != "":
            campos = linea.split(";")
            codigo = int(campos[0])
            descripcion = campos[1]
            precio = float(campos[2])
            if precio > 1000:
                contador += 1
                print(f"  Codigo: {codigo} - {descripcion} - ${precio:.2f}")
    print(f"Total de productos con precio mayor a $1000: {contador}")
except FileNotFoundError:
    print("Error: no se encontro el archivo productos.txt")
except OSError:
    print("Error al acceder al archivo productos.txt")
finally:
    try:
        arch.close()
    except NameError:
        pass
