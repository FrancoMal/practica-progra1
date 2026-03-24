# =============================================================================
# EJERCICIO 6 - COMBINADO: Frecuencia de letras ordenada
# =============================================================================
# Consigna:
# Dado un texto (ingresado por el usuario o definido en el codigo),
# crear un diccionario donde:
#   - La clave es cada letra (sin contar espacios ni signos de puntuacion)
#   - El valor es la cantidad de veces que aparece esa letra
# Convertir todo a minusculas para unificar.
# Imprimir el resultado ordenado de mayor a menor frecuencia.
# Usar la funcion sorted() con el parametro key para ordenar.
# =============================================================================
# Recordar: sorted() puede recibir key=funcion para definir el criterio
# de ordenamiento, y reverse=True para orden descendente.
# Los items() del diccionario devuelven tuplas (clave, valor).
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 6
# =============================================================================
# texto = input("Ingrese un texto: ")
# # Alternativa con texto fijo para pruebas:
# # texto = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
#
# texto = texto.lower()
#
# frecuencia_letras = {}
#
# for caracter in texto:
#     if caracter.isalpha():  # Solo letras, ignora espacios y puntuacion
#         frecuencia_letras[caracter] = frecuencia_letras.get(caracter, 0) + 1
#
# # Ordenar de mayor a menor frecuencia
# # sorted() devuelve una lista de tuplas (clave, valor)
# # key=lambda item: item[1] ordena por el valor (frecuencia)
# letras_ordenadas = sorted(frecuencia_letras.items(),
#                           key=lambda item: item[1],
#                           reverse=True)
#
# print("\n=== Frecuencia de letras (mayor a menor) ===")
# for letra, cantidad in letras_ordenadas:
#     barra = "#" * cantidad
#     print(f"  '{letra}': {cantidad} {barra}")
#
# print(f"\nTotal de letras distintas: {len(frecuencia_letras)}")
# total_letras = sum(frecuencia_letras.values())
# print(f"Total de letras en el texto: {total_letras}")
# =============================================================================
