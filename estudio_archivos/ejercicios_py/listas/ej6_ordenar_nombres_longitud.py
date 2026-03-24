# =============================================================================
# EJERCICIO 6 - Ordenar nombres por longitud y luego alfabeticamente
# =============================================================================
# Consigna:
# Dada una lista de nombres (puede estar hardcodeada o pedida al usuario),
# ordenar la lista usando sort() con una key que ordene PRIMERO por longitud
# del nombre (de menor a mayor) y, en caso de empate en longitud, ALFABETICAMENTE.
# Esto se logra usando sort(key=lambda x: (len(x), x.lower())), que devuelve
# una tupla como criterio de ordenamiento.
# Mostrar la lista original y la lista ordenada.
#
# Ejemplo:
#   Lista original: ["Maria", "Ana", "Pedro", "Luz", "Carlos", "Sol", "Juan"]
#   Lista ordenada: ["Ana", "Luz", "Sol", "Juan", "Maria", "Pedro", "Carlos"]
# =============================================================================
# Recordar: cuando sort() recibe una tupla como key, ordena por el primer
# elemento de la tupla y, en caso de empate, por el segundo.
# x.lower() se usa para que la comparacion alfabetica no distinga mayusculas.
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 6
# =============================================================================
# nombres = ["Maria", "Ana", "Pedro", "Luz", "Carlos", "Sol", "Juan"]
#
# print(f"Lista original: {nombres}")
#
# copia_original = list(nombres)
#
# nombres.sort(key=lambda x: (len(x), x.lower()))
#
# print(f"Lista ordenada: {nombres}")
# =============================================================================
