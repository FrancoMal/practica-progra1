# Estructura de datos elegida: diccionario de listas con sub-diccionario
# articulos = { SKU: [descripcion, { mes: cantidad_total }] }
#
# Se eligió un diccionario principal con clave SKU porque permite acceso
# directo O(1) para verificar si un artículo ya fue procesado.
# Dentro de cada artículo, otro diccionario con clave mes permite
# acumular cantidades por mes de forma eficiente.
# Una lista requeriría recorrer todos los elementos para buscar un SKU
# específico (O(n)), lo que sería ineficiente con 50000 registros.
# Un árbol binario no sería necesario porque no requerimos orden
# especial para la búsqueda, y una lista enlazada tendría acceso
# secuencial O(n).


def leer_archivo():
    """Lee pedidos.csv y devuelve un diccionario con las cantidades por mes de cada artículo."""
    articulos = {}
    try:
        archivo = open("pedidos.csv", "r")
        for linea in archivo:
            linea = linea.strip("\n")
            # Formato CSV: SKU;descripcion;DD/MM/AA;cantidad
            SKU, descripcion, fecha, cantidad = linea.split(";")
            dia, mes, anio = fecha.split("/")
            cantidad = int(cantidad)

            # Si el artículo es nuevo, creo su entrada con descripcion y dict de meses
            if SKU not in articulos:
                articulos[SKU] = [descripcion, {}]
            # Si el mes es nuevo para este artículo, lo inicializo en 0
            if mes not in articulos[SKU][1]:
                articulos[SKU][1][mes] = 0
            # Acumulo la cantidad vendida en ese mes
            articulos[SKU][1][mes] += cantidad
    except FileNotFoundError:
        print("Error: no se encontró el archivo pedidos.csv")
    except OSError:
        print("Error: problema al leer el archivo")
    finally:
        try:
            archivo.close()
        except NameError:
            pass  # Si el archivo nunca se abrió, no hay nada que cerrar
    return articulos


def mes_mayor_demanda(cantidades_por_mes):
    """Recibe un diccionario {mes: cantidad} y devuelve el mes con mayor cantidad.
    Usa max() con una función lambda como key (requisito de la consigna)."""
    return max(cantidades_por_mes, key=lambda m: cantidades_por_mes[m])


def nombre_mes(num_mes):
    """Convierte un número de mes (string de 2 dígitos) a su nombre en español."""
    meses = {
        "01": "Enero", "02": "Febrero", "03": "Marzo",
        "04": "Abril", "05": "Mayo", "06": "Junio",
        "07": "Julio", "08": "Agosto", "09": "Septiembre",
        "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
    }
    return meses.get(num_mes, num_mes)


def mostrar_informe(articulos):
    """Muestra el listado ordenado alfabéticamente por descripción.
    Cada artículo aparece una sola vez con el mes de mayor demanda."""
    if not articulos:
        print("No se encontraron artículos.")
        return

    # Armo una lista de tuplas (descripcion, SKU, mes_mayor, cantidad) para ordenar
    listado = []
    for SKU, datos in articulos.items():
        descripcion = datos[0]
        cantidades = datos[1]
        mejor_mes = mes_mayor_demanda(cantidades)
        listado.append((descripcion, SKU, mejor_mes, cantidades[mejor_mes]))

    # Ordeno alfabéticamente por descripción
    listado.sort(key=lambda x: x[0])

    print(f"{'='*85}")
    print(f"  LISTADO DE ARTÍCULOS - MES DE MAYOR DEMANDA")
    print(f"{'='*85}")
    for desc, sku, mes, cant in listado:
        print(f"  SKU {sku:<8} | {desc:<35} | {nombre_mes(mes):<12} | {cant} unidades")
    print(f"{'='*85}")
    print(f"  Total de artículos: {len(listado)}")


# --- Punto 2: Función recursiva para contar elementos de un conjunto ---

def contar_elementos(conjunto):
    """Cuenta los elementos de un conjunto sin usar len().
    Usa recursión y manejo de excepciones: cuando el conjunto está vacío,
    pop() lanza KeyError, que funciona como caso base."""
    try:
        conjunto.pop()  # Saco un elemento; si está vacío lanza KeyError
        return 1 + contar_elementos(conjunto)
    except KeyError:
        return 0  # Conjunto vacío: caso base


def main():
    # Punto 1: informe de artículos
    articulos = leer_archivo()
    mostrar_informe(articulos)

    # Punto 2: demostración de función recursiva
    print("\n--- Función recursiva: contar elementos de un conjunto ---")
    ejemplo = {10, 20, 30, 40, 50}
    print(f"Conjunto: {ejemplo}")
    # Uso .copy() para no destruir el conjunto original
    print(f"Cantidad de elementos (sin len): {contar_elementos(ejemplo.copy())}")
    print(f"Verificación con len(): {len(ejemplo)}")


main()
