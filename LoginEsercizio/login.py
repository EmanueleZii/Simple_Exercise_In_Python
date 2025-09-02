'''
<summary>
    Scenario: Devi scrivere u n programma Python che simuli u n sistema di login. Il sistema deve permettere all'utente di
    inserire un nome utente e una password. Poi, deve verificare se la combinazione di nome utente e password è corretta.
    Per semplicità, puoi hardcodare nel codice una coppia di nome utente e password che sia considerata corretta.
    Requisiti:
        1. Input dell'Utente:
        • Il programma chiede all'utente di inserire il nome utente.
        • Poi, chiede all'utente di inserire la password.
        2. Verifica delle Credenziali:
        • Il programma controlla se il nome utente e la password inseriti corrispondono a quelli predefiniti.
        • Puoi decidere di avere le credenziali hardcoded nel codice per questo esercizio. Ad esempio, puoi usare "admin"
        come nome utente e "12345" come password.
        3. Output del Programma:
        • Se il nome utente e la password sono corretti, stampa u n messaggio di benvenuto.
        • Altrimenti, informa l'utente che le credenziali sono errate.
        4. Modifica dati del Programma:
        • Inserisci una condizione interna che si occupi di cambiare un dato specifico tra quelli inseriti
        • Appena loggato fai scegliere fra due opzioni di domanda segreta e la risposta ( qual'è il colore preferito, quale
        animale preferito)
</summary>
'''

db = [
    {
        "username": "admin",
        "password": "12345",
        "secret_question": "Qual è il tuo colore preferito?",
        "secret_answer": "blu",
        "secret_answer2": "gatto"
    }
]

isLogged = False

print("Benvenuto nel sistema di login! \n")
print("Inserisci le tue credenziali per effettuare il login. \n")

input_username = str(input("Nome utente:  \n")).lower()
input_password = str(input("Password: \n")).lower()

for user in db:
    if user["username"] == input_username and user["password"] == input_password:
        print("Login effettuato con successo!")
        secret_question = input("Qual è il tuo colore preferito o animale preferito? ")
        print("Hai scelto:", secret_question)
        isLogged = True
        break
else:
    isLogged = False
    print("Nome utente o password errati.")

print("\n")

if isLogged:
    print("Sei loggato!")


print("Menu: \n")
print("1. Cambiare la risposta alla domanda segreta \n")
print("2. Logout \n")
print("3. Cambiare la password \n")
print("4. Cambiare lo username \n")
print("5. Exit \n")

choice = int(input("Scegli un'opzione (1-5): \n"))

if choice == 1 and isLogged:
    new_answer = input("Inserisci la nuova risposta alla domanda segreta: \n")
    db[0]["secret_answer"] = new_answer
    print("Risposta alla domanda segreta aggiornata con successo!")

elif choice == 2 and isLogged:
    isLogged = False
    print("Logout effettuato con successo!")

elif choice == 3 and isLogged:
    new_password = input("Inserisci la nuova password: \n")
    db[0]["password"] = new_password
    print("Password aggiornata con successo!")

elif choice == 4 and isLogged:
    new_username = input("Inserisci il nuovo nome utente: \n")
    db[0]["username"] = new_username
    print("Nome utente aggiornato con successo!")

elif choice == 5:
    print("Uscita dal programma...")
    exit()

else:
    print("Operazione non valida o non sei loggato.")
