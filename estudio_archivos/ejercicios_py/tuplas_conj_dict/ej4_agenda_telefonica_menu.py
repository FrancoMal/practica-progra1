# =============================================================================
# EJERCICIO 4 - DICCIONARIOS: Agenda telefonica con menu
# =============================================================================
# Consigna:
# Crear una agenda telefonica usando un diccionario donde la clave es
# el nombre del contacto y el valor es el numero de telefono.
# Implementar un menu con las siguientes opciones:
#   1. Agregar contacto (nombre y telefono)
#   2. Buscar contacto por nombre
#   3. Eliminar contacto por nombre
#   4. Listar todos los contactos
#   5. Salir
# Validar que no se agreguen contactos duplicados y que al buscar/eliminar
# se informe si el contacto no existe.
# =============================================================================
# Recordar: las claves del diccionario deben ser inmutables (str, int, tupla).
# Los metodos utiles son: dict[clave], dict.get(), del dict[clave], dict.items()
# =============================================================================






























# =============================================================================
# SOLUCION EJERCICIO 4
# =============================================================================
# agenda = {}
#
# while True:
#     print("\n=== AGENDA TELEFONICA ===")
#     print("1. Agregar contacto")
#     print("2. Buscar contacto")
#     print("3. Eliminar contacto")
#     print("4. Listar contactos")
#     print("5. Salir")
#
#     opcion = input("\nElija una opcion: ")
#
#     if opcion == "1":
#         nombre = input("Ingrese el nombre del contacto: ")
#         if nombre in agenda:
#             print(f"El contacto '{nombre}' ya existe con telefono {agenda[nombre]}.")
#             modificar = input("Desea modificar el numero? (s/n): ")
#             if modificar.lower() == "s":
#                 telefono = input("Ingrese el nuevo numero: ")
#                 agenda[nombre] = telefono
#                 print(f"Contacto '{nombre}' actualizado.")
#         else:
#             telefono = input("Ingrese el numero de telefono: ")
#             agenda[nombre] = telefono
#             print(f"Contacto '{nombre}' agregado exitosamente.")
#
#     elif opcion == "2":
#         nombre = input("Ingrese el nombre a buscar: ")
#         if nombre in agenda:
#             print(f"Contacto encontrado: {nombre} -> {agenda[nombre]}")
#         else:
#             print(f"El contacto '{nombre}' no existe en la agenda.")
#
#     elif opcion == "3":
#         nombre = input("Ingrese el nombre a eliminar: ")
#         if nombre in agenda:
#             del agenda[nombre]
#             print(f"Contacto '{nombre}' eliminado.")
#         else:
#             print(f"El contacto '{nombre}' no existe en la agenda.")
#
#     elif opcion == "4":
#         if len(agenda) == 0:
#             print("La agenda esta vacia.")
#         else:
#             print("\n--- Lista de contactos ---")
#             for nombre, telefono in agenda.items():
#                 print(f"  {nombre}: {telefono}")
#             print(f"Total: {len(agenda)} contacto(s)")
#
#     elif opcion == "5":
#         print("Saliendo de la agenda. Hasta luego!")
#         break
#
#     else:
#         print("Opcion no valida. Intente nuevamente.")
# =============================================================================
