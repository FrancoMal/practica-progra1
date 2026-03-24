# =============================================================================
# EJERCICIO 2
# =============================================================================
# Consigna:
# Solicitar al usuario una frase e invertir el orden de las palabras
# SIN invertir las letras de cada palabra.
# Ejemplo: "hola mundo cruel" -> "cruel mundo hola"
# Usar los metodos .split() y " ".join() para resolverlo.
# Recordar: .split() devuelve una NUEVA lista, .join() devuelve una NUEVA cadena.
# =============================================================================
# Tip: split() sin argumentos separa por espacios. Las listas si son mutables
# y se pueden invertir con .reverse() o slicing [::-1].
# =============================================================================






























# -----------------------------------------------------------------------------
# SOLUCION EJERCICIO 2
# -----------------------------------------------------------------------------
# frase = input("Ingrese una frase: ")
#
# palabras = frase.split()        # devuelve una NUEVA lista de palabras
# palabras_invertidas = palabras[::-1]   # slicing genera una NUEVA lista
#
# frase_invertida = " ".join(palabras_invertidas)  # .join() genera una NUEVA cadena
#
# print(f"Frase original:  {frase}")
# print(f"Frase invertida: {frase_invertida}")
# -----------------------------------------------------------------------------
