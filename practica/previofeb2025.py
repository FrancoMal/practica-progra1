
while True:
    try:
        diccionarioPartidos = {}
        diccionarioPartidosAlianzas = {}
        totalVotos = 0
        totalVotosAlianza = 0
        listaVotosPartidos = []
        listaVotosAlianza = []
        partidoMasVotado = ""
        
        archivo = open("Resultados.txt", "rt")
        linea = archivo.readline()
        
        while linea:
            linea = linea.rstrip("\n")
            
            if linea not in diccionarioPartidosAlianzas:
                diccionarioPartidosAlianzas[linea] = 0
                
            diccionarioPartidosAlianzas[linea] += 1
            
            
            partido = linea.split(";")
            if partido[0] not in diccionarioPartidos:
                diccionarioPartidos[partido[0]] = 0
            else:
                diccionarioPartidos[partido[0]] += 1
                
                
            linea = archivo.readline()
        
        # Lista todos los partidos
        for clave in diccionarioPartidos:
            totalVotos += diccionarioPartidos[clave]
        
        for clave in diccionarioPartidos:
            listaVotosPartidos.append(diccionarioPartidos[clave])
        
        listaVotosPartidos.sort(reverse=True)
        
        for clave in diccionarioPartidos:
            if diccionarioPartidos[clave] == listaVotosPartidos[0]:
                partidoMasVotado = clave
                break
        
        print("El total de votos es:")
        partido = ""
        
        for i in range(len(listaVotosPartidos)):
            porcentaje = listaVotosPartidos[i]*100/totalVotos
            cantAsteriscos = listaVotosPartidos[i]*100//totalVotos
            
            for clave in diccionarioPartidos:
                if diccionarioPartidos[clave] == listaVotosPartidos[i]:
                    partido = clave

            print(f"{partido:<30} | {'':*<{cantAsteriscos}} {porcentaje:<2.2f} %")
        print()
        
        # El partido más votado y sus alianzas
        
        print(f"El total de votos por alianza de {partidoMasVotado}: ")
        
        nombre = ""
        alianza = ""
        
        for clave in diccionarioPartidosAlianzas:
            nombre, alianza = clave.split(";")
            
            if nombre == partidoMasVotado:
                totalVotosAlianza += diccionarioPartidosAlianzas[clave]
        
        for clave in diccionarioPartidosAlianzas:
            nombre, alianza = clave.split(";")
            
            if nombre == partidoMasVotado:
                listaVotosAlianza.append(diccionarioPartidosAlianzas[clave])
                
        listaVotosAlianza.sort(reverse=True)

        for i in range(len(listaVotosAlianza)):
            porcentaje = listaVotosAlianza[i]*100/totalVotosAlianza
            cantAsteriscos = listaVotosAlianza[i]*100//totalVotosAlianza
            
            for clave in diccionarioPartidosAlianzas:
                if diccionarioPartidosAlianzas[clave] == listaVotosAlianza[i]:
                    claveEnLista = clave.split(";")
                    nombre, alianza = claveEnLista

            print(f"Alianza {alianza:<30} | {'':*<{cantAsteriscos}} {porcentaje:<2.2f} %")
        
        
        break
            
    except KeyboardInterrupt as mensaje:
        print("Error inesperado: ", mensaje)
        
    finally:
        try:
            archivo.close()
        except NameError:
            pass