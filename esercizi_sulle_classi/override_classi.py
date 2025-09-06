class Animale:
    def emetti_suono(self):
        print("Questo animale fa un suono")

class Cane(Animale):
    def emetti_suono(self):
        print("Bau")

class Gatto(Animale):
    def emetti_suono(self):
        print("Miao")

class Cane(Animale):
    def emetti_suono(self):
        print("Bau")

class Gatto(Animale):
    def emetti_suono(self):
        print("Miao")
class Mucca(Animale):
    def emetti_suono(self):
        return super().emetti_suono()