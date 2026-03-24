# =============================================================================
# EJERCICIO 2 - Crear lista con append, ordenar por ultimo digito
# =============================================================================
# Consigna:
# Pedir al usuario que ingrese 8 numeros enteros positivos y guardarlos en una
# lista usando append(). Luego ordenar la lista por el ULTIMO DIGITO de cada
# numero usando sort() con key=lambda.
# Mostrar la lista original (antes de ordenar) y la lista ordenada.
#
# Ejemplo:
#   Numeros ingresados: [45, 23, 78, 11, 89, 34, 56, 92]
#   Ordenados por ultimo digito: [11, 92, 23, 34, 45, 56, 78, 89]
#
# Pista: el ultimo digito de un numero se obtiene con numero % 10
# =============================================================================
# Recordar: sort(key=lambda x: ...) ordena segun el valor que devuelve la lambda.
# sort() modifica la lista original, si se quiere conservar la original hay que
# copiarla antes con lista[:] o list(lista).
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 2
# =============================================================================
# numeros = []
#
# for i in range(8):
#     num = int(input(f"Ingrese el numero {i + 1}: "))
#     numeros.append(num)
#
# copia_original = list(numeros)
#
# numeros.sort(key=lambda x: x % 10)
#
# print(f"Numeros ingresados: {copia_original}")
# print(f"Ordenados por ultimo digito: {numeros}")
# =============================================================================
