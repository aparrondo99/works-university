"""Paso a paso para realizar un programa que calcula el mcd usando el algoritmo de Euclides"""
def algoritmo(a: int,b: int) -> int:
    while b !=0:
        a,b = b, a % b
    return a
"""Args:
        a: El primer número.
        b: El segundo segundo número.
        r: Es el resultado de la división de a entre b."""
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo: "))
"""Ultimo paso, llamamos a la función."""
mcd = algoritmo(a,b)
print("El mcd es: ", mcd)