# =============================================================================
# Ejercicios de Excepciones - Clase 7
# =============================================================================


# =============================================================================
# Ejercicio 4
# =============================================================================
# Consigna:
# Crear una calculadora simple con un menu que ofrezca las operaciones:
# 1) Sumar, 2) Restar, 3) Multiplicar, 4) Dividir, 5) Salir.
# Pedir al usuario la opcion y luego dos numeros. Manejar las excepciones:
#   - ValueError: si el usuario ingresa algo que no es un numero.
#   - ZeroDivisionError: si intenta dividir por cero.
# Usar finally para imprimir un mensaje de despedida al salir del programa.
# =============================================================================
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
#
# =============================================================================
# Solucion Ejercicio 4
# =============================================================================
# def calculadora():
#     while True:
#         print("\n--- Calculadora ---")
#         print("1) Sumar")
#         print("2) Restar")
#         print("3) Multiplicar")
#         print("4) Dividir")
#         print("5) Salir")
#
#         try:
#             opcion = int(input("Elija una opcion: "))
#
#             if opcion == 5:
#                 break
#
#             if opcion < 1 or opcion > 5:
#                 print("Opcion no valida. Elija entre 1 y 5.")
#                 continue
#
#             num1 = float(input("Ingrese el primer numero: "))
#             num2 = float(input("Ingrese el segundo numero: "))
#
#             if opcion == 1:
#                 resultado = num1 + num2
#             elif opcion == 2:
#                 resultado = num1 - num2
#             elif opcion == 3:
#                 resultado = num1 * num2
#             elif opcion == 4:
#                 resultado = num1 / num2
#
#         except ValueError:
#             print("Error: debe ingresar un valor numerico valido.")
#         except ZeroDivisionError:
#             print("Error: no se puede dividir por cero.")
#         else:
#             print(f"El resultado es: {resultado}")
#         finally:
#             print("Gracias por usar la calculadora. Hasta luego!")
#
# calculadora()
# =============================================================================
