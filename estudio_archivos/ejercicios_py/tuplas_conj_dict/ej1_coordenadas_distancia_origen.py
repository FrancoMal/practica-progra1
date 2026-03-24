# =============================================================================
# EJERCICIO 1 - TUPLAS: Coordenadas y distancia al origen
# =============================================================================
# Consigna:
# Leer 5 coordenadas (x, y) como tuplas, guardarlas en una lista,
# y encontrar la coordenada mas lejana al origen (0, 0).
# La distancia al origen se calcula como: sqrt(x^2 + y^2)
# Mostrar todas las coordenadas con su distancia y cual es la mas lejana.
# =============================================================================
# Recordar: las tuplas son inmutables, ideales para representar coordenadas
# ya que un punto (x, y) no deberia cambiar una vez definido.
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 1
# =============================================================================
# import math
#
# coordenadas = []
#
# print("=== Coordenadas y distancia al origen ===")
# for i in range(5):
#     x = float(input(f"Ingrese la coordenada x del punto {i + 1}: "))
#     y = float(input(f"Ingrese la coordenada y del punto {i + 1}: "))
#     punto = (x, y)
#     coordenadas.append(punto)
#
# print("\n--- Coordenadas ingresadas ---")
# mayor_distancia = -1
# punto_mas_lejano = None
#
# for punto in coordenadas:
#     distancia = math.sqrt(punto[0] ** 2 + punto[1] ** 2)
#     print(f"Punto {punto} -> distancia al origen: {distancia:.2f}")
#     if distancia > mayor_distancia:
#         mayor_distancia = distancia
#         punto_mas_lejano = punto
#
# print(f"\nEl punto mas lejano al origen es {punto_mas_lejano} "
#       f"con distancia {mayor_distancia:.2f}")
# =============================================================================
