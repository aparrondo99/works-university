import random
juego_nuevo = int(input("¿Quieres jugar?: 1 = Si/2 = No: "))
jugador = 0
computadora = 0 
ronda = 0
while juego_nuevo == 1:
    if  juego_nuevo != 1:
        print("Vale :(")
        break
    usuario = int(input("Introduzca un número entre el 1 y el 3 (1: pierda, 2: papel,3: tijera): "))
    n = random.randint(1,3) 
    def juego():
        global jugador, computadora
        piedra = 1
        papel = 2
        tijera = 3       
        if usuario <1 or usuario >3:
            print("Error, número no permitido, introduzca uno dentro del rango.")
            return
        elif usuario == 1: 
            if n == 1:
                print("Empate")
                print("Computadora: , jugador: ",computadora, jugador)
            elif n == 2:
                print("Gana la Computadora :(")
                computadora += 1
                print("Computadora: , jugador: ", computadora, jugador)
            elif n == 3:
                print("Gana el Jugador :D")
                jugador += 1
                print("Computadora: , jugador: ", computadora, jugador)
        elif usuario == 2:
            if n == 1:
                print("Gana la Computadora :(")
                computadora += 1
                print("Computadora: , jugador: ", computadora, jugador)
            elif n == 2:
                print("Empate")
                print("Computadora: , jugador: ", computadora, jugador)
            elif n == 3:
                print("Gana el Jugador :D")
                jugador += 1
                print("Computadora: , jugador: ", computadora, jugador)
        elif usuario == 3:
            if n == 1:
                print("Gana el jugar :D")
                jugador += 1
                print("Computadora: , jugador: ", computadora, jugador)
            elif n == 2:
                print("Gana la computadora :(")
                computadora += 1
                print("Computadora: , jugador: ", computadora, jugador)
            elif n == 3:
                print("Empate")
                print("Computadora: , jugador: ", computadora, jugador)
        else:
            print("Jugador: ", jugador)
            print("Computadora: ", computadora)
juego()
ronda += 1
if ronda == 3:
    juego_dos= int(input("¿Deseas seguir jugando? 1 = Sí, 2 = No: "))
    if juego_dos !=1:
        print("Tu puntuación es de: ", jugador)
    else:
        ronda = 0


