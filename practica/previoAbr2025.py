# Una aerolínea de bajo costo cobra un adicional sobre el precio del pasaje a quienes deseen 
# elegir asiento. Quienes no lo abonen serán asignados al azar en los asientos que no hayan 
# sido elegidos previamente. Esta información se almacena por cada vuelo en un archivo CSV 
# donde cada registro puede tener dos formatos diferentes:
# Formato 1: 
# Nombre del pasajero;fila;asiento
# Formato 2: 
# Nombre del pasajero
# El formato 1 se aplica a quienes hayan abonado el adicional por seleccionar ubicación, mien-
# tras que el formato 2 se aplica a los demás viajeros.
# El nombre del pasajero se escribe como <Apellido, nombre>. La fila oscila entre 1 y N, don-
# de el valor de N depende del modelo de la aeronave. El asiento va desde la A hasta la F en 
# modelos regionales de hasta 32 filas de asientos y desde la A hasta la J en modelos de doble 
# pasillo y largo alcance con más de 32 filas de asientos.
# Se solicita desarrollar un programa que lea un archivo con las características mencionadas y 
# distribuya  los  asientos  respetando  la  reservas  realizadas  y  asignando  al  azar  los  asientos 
# restantes entre los pasajeros que no abonaron el adicional. Mostrar un listado con las asig-
# naciones realizadas ordenado por fila y asiento, e imprimir otro listado con los asientos que 
# hayan quedado libres  ordenado por el mismo criterio. También se  deberá  emitir un listado 
# con las colisiones, si las hubiera. Una colisión ocurre cuando dos pasajeros distintos  reser-
# van el mismo asiento. Estos eventos deben ser resueltos por personal de la aerolínea. 
# Se    suministra  un  archivo  ejemplo  llamado  Vuelo447.txt.  El  archivo  no  está  ordenado  por 
# ningún criterio particular. El programa debe funcionar con éste o cualquier otro archivo que 
# respete las características indicadas, detectando automáticamente el modelo de avión (sim-
# ple o doble pasillo) en función de la cantidad de filas de la aeronave y de los asientos reser-
# vados.  Es  decir  que  si  todas  las  reservas  tienen  una  fila  menor  o  igual  a  32  y  todos  los 
# asientos una letra menor o igual a la F, deberá considerarse que se trata de un avión de un 
# solo pasillo y alcance regional



def determinar_modelo(archivo):
    """Lee el archivo una vez para determinar el modelo sin cargar todo en memoria"""
    max_fila = 0
    max_asiento = 'A'
    arch = open(archivo, 'r')
    for linea in arch:
        linea = linea.strip()
        partes = linea.split(';')
        if len(partes) == 3:
            fila = int(partes[1])
            asiento = partes[2]
            if fila > max_fila:
                max_fila = fila
            if asiento > max_asiento:
                max_asiento = asiento
    arch.close()
    if max_fila <= 32 and max_asiento <= 'F':
        return 'regional'
    else:
        return 'largo alcance'

def generar_asientos(modelo):
    asientos = {}
    if modelo == 'regional':
        filas = 32
        letras = ['A', 'B', 'C', 'D', 'E', 'F']
    else:
        filas = 50  # Suponiendo un máximo de 50 filas para largo alcance
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    for fila in range(1, filas + 1):
        for letra in letras:
            asientos[f"{fila}{letra}"] = None
    return asientos

def asignar_asientos(archivo, asientos):
    """Procesa el archivo línea por línea sin cargar todo en memoria"""
    colisiones = []
    pasajeros_sin_asiento = []
    
    arch = open(archivo, 'r')
    for linea in arch:
        linea = linea.strip()
        partes = linea.split(';')
        if len(partes) == 3:
            nombre = partes[0]
            fila = partes[1]
            asiento = partes[2]
            clave_asiento = f"{fila}{asiento}"
            if asientos[clave_asiento] is None:
                asientos[clave_asiento] = nombre
            else:
                colisiones.append((nombre, asientos[clave_asiento], clave_asiento))
        else:
            nombre = partes[0]
            pasajeros_sin_asiento.append(nombre)
    arch.close()
    
    asientos_libres = [k for k, v in asientos.items() if v is None]
    
    import random
    random.shuffle(asientos_libres)
    
    for pasajero in pasajeros_sin_asiento:
        if asientos_libres:
            asiento_asignado = asientos_libres.pop()
            asientos[asiento_asignado] = pasajero
    
    return colisiones

def imprimir_listados(asientos, colisiones):
    print("Listado de asignaciones:")
    for asiento in sorted(asientos.keys(), key=lambda x: (int(x[:-1]), x[-1])):
        if asientos[asiento] is not None:
            print(f"Asiento {asiento}: {asientos[asiento]}")
    
    print("\nListado de asientos libres:")
    for asiento in sorted(asientos.keys(), key=lambda x: (int(x[:-1]), x[-1])):
        if asientos[asiento] is None:
            print(f"Asiento {asiento} está libre")
    
    if colisiones:
        print("\nListado de colisiones:")
        for colision in colisiones:
            print(f"Colisión en asiento {colision[2]} entre {colision[0]} y {colision[1]}")

def main():
    archivo = 'Vuelo447.txt'
    modelo = determinar_modelo(archivo)
    asientos = generar_asientos(modelo)
    colisiones = asignar_asientos(archivo, asientos)
    imprimir_listados(asientos, colisiones)

if __name__ == "__main__":
    main()
