import os 
os.system('cls')
import random
from werkzeug.security import generate_password_hash

minus="abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros="0123456789"
simbolos= "#*/$%&@?¡¿"
todo= minus+mayus+numeros+simbolos
longitud=15
for _ in range(5):
    muestra= random.sample(todo,longitud)
    password= "".join(muestra)
    password_encryptado= generate_password_hash(password)
    print("{} {}" .format(password,password_encryptado))