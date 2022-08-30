import os
os.system('cls')
import random


def adivina_num(x):
    print("===========================")
    print("Bienvenido al juego")
    print("===========================")

    numero_aleatorio=random.randint(1,x)
    predic=0
    while predic != numero_aleatorio:
        predic= int(input(f"ingrese un numero a adivinar entre 1 y {x}:"))

        if predic < numero_aleatorio:
            print("numero ingresado es menor , intenta otra vez.")

        else:
            print("numero ingresado es mayor , intenta otra vez.")

    print(f"Felicidades, adivinaste el numero {numero_aleatorio}")
adivina_num(10)

          

