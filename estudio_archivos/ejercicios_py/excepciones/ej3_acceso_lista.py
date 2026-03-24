# =============================================================================
# Ejercicios de Excepciones - Clase 7
# =============================================================================


# =============================================================================
# Ejercicio 3
# =============================================================================
# Consigna:
# Dada la lista frutas = ["manzana", "banana", "naranja", "uva", "pera"],
# pedir al usuario un indice (numero entero) e intentar acceder al elemento
# en esa posicion. Manejar las siguientes situaciones:
#   - ValueError: si el usuario no ingresa un numero entero.
#   - IndexError: si el indice esta fuera del rango de la lista.
# Usar el bloque else para imprimir el valor encontrado en caso de exito.
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
#
#
# =============================================================================
# Solucion Ejercicio 3
# =============================================================================
# frutas = ["manzana", "banana", "naranja", "uva", "pera"]
#
# try:
#     indice = int(input("Ingrese un indice para acceder a la lista de frutas: "))
#     fruta = frutas[indice]
# except ValueError:
#     print("Error: debe ingresar un numero entero.")
# except IndexError:
#     print(f"Error: el indice esta fuera de rango. Use un valor entre 0 y {len(frutas) - 1}.")
# else:
#     print(f"La fruta en la posicion {indice} es: {fruta}")
# =============================================================================
