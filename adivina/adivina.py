import random

"""                                                 
Juego para adivinat un número random
Se establecerán niveles de acuerdo a
la cantidad de intentos disponibles
"""

number = random.randint(0,100)

#print(number)

def play(dif):
    chances = dif
    while dif >= 0:
        tries = int(input("Adivine el número: "))
        
        if tries == number:
            print("Felicidades, ganaste!")
            break
        elif tries > number:
            print("Incorrecto, intente de nuevo con un número más pequeño")
            chances -= 1
            print(f"Te quedan {chances} intentos")
        elif tries < number:
            print("Incorrecto, intente de nuevo con un número más grande")
            chances -= 1
            print(f"Te quedan {chances} intentos")
        elif tries < 0:
            print("Valor incorrecto, intente de nuevo")
        if chances == 0:
            print("Perdiste perris!")
            break


main_text = """ 
        ESCOGE LA DIFICULTAD:
        4 = hell
        3 = difícil
        2 = fácil
        1 = noob
        """
difficult = int(input(main_text))
list_op = [1, 2, 3, 4]
if difficult == 4:
    play(3)
elif difficult == 3:
    play(5)
elif difficult == 2:
    play(7)
elif difficult == 1:
    play (10)
else:
    print("Valor incorrecto ingrese de nuevo")
