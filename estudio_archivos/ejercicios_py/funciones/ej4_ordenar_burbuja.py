# =============================================================================
# EJERCICIO 4
# =============================================================================
# Consigna:
#   Escribir una funcion llamada "ordenar_lista" que reciba una lista de
#   numeros como parametro y la ordene de menor a mayor. NO usar sort()
#   ni sorted(). Implementar el ordenamiento manualmente (por ejemplo,
#   metodo burbuja).
#
#   IMPORTANTE: como la lista es un parametro mutable, la funcion la modifica
#   directamente. No es necesario retornar nada.
#
#   En el programa principal, cargar una lista, mostrarla antes de ordenar,
#   invocar la funcion y mostrarla despues de ordenar.
#
#   Ejemplo:
#       Cuantos numeros desea ingresar? 5
#       Ingrese el numero 1: 34
#       Ingrese el numero 2: 12
#       Ingrese el numero 3: 45
#       Ingrese el numero 4: 7
#       Ingrese el numero 5: 23
#       Lista original: [34, 12, 45, 7, 23]
#       Lista ordenada: [7, 12, 23, 34, 45]
# =============================================================================
# TU CODIGO ACA:


# FUNCION:



# PROGRAMA PRINCIPAL:
# (descomentar para usar)
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

# --- SOLUCION EJERCICIO 4 ---------------------------------------------------
# def ordenar_lista(lista):
#     n = len(lista)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if lista[j] > lista[j + 1]:
#                 auxiliar = lista[j]
#                 lista[j] = lista[j + 1]
#                 lista[j + 1] = auxiliar
#
#
# # Programa principal
# cantidad = int(input("Cuantos numeros desea ingresar? "))
# lista = []
# for i in range(cantidad):
#     valor = float(input("Ingrese el numero " + str(i + 1) + ": "))
#     lista.append(valor)
#
# print("Lista original:", lista)
# ordenar_lista(lista)
# print("Lista ordenada:", lista)
# -----------------------------------------------------------------------------
