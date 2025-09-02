# Data
coin = 0

isLoggedClient = False
isLoggedAdmin = False

clienti = [
    {"username": "cliente", "password": "cliente"}
]

amministratori = [
    {"username": "admin", "password": "admin"}
]

articoli = [
    {"Nome": "Warcraft", "Prezzo": 19.99, "Quantita": 10}
]

# ---------------- Funzioni ----------------
def AddCliente(username, password):
    newClient = {"username": username, "password": password}
    clienti.append(newClient)

def LoginClient(username, password):
    for cliente in clienti:
        if cliente["username"] == username and cliente["password"] == password:
            return True
    return False
        
def AddAdmin(username, password):
    newAdmin = {"username": username, "password": password}
    amministratori.append(newAdmin)

def LoginAdmin(username, password):
    for amministratore in amministratori:
        if amministratore["username"] == username and amministratore["password"] == password:
            return True
    return False

def AggiungiArticolo(NomeArticolo, Prezzo, Quantita):
    nuovo = {"Nome": NomeArticolo, "Prezzo": Prezzo, "Quantita": Quantita}
    articoli.append(nuovo)

def RimuoviArticolo(NomeArticolo):
    for articolo in articoli:
        if articolo["Nome"].lower() == NomeArticolo.lower():
            articoli.remove(articolo)
            print(f"Articolo {NomeArticolo} rimosso.")
            return
    print("Articolo non trovato.")

# ---------------- MAIN LOOP ----------------
print("Benvenuto Gestionale clienti e azienda \n")

while True:
    choose = int(input("Menu \n 1-Login Cliente \n 2-Login Amministrazione e Gestione \n"))

    # Login Cliente
    if choose == 1:
        username = input("Inserisci Username: ").lower()
        password = input("Inserisci Password: ").lower()
        isLoggedClient = LoginClient(username, password)

    # Login Admin
    if choose == 2:
        username = input("Inserisci Username: ").lower()
        password = input("Inserisci Password: ").lower()
        isLoggedAdmin = LoginAdmin(username, password)

    # Gestione clienti
    if isLoggedClient:
        print("Menu Cliente \n")
        scelta = int(input("1-Visualizza articoli \n2-Compra un articolo \n3-Aggiungi credito \n"))
        
        # Visualizza articoli
        if scelta == 1:
            print("Stampa tutti gli articoli: ")
            for i, articolo in enumerate(articoli, start=1):
                print(f"{i}. {articolo['Nome']} - €{articolo['Prezzo']} (Disponibili: {articolo['Quantita']})")

        # Compra un articolo
        if scelta == 2:
            NomeArticolo = input("Inserisci il nome dell'articolo: ").lower()
            trovato = False
            for articolo in articoli:
                if articolo["Nome"].lower() == NomeArticolo:
                    trovato = True
                    if coin >= articolo["Prezzo"]:
                        print(f"Articolo acquistato: {articolo['Nome']}")
                        articolo["Quantita"] -= 1
                        coin -= articolo["Prezzo"]
                    else:
                        print("Credito non sufficiente")
                    break
            if not trovato:
                print("Articolo non trovato")

        # Aggiungi credito
        if scelta == 3:
            amount = float(input("Aggiungi Fondi - Inserisci la somma: "))
            coin += amount
            print(f"Credito attuale: €{coin}")

    # Amministrazione
    if isLoggedAdmin:
        print("Menu Amministrazione e Gestione \n")
        scelta = int(input("1-Visualizza articoli \n2-Aggiungi articolo \n3-Rimuovi articolo\n"))

        # Visualizza articoli
        if scelta == 1:
            print("Stampa tutti gli articoli: ")
            for i, articolo in enumerate(articoli, start=1):
                print(f"{i}. {articolo['Nome']} - €{articolo['Prezzo']} (Disponibili: {articolo['Quantita']})")

        # Aggiungi articolo
        if scelta == 2:
            NomeArticolo = input("Inserisci il nome del articolo: ").lower()
            Prezzo = float(input("Inserisci il prezzo del articolo: "))
            Quantita = int(input("Inserisci la quantita del articolo: "))
            AggiungiArticolo(NomeArticolo, Prezzo, Quantita)

        # Rimuovi articolo
        if scelta == 3:
            NomeArticolo = input("Inserisci il nome del articolo: ").lower()
            RimuoviArticolo(NomeArticolo)
