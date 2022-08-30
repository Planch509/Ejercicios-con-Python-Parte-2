import os
os.system('cls')

# diccionarios
Dic = {
        "nombre": "Steeven",
        "apellido": "Villefranche",
          "edad":"22"
    }

print(Dic)
print(Dic["edad"])
print(Dic.get("apellido"))

for j in Dic:
    print(j)
    
for j in Dic:
    print(Dic[j])

print("edad" in Dic)
