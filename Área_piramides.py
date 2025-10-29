"""Vamos a crear un algritmo para calcular el área de una pirámide rectangular y rectangulare."""
def area_piramide_rectangular():
    """ formula: a*b+(a*ha+b*hb)"""
    a = float(input("Tamaño lado A: "))
    b = float(input("Tamaño lado B: "))
    h1 = float(input("Tamaño hipotenusa 1: "))
    h2 = float(input("Tamaño hipotenusa 2: "))
    area_total = a*b + (a*h1+b*h2)
    print(f"El area de la piramide rectangular es de: {area_total:.2f}")
area_piramide_rectangular()
"""Args:
    1.Pedimos los datos al usuario.
    2.Procedemos a realizar la fomrula.
    3.Imprimimos el resultado."""
def area_piramide_cuadrangular():
    """formula: A= a**+2*a*hl"""
    a = float(input("Tamaño del lado: "))
    hl = float(input("Tamaño del apotema lateral: "))
    area = a**2 + 2*a*hl
    print(f"El area de la piramide cuadranugular es: {area:.2f}")
area_piramide_cuadrangular()    