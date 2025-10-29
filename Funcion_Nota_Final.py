"""vamos a crear una funcion para que un alumno sepa su nota final."""
def suma_notas():
    calificacion_1 = float(input("Nota primera calificación: "))
    calificacion_2 =float(input("Nota segunda calificación: "))
    calificacion_3 = float(input("Nota tercera clasificación: "))
    examen = float(input("Nota examen final: "))
    trabajo = float(input("Nota tabajo final: ")) 
    """Args: 
        1.Se pide la nota de los parciales.
        2.Se pide la nota del examen final y del trabajo.
        3.Se relizan las ponderaciones, añadiendo un minimo y un máximo para la nota final."""
    calificacion_media = (calificacion_1 + calificacion_2 + calificacion_3)/3
    calificacion_final = calificacion_media * 0.55
    examen_final = examen * 0.33
    trabajo_final = trabajo * 0.15
    
    notas_finales = float(calificacion_final + examen_final + trabajo_final)
    notas_finales = max(0, min(notas_finales, 10))
    print(f"su nota final es: {notas_finales:.2f}")

suma_notas()

