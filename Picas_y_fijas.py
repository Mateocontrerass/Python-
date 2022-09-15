
#Función

def picas_y_fijas(numero_secreto:int,intento:int)->dict:
    correcta=[]
    #Quiero descomponer cada numero a una lista y comparar los elementos de cada lista
    for num in str(numero_secreto):
        correcta.append(num)
    
    prueba=[]
    for num in str(intento):
        prueba.append(num)

    dicc={"PICAS":0 , "FIJAS":0}

    for i in range(4):
        first=correcta[i]
        second=prueba[i]

        if first==second: dicc["FIJAS"]=dicc["FIJAS"] +1

        if first!=second and second in correcta: dicc["PICAS"]=dicc["PICAS"]+1
    
    return dicc

# Interfaz

numero_secreto:int(input("Ingrese el numero secreto de 4 caracteres de longuitud"))
intento:int(input("Ingrese su numero intentado"))

hola=picas_y_fijas(numero_secreto,intento)
print("El numero de fijas es de" , hola["FIJAS"]," y el numero de picas es", hola["PICAS"])

