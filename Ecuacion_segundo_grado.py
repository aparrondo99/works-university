"""Vamos a resolver una ecuación de segundo grado."""
a = int(input("Indique A: "))
b = int(input("Indique B: "))
c = int(input("Indique C: "))
"""Args:
    1. Pedimos las tres incognitas (a,b,c)
    2. Creamos una variane donde ponemos parte de la formula, para simplificaro.
    3. Imprimimos las dos soluciones."""
def ecuacion():
    formula = b**2-4*a*c
    if formula > 0:
        solucion1 = (-b+((formula)**0.5))/2*a
        solucion2 = (-b-((formula)**0.5))/2*a
        SolucionFinal1= int(solucion1)
        SolucionFinal2= int(solucion2)
        print("Esta es la primera solucion: ",SolucionFinal1)
        print("esta es la segunda solucion: ",SolucionFinal2)
ecuacion()

    
