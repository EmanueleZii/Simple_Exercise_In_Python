
'''Esercizi sulle classi in Python
Creare una classe ContoBancario che incapsula le informazioni di un conto e
fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare
l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto. '''

class ContoBancario:
    def __init__(self, nome_titolare, saldo_iniziale=0):
        self.nome_titolare = nome_titolare
        self.saldo = saldo_iniziale

    def deposita(self, importo):
        if importo > 0:
            self.saldo += importo
            print(f"Deposito di {importo} effettuato. Saldo attuale: {self.saldo}")
        else:
            print("L'importo del deposito deve essere positivo.")

    def preleva(self, importo):
        if importo > 0:
            if importo <= self.saldo:
                self.saldo -= importo
                print(f"Prelievo di {importo} effettuato. Saldo attuale: {self.saldo}")
            else:
                print("Fondi insufficienti per il prelievo.")
        else:
            print("L'importo del prelievo deve essere positivo.")

    def mostra_saldo(self):
        print(f"Saldo attuale: {self.saldo}")


