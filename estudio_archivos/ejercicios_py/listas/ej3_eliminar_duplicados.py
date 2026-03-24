# =============================================================================
# EJERCICIO 3 - Eliminar duplicados sin usar set
# =============================================================================
# Consigna:
# Dada una lista de numeros enteros (puede estar hardcodeada o pedida al usuario),
# eliminar los elementos duplicados SIN usar set(). Se puede resolver de dos formas:
#   a) Usando count() y remove() sobre la misma lista
#   b) Creando una nueva lista y agregando solo si el elemento no esta ya
# Implementar con la estrategia que prefieras.
# Mostrar la lista original y la lista sin duplicados.
#
# Ejemplo:
#   Lista original: [4, 2, 7, 2, 4, 8, 7, 3, 4, 1]
#   Lista sin duplicados: [4, 2, 7, 8, 3, 1]
# =============================================================================
# Recordar: count(x) devuelve cuantas veces aparece x en la lista.
# Si se usa remove() mientras se recorre, tener cuidado con los indices.
# La forma mas segura es crear una lista nueva.
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 3
# =============================================================================
# lista_original = [4, 2, 7, 2, 4, 8, 7, 3, 4, 1]
#
# print(f"Lista original: {lista_original}")
#
# # Estrategia: crear lista nueva sin duplicados
# sin_duplicados = []
# for elemento in lista_original:
#     if elemento not in sin_duplicados:
#         sin_duplicados.append(elemento)
#
# print(f"Lista sin duplicados: {sin_duplicados}")
# =============================================================================
