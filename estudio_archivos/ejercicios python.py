
# "productos.txt" tiene formato codigo;descripcion;precio. Cuenta cuantos tienen precio > 1000.
# try:    
#     arch = open("productos.txt", "rt")
#     # COMPLETA: contador, recorrer, split, convertir precio
#     contador = 0
#     for linea in arch:
#         linea = linea.rstrip("\n")
#         codigo,descripcion,precio=linea.split(";")
#         if precio > 1000:
#            contador+=1
#     print(contador)
# except FileNotFoundError as msg:
#     print("Archivo no encontrado:", msg)
# except OSError as msg:
#     print("Error:", msg)
# finally:
#     try:
#         arch.close()
#     except NameError:
#         pass

# COMPLETA TODO EL CODIGO desde cero
# Recuerda: try/except/finally, abrir 2 archivos,
# leer con for o readline, escribir con write

# Lee "alumnos.txt" (legajo;nombre) y copia a "aprobados.txt" solo legajos < 1100000.


# try:
#     arch = open("alumnos.txt", "rt")
#     arch2 = open("aprobados.txt","wt")
    
#     for linea in arch:
#        linea = linea.rstrip('\n')
#        legajo,nombre=linea.split(";")
#        if legajo < 1100000:
#           arch2.write(linea)
# except FileNotFoundError as msg:
#     print("Archivo no encontrado: ", msg)
# except OSError as msg:
#     print("Error: ", msg)
# finally:
#     try:
#         arch.close()
#     except NameError:
#         pass


# COMPLETA TODO EL CODIGO
# Pista: necesitas variables para guardar el maximo
# y el nombre del producto correspondiente


# "ventas.txt" tiene formato producto;cantidad;precio_unitario. Encuentra el producto con mayor precio unitario e imprimilo.
# try:
#     arch = open("ventas.txt", rt)
#     mayor= []
#     for linea in arch:
#         linea = linea.rstrip('\n')
#         producto,cantidad,precio_unitario=linea.split(";")
#         if precio_unitario > mayor[2]:
#            mayor = [producto,cantidad,precio_unitario]
#     print("el producto ", mayor[0], " tiene el mayor precio unitario: ", mayor[2])
    
# except FileNotFoundError as msg:
#    print("error al abrir archivo", msg)
# except OSError as msg:
#    print("Error", msg)
# finally:
#    try:
#       arc.close()
#    except NameError:
#       pass



# COMPLETA TODO EL CODIGO
# Abrir entrada en "rt" y salida en "wt"
# Leer cada linea, calcular sueldo final, grabar
# "empleados.txt" tiene nombre;sueldo_basico;antiguedad. Crea "sueldos.txt" con nombre;sueldo_final donde sueldo_final = sueldo_basico * (1 + antiguedad * 0.03).
# try:
#     arch_emp=open("empleados.txt", rt)
#     arch_sueldo=open("sueldos.txt", wt)

#     for linea in arch_emp:
#        linea = linea.rstrip("\n")
#        nombre,sueldo_basico,antiguedad = linea.split("/")
#        sueldo_final = sueldo_basico * (1 + antiguedad * 0.03)
#        arch_sueldo.write(nombre,";",sueldo_final)

   
# except FileNotFoundError as msg:
#     print("No se puede abrir:", msg)
# except OSError as msg:
#     print("Error:", msg)
# finally:
#     try:
#         arch_emp.close()
#         arch_sueldo.close()
#     except NameError:
#         pass

#Lee "texto.txt" y cuenta la cantidad total de palabras en todo el archivo.
# try:
#     arch = open("texto.txt", "rt")
#     total_palabras = 0
#     for linea in arch:
#         linea = linea.rstrip('\n')
#         palabras = linea.split()
#         total_palabras += len(palabras)
#     print("Total de palabras:", total_palabras)
# except FileNotFoundError as msg:
#     print("No se puede abrir:", msg)
# except OSError as msg:
#     print("Error:", msg)
# finally:
#     try:
#         arch.close()
#     except NameError:
#         pass



# COMPLETA TODO EL CODIGO
# Pista: usar una variable booleana "encontrado"
# Recorrer con readline o for, comparar legajos



# "alumnos.txt" tiene legajo;nombre. Dado un legajo ingresado por teclado, buscar si existe e imprimir el nombre. Si no existe, informar.
# try:
#     arch = open("alumnos.txt", rt)
#     try:
#         inputLegajo = int(input(("ingrese legajo: "))
#     except ValueError as msg:
#         print("Ingrese numero")
    
#     for linea in arch:
#         linea = linea.rstrip(\n)
#         legajo,nombre= linea.split("/")
#         if legajo == inputLegajo:
#            print(nombre)
#         else:
#            print("No encontrado")
    
# except FileNotFoundError as msg:
#    print("error", msg)
# except OSError as msg:
#    print("error", msg)

# finally: 
#     try:
#         arch.close()
#     except NameError:
#         pass


# COMPLETA TODO EL CODIGO
# Pista: modo de apertura "at" (append text)
# Estructura similar al ejemplo de creacion


#Agrega nuevos alumnos al final de "alumnos.txt" sin perder los datos anteriores. Pedir legajo y nombre hasta que se ingrese legajo vacio.
# try:
#     arch = open("alumnos.txt", at)
#     lu = int(input(ingrese legajo:))
#     while lu != "":
#        string(input(Ingrese nombre: ))
#        arch.append(nombre + ";"+ lu)
#        print(agregado existosamente)
#        lu = int(input(ingrese legajo: ))
# except FileNotFoundError as msg:
#    print("Error: ", msg)
# except OSError as msg:
#    print("Error: ", msg)

# finally: 
#     try:
#         arch.close()
#     except NamError:
#         pass



# COMPLETA TODO EL CODIGO
# Necesitas: contador, acumulador
# El promedio se calcula al final (acum / cont)

# try:
#      arch = open("ventas.txt", rt)
#      cantRegistros = 0
#      totalVendido = 0
#      for linea in arch:
#          linea = linea.rstrip(\n)
#          producto,cantidad,precio_unitario = linea.split(";")
#          cantRegistros += 1
#          totalVendido += (cantidad * precio_unitario)
#      print("Registros:", cantTotal)
#      print("Monto total:", totalVendido)
#   if cantRegistros > 0:
#        print("Promedio:", round(totalVendido / cantRegistros, 2))
# except FileNotFoundError as msg:
#    print("Error: ", msg)
# except OSError as msg:
#    print("Error: ", msg)

# finally: 
#     try:
#         arch.close()
#     except NameError:
#         pass