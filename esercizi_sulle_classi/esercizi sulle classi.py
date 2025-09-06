'''
Esercizi sulle classi in Python
Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
1.Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore
__init__ che accetta due parametri: nome (nome del ristorante) e
tipo cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere
impostato su False di default (cioè, il ristorante è chiuso).
Un dizionario menu dove dentro ci sono i piatti e prezzi che ha il ristorante
2.Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il
tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che
il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica
che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu'''

class ristorante:

    aperto = False  # attributo di classe
    
    dizionario_menu = {
        "Spaghetti Carbonara": 8.50,
        "Margherita Pizza": 7.00,
        "Tiramisu": 5.00,
        "Insalata Caprese": 6.50
    }
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina

    def descrivi_ristorante(self):
        return f"{self.nome} offre cucina {self.tipo_cucina}."
    def apri_ristorante(self):
        ristorante.aperto = True
        return f"{self.nome} è ora aperto!"
    def chiudi_ristorante(self):
        ristorante.aperto = False
        return f"{self.nome} è ora chiuso."
    def mostra_menu(self):
        menu = "Menu:\n"
        for piatto, prezzo in ristorante.dizionario_menu.items():
            menu += f"{piatto}: €{prezzo:.2f}\n"
        return menu
    def aggiungi_piatto(self, piatto, prezzo):
        ristorante.dizionario_menu[piatto] = prezzo
        return f"{piatto} è stato aggiunto al menu a €{prezzo:.2f}."
    def rimuovi_piatto(self, piatto):
        if piatto in ristorante.dizionario_menu:
            del ristorante.dizionario_menu[piatto]
            return f"{piatto} è stato rimosso dal menu."
        else:
            return f"{piatto} non è presente nel menu."
        
    def StampaMenu(self):
            for piatto, prezzo in ristorante.dizionario_menu.items():
                print(f"{piatto}: €{prezzo:.2f}")                       

# Esempio di utilizzo
class Prodotto:
    nome = ""
    costo_produzione = 0.0
    prezzo_vendita = 0.0
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
class Laptop(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita, specifiche):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.specifiche = specifiche
    
    def mostra_specifiche(self):
        return f"Specifiche del laptop {self.nome}: {self.specifiche}"

class Smartphone(Prodotto):
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, sistema_operativo):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.sistema_operativo = sistema_operativo
    
    def mostra_sistema_operativo(self):
        return f"Il sistema operativo dello smartphone {self.nome} è {self.sistema_operativo}"

'''3. Classe Fabbrica:
Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che produce e vende vari
tipi di prodotti. Gli studenti dovranno creare una classe base chiamata Prodotto e diverse classi parallele che rappresentano diversi tipi di prodotti. Inoltre, dovranno creare una classe Fabbrica che gestisce l'inventario e le vendite dei prodotti.
1. Classe Prodotto:
Attributi:
nome (stringa che descrive il nome del prodotto)
costo_produzione (costo per produrre il prodotto)
prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
Metodi:
calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
2. Classi parallele:
Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e
garanzia per Elettronica.
3. Classe Fabbrica:
Attributi:
inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
Metodi:
aggiungi_prodotto: aggiunge prodotti all'inventario.
vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.'''

class Fabbrica:
    prodotti = []  # attributo di classe per tenere traccia dei prodotti

    def __init__(self, nome):
        self.nome = nome

    def aggiungi_prodotto(self, prodotto):
        Fabbrica.prodotti.append(prodotto)
        return f"Prodotto {prodotto.nome} aggiunto alla fabbrica {self.nome}."

    def rimuovi_prodotto(self, prodotto):
        if prodotto in Fabbrica.prodotti:
            Fabbrica.prodotti.remove(prodotto)
            return f"Prodotto {prodotto.nome} rimosso dalla fabbrica {self.nome}."
        else:
            return f"Prodotto {prodotto.nome} non trovato nella fabbrica {self.nome}."

    def mostra_prodotti(self):
        if not Fabbrica.prodotti:
            return "Nessun prodotto disponibile."
        lista_prodotti = "Prodotti disponibili:\n"
        for prodotto in Fabbrica.prodotti:
            lista_prodotti += f"- {prodotto.nome}: Prezzo di vendita €{prodotto.prezzo_vendita:.2f}, Costo di produzione €{prodotto.costo_produzione:.2f}, Profitto €{prodotto.calcola_profitto():.2f}\n"
        return lista_prodotti