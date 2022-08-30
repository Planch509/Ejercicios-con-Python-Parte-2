import os
os.system('cls')

#validar si un archivo tiene la extension.py
def Validar(nombre_archivo):
    if len(nombre_archivo) >=3 and nombre_archivo[-3:] =='.py':
        return nombre_archivo
    else:
        return nombre_archivo + '.py'

    
print (Validar("ss.py"))
print (Validar("okey"))
