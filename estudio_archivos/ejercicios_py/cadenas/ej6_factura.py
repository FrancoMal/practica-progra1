# =============================================================================
# EJERCICIO 6
# =============================================================================
# Consigna:
# Simular la impresion de una factura. Solicitar al usuario que ingrese
# items de una factura: cada item tiene una descripcion (cadena) y un precio
# (float). El usuario ingresa items hasta que escribe "fin" como descripcion.
# Luego, imprimir una tabla alineada usando f-strings con formato:
#   - Descripcion alineada a la izquierda en 30 caracteres
#   - Precio alineado a la derecha en 10 caracteres con 2 decimales
#   - Una linea separadora con "-" * 42
#   - El total alineado de la misma forma
# Recordar: los f-strings generan NUEVAS cadenas. El operador * con cadenas
# tambien genera una NUEVA cadena (inmutabilidad).
# =============================================================================
# Tip: f"{'texto':<30}" alinea a la izquierda en 30 chars.
#      f"{valor:>10.2f}" alinea a la derecha en 10 chars con 2 decimales.
# =============================================================================

































# -----------------------------------------------------------------------------
# SOLUCION EJERCICIO 6
# -----------------------------------------------------------------------------
# descripciones = []
# precios = []
#
# while True:
#     descripcion = input("Descripcion del item (o 'fin' para terminar): ")
#     if descripcion.lower() == "fin":    # .lower() devuelve una NUEVA cadena
#         break
#     precio = float(input("Precio: "))
#     descripciones.append(descripcion)
#     precios.append(precio)
#
# # Imprimir encabezado (f-string genera una NUEVA cadena)
# print()
# print(f"{'DESCRIPCION':<30} {'PRECIO':>10}")
# print("-" * 42)    # operador * genera una NUEVA cadena de 42 guiones
#
# total = 0.0
# for i in range(len(descripciones)):
#     print(f"{descripciones[i]:<30} {precios[i]:>10.2f}")
#     total += precios[i]
#
# print("-" * 42)
# print(f"{'TOTAL':<30} {total:>10.2f}")
# -----------------------------------------------------------------------------
