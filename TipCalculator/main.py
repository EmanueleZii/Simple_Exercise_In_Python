cost = float(input("Inserisci il costo totale: "))
NumPeople = int(input("Inserisci il numero di persone: "))
give = float(input("Inserisci la mancia (in percentuale, es. 0.1 per 10%): "))

result = (cost / NumPeople) * (1 + give)

print(f"Ogni persona deve pagare: {result:.2f}")



























