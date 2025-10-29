import datetime
def entrega(fecha_limite_str):
    fecha_limite = datetime.datetime.strptime(fecha_limite_str, "%d/%m/%Y %H:%M")
    fecha_actual =datetime.datetime.now()
    return fecha_actual <= fecha_limite 
fecha_maxima = 30/10/2025
if entrega (fecha_maxima):
    print("Aún estas dentro de la fecha.")
else:
    print("Entrega fuera de fecha.")
entrega()

