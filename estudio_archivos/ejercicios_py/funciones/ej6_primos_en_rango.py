# =============================================================================
# EJERCICIO 6 (INTEGRADOR)
# =============================================================================
# Consigna:
#   Escribir un programa completo con las siguientes funciones:
#
#   1) "verificar_si_es_primo": recibe un numero entero y devuelve True si
#      es primo, False en caso contrario. Un numero es primo si es mayor
#      que 1 y solo es divisible por 1 y por si mismo.
#      (NO retornar dentro del bucle, usar una variable bandera)
#
#   2) "buscar_primos_en_rango": recibe dos numeros (inicio y fin) y devuelve
#      una lista con todos los numeros primos en ese rango. Debe invocar
#      a la funcion verificar_si_es_primo para cada numero.
#
#   Programa principal:
#      - Pedir al usuario un rango (inicio y fin)
#      - Invocar buscar_primos_en_rango
#      - Mostrar la lista de primos encontrados y cuantos son
#
#   Ejemplo:
#       Ingrese el inicio del rango: 1
#       Ingrese el fin del rango: 20
#       Primos encontrados: [2, 3, 5, 7, 11, 13, 17, 19]
#       Cantidad de primos: 8
# =============================================================================
# TU CODIGO ACA:


# FUNCIONES (van las dos antes del programa principal):



# PROGRAMA PRINCIPAL:
# (descomentar para usar)
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

# --- SOLUCION EJERCICIO 6 ---------------------------------------------------
# def verificar_si_es_primo(numero):
#     es_primo = True
#     if numero <= 1:
#         es_primo = False
#     else:
#         for i in range(2, numero):
#             if numero % i == 0:
#                 es_primo = False
#     return es_primo
#
#
# def buscar_primos_en_rango(inicio, fin):
#     lista_primos = []
#     for num in range(inicio, fin + 1):
#         if verificar_si_es_primo(num):
#             lista_primos.append(num)
#     return lista_primos
#
#
# # Programa principal
# inicio = int(input("Ingrese el inicio del rango: "))
# fin = int(input("Ingrese el fin del rango: "))
# primos = buscar_primos_en_rango(inicio, fin)
# print("Primos encontrados:", primos)
# print("Cantidad de primos:", len(primos))
# -----------------------------------------------------------------------------
