# =============================================================================
# EJERCICIO 5 - Matriz 4x4 con numeros al azar, suma de cada fila
# =============================================================================
# Consigna:
# Crear una matriz de 4x4 (lista de listas) con numeros enteros al azar entre
# 1 y 100 usando el modulo random (random.randint(1, 100)).
# Imprimir la matriz de forma legible (una fila por linea).
# Luego calcular e imprimir la suma de cada fila.
#
# Ejemplo de salida:
#   Matriz generada:
#   [23, 45, 67, 12]
#   [89, 34, 56, 78]
#   [11, 92, 43, 65]
#   [37, 28, 71, 54]
#
#   Suma de la fila 1: 147
#   Suma de la fila 2: 257
#   Suma de la fila 3: 211
#   Suma de la fila 4: 190
# =============================================================================
# Recordar: para crear la matriz, usar un for externo para las filas y un for
# interno para las columnas. Cada fila es una lista que se agrega a la matriz.
# import random al inicio del programa.
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 5
# =============================================================================
# import random
#
# matriz = []
# for fila in range(4):
#     fila_actual = []
#     for columna in range(4):
#         fila_actual.append(random.randint(1, 100))
#     matriz.append(fila_actual)
#
# print("Matriz generada:")
# for fila in matriz:
#     print(fila)
#
# print()
# for i in range(len(matriz)):
#     suma_fila = 0
#     for elemento in matriz[i]:
#         suma_fila = suma_fila + elemento
#     print(f"Suma de la fila {i + 1}: {suma_fila}")
# =============================================================================
