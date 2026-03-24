# =============================================================================
# EJERCICIO 4 - Monto total y promedio de ventas
# =============================================================================
# Consigna: Leer el archivo ventas.txt (formato: producto;cantidad;precio)
# y calcular el monto total de todas las ventas y el promedio por venta.
# Monto de cada venta = cantidad * precio.
# =============================================================================
# Reglas de la cursada:
# - NUNCA usar readlines(), read() sin parametro, ni list(arch) -> PROHIBIDO
# - Usar readline() con while, o for linea in arch
# - Siempre try/except/finally con close() protegido por except NameError
# - FileNotFoundError ANTES de OSError
# - Usar seek(0) en vez de cerrar y reabrir en el mismo modo
# =============================================================================

print("=" * 60)
print("EJERCICIO 4 - Monto total y promedio de ventas")
print("=" * 60)

try:
    arch = open("ventas.txt", "r")
    monto_total = 0
    cant_ventas = 0
    for linea in arch:
        linea = linea.strip()
        if linea != "":
            campos = linea.split(";")
            producto = campos[0]
            cantidad = int(campos[1])
            precio = float(campos[2])
            monto = cantidad * precio
            monto_total += monto
            cant_ventas += 1
            print(f"  {producto}: {cantidad} x ${precio:.2f} = ${monto:.2f}")
    if cant_ventas > 0:
        promedio = monto_total / cant_ventas
        print(f"Monto total de ventas: ${monto_total:.2f}")
        print(f"Cantidad de ventas: {cant_ventas}")
        print(f"Promedio por venta: ${promedio:.2f}")
    else:
        print("No se encontraron ventas en el archivo.")
except FileNotFoundError:
    print("Error: no se encontro el archivo ventas.txt")
except OSError:
    print("Error al acceder al archivo ventas.txt")
finally:
    try:
        arch.close()
    except NameError:
        pass
