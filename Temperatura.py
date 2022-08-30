# Este ejercicio consiste en convertir temperaturas de centigrados en fahrenheit y kelvin.

C=int(input("Ingrese una temperatura en centigrados :"))

R=C+460
F=(9*C/5)+32
Kel=R-187

print("la temperatura en fahrenheit es: ",F)
print("la temperatura en  Rankine es:",R)
print("la temperatura en Kelvin es :", Kel)
