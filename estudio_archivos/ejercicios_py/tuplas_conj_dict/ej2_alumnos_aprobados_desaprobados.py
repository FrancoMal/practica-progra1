# =============================================================================
# EJERCICIO 2 - CONJUNTOS: Alumnos aprobados y desaprobados
# =============================================================================
# Consigna:
# Dadas dos listas de alumnos (aprobados en parcial 1 y aprobados en parcial 2),
# usar conjuntos (sets) para determinar:
#   a) Alumnos que aprobaron AMBOS parciales (interseccion)
#   b) Alumnos que aprobaron AL MENOS UN parcial (union)
#   c) Alumnos que aprobaron SOLO el parcial 1 (diferencia)
#   d) Alumnos que aprobaron SOLO el parcial 2 (diferencia)
#   e) Alumnos que aprobaron exactamente uno de los dos (diferencia simetrica)
# Las listas pueden tener nombres repetidos; los sets los eliminan automaticamente.
# =============================================================================
# Recordar: los sets no permiten duplicados y no tienen orden.
# Operaciones: & (interseccion), | (union), - (diferencia), ^ (dif. simetrica)
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 2
# =============================================================================
# aprobados_parcial1 = ["Ana", "Juan", "Pedro", "Maria", "Luis", "Ana"]
# aprobados_parcial2 = ["Maria", "Luis", "Carlos", "Sofia", "Juan", "Carlos"]
#
# set_parcial1 = set(aprobados_parcial1)
# set_parcial2 = set(aprobados_parcial2)
#
# print("=== Analisis de aprobados con conjuntos ===")
# print(f"Aprobaron parcial 1: {set_parcial1}")
# print(f"Aprobaron parcial 2: {set_parcial2}")
#
# # a) Aprobaron AMBOS parciales (interseccion)
# ambos = set_parcial1 & set_parcial2
# print(f"\na) Aprobaron AMBOS parciales: {ambos}")
#
# # b) Aprobaron AL MENOS UN parcial (union)
# al_menos_uno = set_parcial1 | set_parcial2
# print(f"b) Aprobaron al menos un parcial: {al_menos_uno}")
#
# # c) Aprobaron SOLO el parcial 1 (diferencia)
# solo_parcial1 = set_parcial1 - set_parcial2
# print(f"c) Aprobaron SOLO parcial 1: {solo_parcial1}")
#
# # d) Aprobaron SOLO el parcial 2 (diferencia)
# solo_parcial2 = set_parcial2 - set_parcial1
# print(f"d) Aprobaron SOLO parcial 2: {solo_parcial2}")
#
# # e) Aprobaron exactamente uno (diferencia simetrica)
# exactamente_uno = set_parcial1 ^ set_parcial2
# print(f"e) Aprobaron exactamente un parcial: {exactamente_uno}")
# =============================================================================
