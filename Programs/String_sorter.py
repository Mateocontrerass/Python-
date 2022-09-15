
# To sort a string 

def ordenar_cadena(cadena:str)->str:
    lista=[]
    for i in cadena:
        lista.append(i)
    
    lista2=[]

    #En la lista2 va el minimo 
    i=0
    while i<len(cadena):

        lista2.append(min(lista))
        lista.remove(min(lista))
        i+=1
    
    hola="".join(lista2)
    return hola
    

