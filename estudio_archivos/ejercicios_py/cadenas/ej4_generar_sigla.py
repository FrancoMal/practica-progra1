# =============================================================================
# EJERCICIO 4
# =============================================================================
# Consigna:
# Solicitar al usuario una frase y generar la sigla formada por la primera
# letra de cada palabra, toda en mayusculas.
# Ejemplo: "Universidad de Buenos Aires" -> "UDBA"
# Ejemplo: "organizacion de las naciones unidas" -> "ODLNU"
# Recordar: .split() devuelve una NUEVA lista, .upper() devuelve una NUEVA cadena.
# =============================================================================
# Tip: recorrer la lista de palabras obtenida con split(), tomar el primer
# caracter de cada una con indice [0] y concatenar. La concatenacion con +
# genera una NUEVA cadena cada vez (inmutabilidad).
# =============================================================================

































# -----------------------------------------------------------------------------
# SOLUCION EJERCICIO 4
# -----------------------------------------------------------------------------
# frase = input("Ingrese una frase: ")
#
# palabras = frase.split()    # devuelve una NUEVA lista
# sigla = ""                  # cadena vacia inicial
#
# for palabra in palabras:
#     sigla = sigla + palabra[0]   # concatenar genera una NUEVA cadena cada vez
#
# sigla = sigla.upper()   # .upper() devuelve una NUEVA cadena
#
# print(f"Frase: {frase}")
# print(f"Sigla: {sigla}")
# -----------------------------------------------------------------------------
