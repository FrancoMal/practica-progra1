# =============================================================================
# EJERCICIO 5
# =============================================================================
# Consigna:
# Solicitar al usuario una frase que puede contener vocales acentuadas
# (a, e, i, o, u) y reemplazarlas por sus equivalentes sin acento.
# Usar la tecnica de CADENAS PARALELAS: una cadena con las vocales acentuadas
# y otra con las vocales sin acento, en el mismo orden. Buscar la posicion
# con .index() y reemplazar usando esa posicion en la cadena paralela.
# Ejemplo: "La programacion esta en accion" -> "La programacion esta en accion"
# Recordar: las cadenas son INMUTABLES, se debe construir una NUEVA cadena
# caracter por caracter.
# =============================================================================
# Tip: .index() devuelve la posicion de un caracter en una cadena.
# Si el caracter no esta, lanza ValueError -> usar "in" antes para verificar.
# =============================================================================

































# -----------------------------------------------------------------------------
# SOLUCION EJERCICIO 5
# -----------------------------------------------------------------------------
# frase = input("Ingrese una frase (puede tener tildes): ")
#
# con_acento = "aeiouAEIOU"
# sin_acento = "aeiouAEIOU"
#
# nueva_frase = ""    # se construye una NUEVA cadena caracter por caracter
#
# for caracter in frase:
#     if caracter in con_acento:
#         posicion = con_acento.index(caracter)   # buscar posicion en paralela
#         nueva_frase = nueva_frase + sin_acento[posicion]  # NUEVA cadena cada vez
#     else:
#         nueva_frase = nueva_frase + caracter    # NUEVA cadena cada vez
#
# print(f"Original:    {frase}")
# print(f"Sin acentos: {nueva_frase}")
# -----------------------------------------------------------------------------
