cost = float(input("Inserisci il costo totale: "))
NumPeople = int(input("Inserisci il numero di persone: "))
give = float(input("Inserisci la mancia (in percentuale, es. 0.1 per 10%): "))

tip_as_percent = give / 100
total_tip_amount = cost * tip_as_percent
total_bill = cost + total_tip_amount
bill_per_percent = total_bill / NumPeople
final_amount = round(bill_per_percent, 2)

print(f"Ogni persona deve pagare: {final_amount}")








