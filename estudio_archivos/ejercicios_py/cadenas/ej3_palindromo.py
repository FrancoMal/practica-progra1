# =============================================================================
# EJERCICIO 3
# =============================================================================
# Consigna:
# Solicitar al usuario una cadena y verificar si es un palindromo.
# Un palindromo se lee igual de izquierda a derecha que de derecha a izquierda.
# Se deben IGNORAR los espacios y las diferencias entre mayusculas/minusculas.
# Ejemplos: "Anita lava la tina" -> es palindromo
#           "Amor a Roma"        -> es palindromo
# Recordar: .lower() y .replace() devuelven NUEVAS cadenas (inmutabilidad).
# =============================================================================
# Tip: primero limpiar la cadena (quitar espacios, pasar a minusculas),
# luego comparar con su version invertida usando slicing [::-1].
# =============================================================================

































# -----------------------------------------------------------------------------
# SOLUCION EJERCICIO 3
# -----------------------------------------------------------------------------
# cadena = input("Ingrese una cadena: ")
#
# # Cada operacion devuelve una NUEVA cadena (las cadenas son inmutables)
# cadena_limpia = cadena.lower().replace(" ", "")
#
# # Slicing [::-1] genera una NUEVA cadena invertida
# cadena_invertida = cadena_limpia[::-1]
#
# if cadena_limpia == cadena_invertida:
#     print(f'"{cadena}" ES un palindromo.')
# else:
#     print(f'"{cadena}" NO es un palindromo.')
# -----------------------------------------------------------------------------
