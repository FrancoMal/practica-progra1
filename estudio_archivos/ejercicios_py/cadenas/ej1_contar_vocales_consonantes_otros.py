# =============================================================================
# EJERCICIO 1
# =============================================================================
# Consigna:
# Solicitar al usuario una frase y contar cuantas vocales, consonantes
# y otros caracteres (espacios, signos de puntuacion, numeros, etc.) contiene.
# Mostrar los resultados por pantalla.
# Recordar: las cadenas son inmutables, usamos metodos como .lower() que
# devuelven una NUEVA cadena.
# =============================================================================
# Tip: usar el operador "in" para verificar pertenencia a una cadena.
# =============================================================================






























# -----------------------------------------------------------------------------
# SOLUCION EJERCICIO 1
# -----------------------------------------------------------------------------
# frase = input("Ingrese una frase: ")
#
# vocales = 0
# consonantes = 0
# otros = 0
#
# letras_vocales = "aeiou"
# letras_consonantes = "bcdfghjklmnpqrstvwxyz"
#
# for caracter in frase.lower():      # .lower() devuelve una NUEVA cadena
#     if caracter in letras_vocales:
#         vocales += 1
#     elif caracter in letras_consonantes:
#         consonantes += 1
#     else:
#         otros += 1
#
# print(f"Vocales: {vocales}")
# print(f"Consonantes: {consonantes}")
# print(f"Otros caracteres: {otros}")
# -----------------------------------------------------------------------------
