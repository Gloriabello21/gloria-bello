"""#1
name = input("what's your name? ")
print(f"hello, {name}")
"""
#2
"""lo que hace este ejercicio es que guarda los nombres que pones
y despues pones code names.txt y hay se crea un archivo e imprimen los
nombres que ya escribiste antes"""
"""name = input("what's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
#3
lo que hace este ejercicio es que guarda los nombres que pones
y despues pones vas a names.txt y hay se imprimen los nombres que vas escribiendo
name = input("what's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")"""
#4
"""lo que hace este ejemplo es que va a saludar a todos los nombres que estan en el names.txt"""
with open("names.txt", (r)) as files:
    lines= file,readlines()
    print("")