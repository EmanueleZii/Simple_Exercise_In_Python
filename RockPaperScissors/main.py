import random

arr = ["paper", "rock", "scissor"]
# La scelta dell’utente (con -1 perché l’indice parte da 0)
utente_scelta = arr[utente - 1]
computer_scelta = scegliRandom()

print("Tu hai scelto:", utente_scelta)
print("Il computer ha scelto:", computer_scelta)

def scegliRandom():
    return random.choice(arr)

print("Benvenuto a carta forbici e sasso")

utente = int(input("Premi 1 = carta 2 = sasso 3 = forbici"))

if computerscelta == utente:
    print("Pareggio")
elif utente_scelta == "carta":
    if computer_scelta == "sasso":
        print("Hai vinto! Carta batte Sasso.")
    else:
        print("Hai perso! Forbici battono Carta.")
elif utente == "sasso":
    if computer_scelta == "forbici":
        print("Hai vinto! Sasso batte Forbici.")
    else:
        print("Hai perso! Carta batte Sasso.")
elif utente == "forbici":
    if computer_scelta == "carta":
        print("Hai vinto! Forbici battono Carta.")
    else:
        print("Hai perso! Sasso batte Forbici.")
