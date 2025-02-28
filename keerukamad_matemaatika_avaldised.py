import random
import time

# Mängija klass
class Mängija:
    def __init__(self, nimi):
        self.nimi = nimi
        self.raha = 1000  # Algrahaga
        self.risk = 1  # Madal risk alguses
        self.äri_tase = 1  # Äri tase alguses

    def raha_pesemine(self):
        """Simuleerib raha pesemist"""
        print(f"{self.nimi} alustas raha pesemise protsessi.")
        õnn = random.random()  # Õnne määr mängib suurt rolli
        kui_õnnelik = self.risk * õnn
        if kui_õnnelik > 0.5:
            teenitud = random.randint(100, 500)  # Teenitud raha
            self.raha += teenitud
            print(f"Õnnestus raha pesta! Teenitud: {teenitud} EUR.")
        else:
            kaotus = random.randint(50, 200)
            self.raha -= kaotus
            print(f"Raha pesemine ei õnnestunud. Kaotus: {kaotus} EUR.")
        
    def äri_arenemine(self):
        """Simuleerib äri arendamist"""
        kasum = random.randint(100, 300)
        self.raha += kasum
        print(f"Äri kasvab! Teenitud tulu: {kasum} EUR.")

    def politsei_ohud(self):
        """Kontrollib, kas politsei avastab midagi"""
        if random.random() < 0.1 * self.risk:  # Mida kõrgem risk, seda suurem tõenäosus
            print("Politsei on avastanud kahtlase tegevuse!")
            karistus = random.randint(100, 500)
            self.raha -= karistus
            print(f"Politsei trahv: {karistus} EUR.")

# Mängu käivitamine
def mäng():
    nimi = input("Sisesta oma mängija nimi: ")
    mängija = Mängija(nimi)

    for päev in range(1, 11):  # Mäng kestab 10 päeva
        print(f"\nPäev {päev}:")
        print(f"Praegu on sul raha: {mängija.raha} EUR.")
        
        # Tegevuse valimine
        tegevus = input("Kas soovid teha raha pesemist (1), arendada äri (2) või vaadata politsei olukorda (3)? ")

        if tegevus == '1':
            mängija.raha_pesemine()
        elif tegevus == '2':
            mängija.äri_arenemine()
        elif tegevus == '3':
            mängija.politsei_ohud()
        else:
            print("Vigane valik.")
