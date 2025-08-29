import random

# Lista delle mosse
mosse = ["carta", "sasso", "forbici"]

def scegliRandom():
    return random.choice(mosse)

print("Benvenuto a carta forbici e sasso!")
utente = int(input("Premi 1 = carta, 2 = sasso, 3 = forbici: "))

# La scelta dell’utente (con -1 perché l’indice parte da 0)
utente_scelta = mosse[utente - 1]
computer_scelta = scegliRandom()

print("Tu hai scelto:", utente_scelta)
print("Il computer ha scelto:", computer_scelta)

# Regole del gioco
if utente_scelta == computer_scelta:
    print("Pareggio!")
elif utente_scelta == "carta":
    if computer_scelta == "sasso":
        print("Hai vinto! Carta batte Sasso.")
    else:
        print("Hai perso! Forbici battono Carta.")
elif utente_scelta == "sasso":
    if computer_scelta == "forbici":
        print("Hai vinto! Sasso batte Forbici.")
    else:
        print("Hai perso! Carta batte Sasso.")
elif utente_scelta == "forbici":
    if computer_scelta == "carta":
        print("Hai vinto! Forbici battono Carta.")
    else:
        print("Hai perso! Sasso batte Forbici.")