    
import os 
os.system('cls')

class rectangulo:
    def __init__(self, base, altura):
       self.base = base 
       self.altura = altura 
    def calcular_area(self):
        return self.base * self.altura
base = int(input("proporciona una base:"))
altura = int(input("proporciona la altura:"))

rect= rectangulo(base,altura)
print(rect.calcular_area)
    