import os
os.system('cls')


mes=int(input("ingrese el mes  del año (1-12):"))
estacion=None

if  mes==1 or mes==2 or mes==12:
    estacion="invierno"
elif mes==3 or mes==4 or mes==5:
    estacion="primavera"
elif mes==6 or mes==7 or mes==8:
    estacion="verano"
else:
    estacion="numero fuera de rango"  
     
print("Estacion:",estacion, "para el mes",mes) 
