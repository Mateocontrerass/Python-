#Calcular precio de boletos de avión.
# No. compañias: 2 (Alas y Volar)
# Temporada: Alta(1) Baja(0)
# Edad: Mayores de 60 pagan seguro. Menores de 18 descuento.
# Estudiante: Si (1) , no (0)

def precios_aviacion_2(alta:bool,compañia:str,edad:int,estudiante:bool)->int:
    precio=5000000
    variaciones=0
    seguro=False

    if compañia=="ALAS":
        if alta==True:
            variaciones+=0.3
        else:
            if edad>=0 and estudiante:
                variaciones+=0.1

    elif compañia=="VOLAR":
        if alta==True:variaciones+=0.2
        if edad>60: seguro=True

        if edad<18: variacones-=0.5
    
    precio*=(1+variaciones)

    if seguro==True: precio+=100000

    return precio


############INTERFAZ
alta=bool(int(input("Ingrese 1 si es temporada alta, 0 de lo contrario:")))
compañia=input("Ingrese el tipo de compañoa que utilizara para viajar, ALAS o VOLAR:")
edad=int(input("Ingrese su edad :"))
estudiante=bool(int(input("Ingrese 1 si es estudiante, 0 si no lo es")))

tarifa=precios_aviacion_2(alta,compañia,edad,estudiante)

print("El precio de su boleto es ", tarifa )