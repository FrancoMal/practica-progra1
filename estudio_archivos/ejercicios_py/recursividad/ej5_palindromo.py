# =============================================================================
# EJERCICIO 5: Determinar si una cadena es palindromo recursivamente
# =============================================================================
# Consigna:
# Escribir una funcion recursiva llamada "es_palindromo" que reciba una cadena
# de texto y dos indices (inicio y fin), y determine si la cadena es un
# palindromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# Caso base: si inicio >= fin, retornar True (ya se compararon todos los pares)
# Caso recursivo: si el caracter en posicion inicio es igual al caracter en
#   posicion fin, llamar recursivamente con inicio + 1 y fin - 1.
#   Si son distintos, retornar False inmediatamente.
# Al llamar por primera vez: es_palindromo(cadena, 0, len(cadena) - 1)
# Ejemplo: es_palindromo("reconocer", 0, 8) -> True
#          es_palindromo("hola", 0, 3) -> False
# =============================================================================


# RESOLVER ACA

def es_palindromo():
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
# def es_palindromo(cadena, inicio, fin):
#     # Caso base: los indices se cruzaron o son iguales, es palindromo
#     if inicio >= fin:
#         return True
#     # Si los caracteres en los extremos no coinciden, no es palindromo
#     if cadena[inicio] != cadena[fin]:
#         return False
#     # Caso recursivo: comparar el siguiente par de caracteres
#     return es_palindromo(cadena, inicio + 1, fin - 1)
