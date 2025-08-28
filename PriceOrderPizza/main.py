print("Benvenuto nel programma di ordinazione della pizza!")

size = input("Quale dimensione di pizza desideri? (piccola/media/grande) ")
pepperoni = input("Vuoi aggiungere pepperoni? (si/no) ")
extra_cheese = input("Vuoi aggiungere formaggio extra? (si/no) ")

bill = 0

if size == "piccola":
    bill += 5
elif size == "media":
    bill += 7
elif size == "grande":
    bill += 9

if pepperoni == "si":
    bill += 2

if extra_cheese == "si":
    bill += 1

print("Il tuo totale è: $" + str(bill))

