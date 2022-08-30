#obtener el primer elemento y el ultimo elemento de una lista

import os 
os.system("cls")

lenguajes=["python","PHP","Go","perl","Java"]
lenguajes.append("Javasript")
lenguajes[2] = "C++"
print(lenguajes)
primer_elemento=lenguajes[0]
ultimo_elememto=lenguajes[4]
print(primer_elemento)
print(ultimo_elememto)
