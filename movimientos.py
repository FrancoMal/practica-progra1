import json

arch1=open("movimientos.jsonl","r",encoding="utf-8")

arch_csv=open("movimientos.csv","w",encoding="utf-8")


lista_saldos=[]


for linea in arch1:
    
    dic=json.loads(linea)
    
    saldo_final=sum(dic["Movimientos"])

    registro=f'{dic["Cuenta"]};{dic["Nombre"]};{saldo_final}\n'

    if saldo_final<0:

        lista_saldos.append([dic["Cuenta"],dic["Nombre"],saldo_final])

    arch_csv.write(registro)

arch_csv.close()
arch1.close()


matriz_ordenada=sorted(lista_saldos,key=lambda x: x[2])


for i in matriz_ordenada:
    
    print(f"la cuenta {i[0]} del titular {i[1]} tiene un saldo negativo de {i[2]}")