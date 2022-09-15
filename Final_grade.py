# Input: List of dictionaries with name and grade of each student such as {"nombre":mateo, "nota":3}
# and the function will approximate the grade.

def calcular_definitivas(estudiantes:list)->list:
    total=[]
    
    def aproximacion(nota):
        final=float(nota)
        if nota>=4.5: final=5
        elif nota >=3.5 and nota<4.5: final = 4
        elif nota >=2.5 and nota<3.5: final = 3
        else: final = 1.5
        return final


    for x in estudiantes: 
        nombre=x["nombre"]
        valor=aproximacion(x["nota"])

        dicc={"nombre":nombre,"nota":valor}

        total.append(dicc)

    return total


# Example 
hey=list([{"nombre":"mateo","nota":2.9},{"nombre":"mateo2","nota":4.4}])
hi=calcular_definitivas(hey)
print("The approximated grades are ",hi)