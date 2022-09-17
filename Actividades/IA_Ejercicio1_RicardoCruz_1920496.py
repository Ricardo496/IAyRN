nombre = input("Introduce tu nombre: ")

if nombre == "Ana":
  print("Nombre no valido")
elif nombre == "Juan":
    print("Nombre no valido")
elif nombre == "Pedro":
    print("Nombre no valido")
else:
    print("Hola " + nombre)

def mifuncion():
    numeros = list(range(11))
    print(numeros[-1])
    numeros1 = list(range(10, -1, -1))
    print(numeros1)

print(mifuncion())