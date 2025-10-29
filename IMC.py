"""En este caso, vamos a crear una calculadora del IMC.
La formula para el IMC = Peso (KG) dividido en la altura al cuadrado (M2)"""
def IMC():
    peso =float(input("Ingese su peso en KG: "))
    altura =float(input("Ingrese su altura en M: "))   
    """Args:
        Variable 1: Pedir el peso en KG.
        Variable 2: Pedir la altura en M.
        Ahora añadimos un if para que no se pueda poner pesos o altura negativa"""
    if peso <=0 or altura <=0:
        print("Error, no puedes introducir número negativos")
        return peso
    else:
        imc = peso / (altura**2)
        print(f"Tú IMC es de {imc:.2f}%")
"""Una vez hecha la función, la ejecutamos."""
IMC()
       
    



