# =============================================================================
# EJERCICIO 1 - Leer numeros hasta -1, guardar en lista, imprimir mayores al promedio
# =============================================================================
# Consigna:
# Leer numeros enteros por teclado hasta que el usuario ingrese -1 (el -1 NO
# se guarda en la lista). Guardar todos los numeros en una lista.
# Calcular el promedio de los numeros ingresados.
# Luego recorrer la lista e imprimir solo los numeros que sean mayores al promedio.
# Mostrar tambien el promedio calculado.
#
# Ejemplo:
#   Ingrese un numero (-1 para terminar): 10
#   Ingrese un numero (-1 para terminar): 4
#   Ingrese un numero (-1 para terminar): 8
#   Ingrese un numero (-1 para terminar): 2
#   Ingrese un numero (-1 para terminar): 6
#   Ingrese un numero (-1 para terminar): -1
#   Promedio: 6.0
#   Numeros mayores al promedio: 10, 8
# =============================================================================
# Recordar: el -1 es solo el centinela de corte, no forma parte de los datos.
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 1
# =============================================================================
# numeros = []
#
# num = int(input("Ingrese un numero (-1 para terminar): "))
# while num != -1:
#     numeros.append(num)
#     num = int(input("Ingrese un numero (-1 para terminar): "))
#
# if len(numeros) > 0:
#     suma = 0
#     for n in numeros:
#         suma = suma + n
#     promedio = suma / len(numeros)
#
#     print(f"Promedio: {promedio}")
#
#     print("Numeros mayores al promedio:")
#     for n in numeros:
#         if n > promedio:
#             print(n)
# else:
#     print("No se ingresaron numeros.")
# =============================================================================
