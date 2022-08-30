#Obtner un conjunto de numeros separados por coma y crear y crear una lista 

import os 
os.system("cls")
entrada=input("Escriba Varios numeros por coma : ")
print(entrada)
print(type(entrada))
numeros=entrada.split(',')
print(numeros)
print(type(numeros))