# Scrittura su un file
file = open("file.txt", "w")
file.write("Ciao, mondo!\n")
file.write("Questa è una seconda riga.\n")

file.close()

# Lettura del file
file = open("file.txt", "r")
contenuto = file.read()
riga = file.readline()
print(contenuto)
print(riga)

file.close()

# Uso del costrutto with per gestire i file
with open("file.txt", "r") as file:
    contenuto = file.read()

# Aggiunta di contenuto al file
with open("file.txt", "w") as file:
    file.write(contenuto)
    file.write("Aggiunta di una nuova riga.\n") 
    file.write("E un'altra riga.\n")




    