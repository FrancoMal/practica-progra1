# =============================================================================
# Ejercicios de Excepciones - Clase 7
# =============================================================================


# =============================================================================
# Ejercicio 5
# =============================================================================
# Consigna:
# Escribir una funcion validar_fecha(dia, mes, anio) que reciba tres enteros
# representando una fecha. Usar assert para verificar:
#   - El dia debe estar entre 1 y 31.
#   - El mes debe estar entre 1 y 12.
#   - El anio debe ser mayor a 0.
# Si alguna condicion no se cumple, el assert lanzara un AssertionError.
# Capturar el AssertionError e imprimir un mensaje indicando que la fecha
# no es valida. Si la fecha es valida, imprimir la fecha formateada.
# =============================================================================
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# =============================================================================
# Solucion Ejercicio 5
# =============================================================================
# def validar_fecha(dia, mes, anio):
#     assert 1 <= dia <= 31, f"Dia invalido: {dia}. Debe estar entre 1 y 31."
#     assert 1 <= mes <= 12, f"Mes invalido: {mes}. Debe estar entre 1 y 12."
#     assert anio > 0, f"Anio invalido: {anio}. Debe ser mayor a 0."
#     return f"{dia:02d}/{mes:02d}/{anio:04d}"
#
# try:
#     d = int(input("Ingrese el dia: "))
#     m = int(input("Ingrese el mes: "))
#     a = int(input("Ingrese el anio: "))
#     fecha = validar_fecha(d, m, a)
# except ValueError:
#     print("Error: debe ingresar numeros enteros.")
# except AssertionError as e:
#     print(f"Error de validacion: {e}")
# else:
#     print(f"La fecha ingresada es: {fecha}")
# =============================================================================
