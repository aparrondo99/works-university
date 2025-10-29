"""En este caso vamos a crear un algoritmo para un cambio de divisas con un 5% de comisión. """
eur= 0.85
usd= 1.17
dinero_ingreso= float(input("Cantidad a ingresar: "))
moneda_base= input("Moneda base (eur/usd): ")
dinero_destino = dinero_ingreso * 0.95
def exchange():
    """Args:
        1. dinero_ingres: pedimos al usuario que nos ingrese la cantidad de dinero para cambiar
        2. moneda_base: Pedimos al usuaio que nos indique la moneda de su divisa actual.
        3. Hacemos el 5% de de comisión, descontando el dinero que le daremos al usuario."""
    if moneda_base == "eur":
        dinero_destino * usd
        dinero_total = dinero_destino * usd
        print(f"El cambio total es de:{dinero_total:.2f} USD.")
    elif moneda_base == "usd":
        dinero_destino * eur
        dinero_total = dinero_destino * eur
        print(f"El cambio total es: {dinero_total:.2f} EUR.")
    else:
        print("por favor, indique si la divisa es eur o usd.")
"""Usamos el if, elif y else para que el prorama sepa que si es eur, tiene que pasarlo a usd
    y si es usd, tiene que pasar a eur."""
exchange()

    