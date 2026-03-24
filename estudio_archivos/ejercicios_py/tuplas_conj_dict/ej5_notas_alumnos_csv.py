# =============================================================================
# EJERCICIO 5 - COMBINADO: Notas de alumnos desde CSV
# =============================================================================
# Consigna:
# Leer un archivo CSV con formato: nombre;materia;nota
# Crear un diccionario donde:
#   - La clave es el nombre del alumno (str)
#   - El valor es una lista de tuplas (materia, nota)
# Luego imprimir el promedio de notas de cada alumno.
#
# Ejemplo de contenido del archivo "notas.csv":
#   Juan;Matematica;8
#   Maria;Fisica;9
#   Juan;Fisica;7
#   Maria;Matematica;10
#   Pedro;Matematica;6
#   Pedro;Fisica;5
#
# Si el archivo no existe, mostrar un mensaje de error.
# =============================================================================
# Recordar: las tuplas son ideales para almacenar pares (materia, nota)
# porque esos datos no deberian modificarse una vez leidos.
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 5
# =============================================================================
# # Primero creamos el archivo CSV de ejemplo para poder probarlo
# datos_ejemplo = """Juan;Matematica;8
# Maria;Fisica;9
# Juan;Fisica;7
# Maria;Matematica;10
# Pedro;Matematica;6
# Pedro;Fisica;5
# Ana;Matematica;9
# Ana;Fisica;8
# Ana;Quimica;7"""
#
# # Crear el archivo de ejemplo
# with open("notas.csv", "w") as archivo:
#     archivo.write(datos_ejemplo)
# print("Archivo 'notas.csv' creado con datos de ejemplo.\n")
#
# # Leer el archivo y procesar los datos
# alumnos = {}
#
# try:
#     with open("notas.csv", "r") as archivo:
#         for linea in archivo:
#             linea = linea.strip()
#             if linea == "":
#                 continue
#             partes = linea.split(";")
#             nombre = partes[0]
#             materia = partes[1]
#             nota = float(partes[2])
#
#             tupla_materia_nota = (materia, nota)
#
#             if nombre in alumnos:
#                 alumnos[nombre].append(tupla_materia_nota)
#             else:
#                 alumnos[nombre] = [tupla_materia_nota]
#
#     print("=== Notas por alumno ===")
#     for alumno, materias in alumnos.items():
#         print(f"\n{alumno}:")
#         suma_notas = 0
#         for materia, nota in materias:
#             print(f"  {materia}: {nota}")
#             suma_notas += nota
#         promedio = suma_notas / len(materias)
#         print(f"  Promedio: {promedio:.2f}")
#
# except FileNotFoundError:
#     print("Error: no se encontro el archivo 'notas.csv'.")
# =============================================================================
