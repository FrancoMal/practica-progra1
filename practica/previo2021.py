# Estructura de datos elegida: diccionario de diccionarios
# vendedores = { num_vendedor: { cod_articulo: cantidad_total } }
#
# Se eligió un diccionario porque permite acceso directo por clave (vendedor),
# y dentro de cada vendedor otro diccionario por artículo.
# Esto es más eficiente que una lista porque no necesitamos recorrer
# toda la estructura para buscar un vendedor o artículo específico.
# Un árbol binario no sería necesario porque no requerimos orden especial
# para la búsqueda, y una lista enlazada tendría acceso secuencial O(n).


def leer_archivo(mes_buscado):
    """Lee ventas.txt y devuelve un diccionario con las ventas del mes indicado."""
    vendedores = {}
    try:
        archivo = open("ventas.txt", "r")
        for linea in archivo:
            linea = linea.strip("\n")
            # Parseo del registro según el formato fijo:
            # Pos 0-1: num vendedor | Pos 2-3: cod articulo | Pos 4-7: cantidad | Pos 8-15: fecha ddmmaaaa
            num_vendedor = linea[0:2]
            cod_articulo = linea[2:4]
            cantidad = int(linea[4:8])
            mes = linea[10:12]  # posiciones 10-11 dentro de la fecha (dd[mm]aaaa)

            # Solo acumulo las ventas que correspondan al mes pedido
            if mes == mes_buscado:
                if num_vendedor not in vendedores:
                    vendedores[num_vendedor] = {}
                if cod_articulo not in vendedores[num_vendedor]:
                    vendedores[num_vendedor][cod_articulo] = 0
                # Acumulo la cantidad vendida de ese artículo por ese vendedor
                vendedores[num_vendedor][cod_articulo] += cantidad
    except FileNotFoundError:
        print("Error: no se encontró el archivo ventas.txt")
    finally:
        try:
            archivo.close()
        except NameError:
            pass  # Si el archivo nunca se abrió, no hay nada que cerrar
    return vendedores


def pedir_mes():
    """Pide al usuario un mes (1-12) y lo devuelve formateado a 2 dígitos."""
    while True:
        try:
            mes = int(input("Ingrese el número de mes (1-12): "))
            if 1 <= mes <= 12:
                # Formateo a 2 dígitos: 3 -> "03", 12 -> "12"
                return str(mes).zfill(2)
            else:
                print("Error: ingrese un número entre 1 y 12.")
        except ValueError:
            print("Error: debe ingresar un número entero.")


def mostrar_informe(vendedores):
    """Muestra el informe de ventas por vendedor y artículo."""
    if not vendedores:
        print("No se encontraron ventas para el mes indicado.")
        return

    # Lambda para formatear una línea del informe
    formato_linea = lambda vend, art, cant: f"  Artículo {art}: {cant} unidades"

    # Ordeno los vendedores por número (ya son strings, orden lexicográfico funciona)
    for vendedor in sorted(vendedores.keys()):
        print(f"Vendedor {vendedor}:")
        articulos = vendedores[vendedor]
        for articulo in sorted(articulos.keys()):
            print(formato_linea(vendedor, articulo, articulos[articulo]))

    # Calculo el total general usando lambda + sum
    total = sum(
        cant
        for arts in vendedores.values()
        for cant in arts.values()
    )
    print(f"\nTotal de unidades vendidas en el mes: {total}")


def main():
    mes = pedir_mes()
    vendedores = leer_archivo(mes)
    mostrar_informe(vendedores)


main()
