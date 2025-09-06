class Cane:
    def parla(self):
        print("Bau")

class Gatto:
    def parla(self):
        print("Miao")


def fai_parlare(animale):
    animale.parla()

cane = Cane()
gatto = Gatto()
fai_parlare(cane)  # Output: Bau
fai_parlare(gatto)  # Output: Miao


class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")
class Quadrato:
    def disegna(self):
        print("Disegno un quadrato")

def disegna_forma(forma):
    forma.disegna()

figure = [Cerchio(), Quadrato()]

for figura in figure:
    disegna_forma(figura)    # Output: Disegno un cerchio
    #         Disegno un quadrato

