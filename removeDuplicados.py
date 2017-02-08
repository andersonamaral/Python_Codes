
#Recebe uma lista
#Remove os duplicados
#Imrpime os caracteres unicos
lista = input()

def removeDuplicados(lista):

    novalista=[]
    seen = set()
    for item in lista:
        if item not in seen:
            seen.add( item )
            novalista.append(item)

    return novalista

#li=[12,24,35,24,88,120,155,88,120,155]
print (removeDuplicados(lista))




