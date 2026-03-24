# =============================================================================
# EJERCICIO 4 - Rotar una lista N posiciones a la derecha
# =============================================================================
# Consigna:
# Dada una lista de elementos (puede ser de numeros o de strings) y un numero N,
# rotar la lista N posiciones a la derecha. NO usar slicing directo como solucion
# trivial (es decir, no hacer simplemente lista[-n:] + lista[:-n]).
# Implementar la rotacion usando un bucle que mueva elementos uno a uno:
# en cada paso, sacar el ultimo elemento (con pop()) e insertarlo al principio
# (con insert(0, ...)), repitiendo N veces.
# Mostrar la lista antes y despues de la rotacion.
#
# Ejemplo:
#   Lista original: [1, 2, 3, 4, 5, 6, 7]
#   Posiciones a rotar: 3
#   Lista rotada: [5, 6, 7, 1, 2, 3, 4]
# =============================================================================
# Recordar: pop() sin argumento saca el ultimo elemento y lo devuelve.
# insert(0, valor) inserta un valor al principio de la lista.
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 4
# =============================================================================
# lista = [1, 2, 3, 4, 5, 6, 7]
# n = int(input("Cuantas posiciones rotar a la derecha: "))
#
# print(f"Lista original: {lista}")
#
# # Ajustar N por si es mayor que el largo de la lista
# n = n % len(lista)
#
# for i in range(n):
#     ultimo = lista.pop()
#     lista.insert(0, ultimo)
#
# print(f"Lista rotada: {lista}")
# =============================================================================
