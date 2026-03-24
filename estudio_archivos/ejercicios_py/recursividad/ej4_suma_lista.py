# =============================================================================
# EJERCICIO 4: Suma de elementos de una lista recursivamente
# =============================================================================
# Consigna:
# Escribir una funcion recursiva llamada "suma_lista" que reciba una lista
# de numeros y un indice, y devuelva la suma de todos los elementos.
# Se usa el indice como parametro para recorrer la lista sin usar for/while.
# Caso base: si el indice es igual al largo de la lista, retornar 0
#   (ya no quedan elementos por sumar)
# Caso recursivo: lista[indice] + suma_lista(lista, indice + 1)
# Al llamar a la funcion por primera vez, el indice debe ser 0.
# Ejemplo: suma_lista([3, 7, 2, 5], 0) -> 17
# =============================================================================


# RESOLVER ACA

def suma_lista():
    pass
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

# --- Solucion ---
# def suma_lista(lista, indice):
#     # Caso base: el indice llego al final de la lista
#     if indice == len(lista):
#         return 0
#     # Caso recursivo: sumar el elemento actual + la suma del resto
#     return lista[indice] + suma_lista(lista, indice + 1)
