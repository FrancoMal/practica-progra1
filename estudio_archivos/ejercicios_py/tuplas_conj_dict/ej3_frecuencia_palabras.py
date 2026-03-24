# =============================================================================
# EJERCICIO 3 - DICCIONARIOS: Frecuencia de palabras
# =============================================================================
# Consigna:
# Pedir al usuario una frase y contar la frecuencia de cada palabra
# usando un diccionario. Utilizar el metodo get() o el operador 'in'
# para verificar si la palabra ya existe en el diccionario.
# Mostrar cada palabra con su cantidad de apariciones.
# Convertir todo a minusculas para evitar duplicados por mayusculas.
# =============================================================================
# Recordar: dict.get(clave, valor_por_defecto) devuelve el valor si la clave
# existe, o el valor_por_defecto si no existe (sin lanzar error).
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 3
# =============================================================================
# frase = input("Ingrese una frase: ")
# frase = frase.lower()
# palabras = frase.split()
#
# frecuencia = {}
#
# # Opcion 1: usando get()
# for palabra in palabras:
#     frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
#
# # Opcion 2 (alternativa): usando 'in'
# # for palabra in palabras:
# #     if palabra in frecuencia:
# #         frecuencia[palabra] += 1
# #     else:
# #         frecuencia[palabra] = 1
#
# print("\n=== Frecuencia de palabras ===")
# for palabra, cantidad in frecuencia.items():
#     print(f"'{palabra}' aparece {cantidad} vez/veces")
#
# print(f"\nTotal de palabras distintas: {len(frecuencia)}")
# print(f"Total de palabras en la frase: {len(palabras)}")
# =============================================================================
