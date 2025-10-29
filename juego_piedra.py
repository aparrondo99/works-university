import random
def nuevo_juego():
    """Args:
    1.Se inicia el juego preguntando al usuario si quiere jugar.
    2.Se inicializan las variables necesarias para el juego.
    3.Se inicia el bucle del juego."""
    juego_nuevo = int(input("¿Quieres jugar?: 1 = Si/2 = No: "))

    if  juego_nuevo != 1:
        print("Vale :(")
        return
    jugador = 0
    computadora = 0
    ronda = 0
    while juego_nuevo == 1:
        n = random.randint(1, 3)
        usuario = int(input("Introduzca un número entre el 1 y el 3 (1: piedra, 2: papel,3: tijera): "))
        if comprobacion(usuario):
            jugador, computadora, ronda = juego(usuario, n, jugador, computadora, ronda)
        juego_nuevo, jugador, computadora, ronda = oleadas(jugador, computadora, ronda)
def comprobacion(usuario):
        """Args:
            1.Se comprueba que el usuario intoduzca un número válido.
        Returns:
            Devuelve True en caso de ser valido el número introdicido."""
        if usuario <1 or usuario >3:
            print("Error, número no permitido, introduzca uno dentro del rango.")
            return False
        return True

def juego(usuario,n, jugador,computadora, ronda):
    """Args:
    1.Se comparan los números introducidos por el usuario y la computadora.
    2.Se actualizan las puntuaciones y la ronda.
    Returns:
        Devuelve las puntuaciones y la ronda actualizadas."""
    if usuario == n:
        print("Empate")

    elif (usuario == 1 and n == 3) or (usuario == 2 and n == 1) or (usuario == 3 and n == 2):
        print("Gana el jugador :D")
        jugador += 1

    else:
        print("Gana la computadora :(")
        computadora += 1

    ronda += 1
    print(f"La computadora eligió: {n}")
    print(f"Puntuación jugador: {jugador}")
    print(f"Puntuacion computadora: {computadora}")
    print(f"Ronda: {ronda}")


    return jugador, computadora, ronda

def oleadas(jugador, computadora, ronda):
    """Args:
    1.Se comprueba si se han jugado 3 rondas.
    2.Se pregunta al usuario si desea seguir jugando.
    Returns:
        Devuelve si se desea seguir jugando, las puntuaciones y la ronda actualizadas."""
    if ronda == 3:
        juego_dos = int(input("¿Deseas seguir jugando? 1 = Sí, 2 = No: "))

        if juego_dos !=1:
            print("Tu puntuación es de: ", jugador)
            return False, jugador, computadora, ronda

        else:
            return True, jugador, computadora, 0
    return True , jugador, computadora, ronda

nuevo_juego()
