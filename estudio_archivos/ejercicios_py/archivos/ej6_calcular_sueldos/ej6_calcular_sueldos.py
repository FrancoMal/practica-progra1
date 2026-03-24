# =============================================================================
# EJERCICIO 6 - Calcular sueldos finales con antiguedad
# =============================================================================
# Consigna: Leer el archivo empleados.txt (formato: nombre;sueldo;antiguedad)
# y crear un archivo sueldos.txt con el formato nombre;sueldo_final, donde
# sueldo_final = sueldo * (1 + antiguedad * 0.03).
# Es decir, cada anio de antiguedad suma un 3% al sueldo base.
# =============================================================================
# Reglas de la cursada:
# - NUNCA usar readlines(), read() sin parametro, ni list(arch) -> PROHIBIDO
# - Usar readline() con while, o for linea in arch
# - Siempre try/except/finally con close() protegido por except NameError
# - FileNotFoundError ANTES de OSError
# - Un write() por registro, agregar \n manualmente
# - Usar seek(0) en vez de cerrar y reabrir en el mismo modo
# =============================================================================







try:
    arch_emp=open("empleados.txt", "rt")
    arch_sueldo=open("sueldos.txt", "wt")

    for linea in arch_emp:
       linea = linea.rstrip("\n")
       nombre,sueldo_basico,antiguedad = linea.split(";")
       sueldo_final = float(sueldo_basico) * (1 + float(antiguedad) * 0.03)
       arch_sueldo.write(nombre+";"+str(sueldo_final)+"\n")

    print
except FileNotFoundError as msg:
    print("No se puede abrir:", msg)
except OSError as msg:
    print("Error:", msg)
finally:
    try:
        arch_emp.close()
        arch_sueldo.close()
    except NameError:
        pass














# print("=" * 60)
# print("EJERCICIO 6 - Calcular sueldos finales con antiguedad")
# print("=" * 60)

# try:
#     arch_entrada = open("empleados.txt", "rt")
#     arch_salida = open("sueldos.txt", "wt")
#     cantidad = 0
#     for linea in arch_entrada:
#         linea = linea.strip()
#         if linea != "":
#             campos = linea.split(";")
#             nombre = campos[0]
#             sueldo = float(campos[1])
#             antiguedad = int(campos[2])
#             sueldo_final = sueldo * (1 + antiguedad * 0.03)
#             arch_salida.write(nombre + ";" + str(round(sueldo_final, 2)) + "\n")
#             cantidad += 1
#             print(f"  {nombre}: sueldo ${sueldo:.2f}, antiguedad {antiguedad} anios -> sueldo final ${sueldo_final:.2f}")
#     print(f"Se generaron {cantidad} registros en sueldos.txt")
# except FileNotFoundError:
#     print("Error: no se encontro el archivo empleados.txt")
# except OSError:
#     print("Error al acceder a los archivos")
# finally:
#     try:
#         arch_entrada.close()
#     except NameError:
#         pass
#     try:
#         arch_salida.close()
#     except NameError:
#         pass
