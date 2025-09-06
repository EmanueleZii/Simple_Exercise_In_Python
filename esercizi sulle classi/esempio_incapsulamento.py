
class Computer:
    def __init__(self):
        self.__processore = "Intel i5" # Attributo privato

def get_processore(self):
    return self.__processore

def set_processore(self, processore):
    self.__processore = processore

pc = Computer()
print(pc.get_processore())
# Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5")

# Modifica l'attributo privato tramite il setter
print(pc.get_processore())



# esempio di livelli di accesso
# Variabile globale
numero = 10

def funzione_esterna():
    # Variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione esterna (locale):", numero)

def funzione_interna():
    # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
    nonlocal numero
    numero = 3
    print("Numero dentro funzione interna (nonlocal):", numero)

funzione_interna()
print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)


#private variable in a class
class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"

    def __metodo_privato(self):
        return "Questo è un metodo privato"

obj = MiaClasse()

# Stampando direttamente la variabile privata solleverà un'eccezione
# print(obj.__variabile_privata) # AttributeError
# L'accesso corretto (che dovrebbe essere evitato) sarebbe:
print(obj._MiaClasse__variabile_privata) # Funzionerà, ma non è buona prassi

def __metodo_privato(self):
    return "Questo è un metodo privato"

obj = MiaClasse()
# Stampando direttamente la variabile privata solleverà un'eccezione
# print(obj.__variabile_privata) # AttributeError
# L'accesso corretto (che dovrebbe essere evitato) sarebbe:
print(obj._MiaClasse__variabile_privata) # Funzionerà, ma non è buona prassi

# Stampa il valore restituito dal metodo privato
print(obj._MiaClasse__metodo_privato()) # Funzionerà, ma non è buona prassi
print(obj._MiaClasse__variabile_privata) # Funzionerà, ma non è buona prassi