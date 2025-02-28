import random
import time

# Mängija klass
class Mängija:
    def __init__(self, nimi):
        self.nimi = nimi
        self.raha = 1000  # Algrahaga
        self.äri_tase = 1  # Algus
        self.kaupade_varud = {'E-sigaretid': 10, 'Telefonid': 5, 'Rõivad': 3}
        self.raha_pesemise_etapp = 1  # Raha pesemise etapp alguses

    def müüa_tooteid(self):
        """Simuleerib tavaliste kaupade müüki"""
        print("Müügi võimalused: ")
        for toode, kogus in self.kaupade_varud.items():
            print(f"{toode}: {kogus} ühikut, hind: {random.randint(50, 200)} EUR igaüks")
        
        valik = input("Mida soovid müüa? Valik (1: E-sigaretid, 2: Telefonid, 3: Rõivad): ")
        if valik == '1':
            tulu = self.kaupade_varud['E-sigaretid'] * random.randint(50, 150)
            print(f"Müüsid e-sigarettide koguse, teenides {tulu} EUR.")
            self.raha += tulu
            self.kaupade_varud['E-sigaretid'] = 0
        elif valik == '2':
            tulu = self.kaupade_varud['Telefonid'] * random.randint(100, 300)
            print(f"Müüsid telefonid, teenides {tulu} EUR.")
            self.raha += tulu
            self.kaupade_varud['Telefonid'] = 0
        elif valik == '3':
            tulu = self.kaupade_varud['Rõivad'] * random.randint(30, 100)
            print(f"Müüsid rõivad, teenides {tulu} EUR.")
            self.raha += tulu
            self.kaupade_varud['Rõivad'] = 0
        else:
            print("Vigane valik.")
    
    def raha_pesemine(self):
        """Raha pesemise spetsiifilised etapid"""
        print("Raha pesemise valikud: ")
        print("1. Kasutada kuritegevuse kanaleid")
        print("2. Läbipaistmatu investeeringud (nt ettevõtted, kinnisvara)")
        print("3. Altkäemaksu kaudu raha liikumine")
        
        valik = input("Vali meetod: ")
        if valik == '1':
            õnn = random.random() * self.raha_pesemise_etapp
            if õnn > 0.7:
                teenitud = random.randint(200, 500)
                self.raha += teenitud
                print(f"Õnnestus kasutada kuritegevuse kanaleid! Teenitud: {teenitud} EUR.")
            else:
                kaotus = random.randint(100, 300)
                self.raha -= kaotus
                print(f"Raha pesemine ei õnnestunud. Kaotus: {kaotus} EUR.")
        elif valik == '2':
            õnn = random.random() * (self.raha_pesemise_etapp / 2)
            if õnn > 0.5:
                teenitud = random.randint(150, 400)
                self.raha += teenitud
                print(f"Õnnestus raha pesta läbi investeeringud! Teenitud: {teenitud} EUR.")
            else:
                print("Investeeringud ei toonud soovitud tulemusi.")
        elif valik == '3':
            altkäemaksu_võimalus = random.random()
            if altkäemaksu_võimalus > 0.4:
                teenitud = random.randint(100, 250)
                self.raha += teenitud
                print(f"Altkäemaks toimis! Teenitud: {teenitud} EUR.")
            else:
                kaotus = random.randint(50, 150)
                self.raha -= kaotus
                print(f"Altkäemaks ei õnnestunud. Kaotus: {kaotus} EUR.")
        else:
            print("Vigane valik.")
        
        # Raha pesemise etapi areng
        self.raha_pesemise_etapp += 0.1
        print(f"Raha pesemise etapp tõusis tasemele: {self.raha_pesemise_etapp:.1f}")

    def politsei_ohud(self):
        """Politsei ohud mängus"""
        if random.random() < 0.1 * self.raha_pesemise_etapp:  # Mida kõrgem tasemele, seda suurem risk
            trahv = random.randint(200, 600)
            self.raha -= trahv
            print(f"Politsei leidis kahtlase tegevuse! Traktide trahv: {trahv} EUR.")
        else:
            print("Politseil ei õnnestunud midagi leida.")

# Mängu käivitamine
def mäng():
    nimi = input("Sisesta oma mängija nimi: ")
    mängija = Mängija(nimi)

    for päev in range(1, 11):  # Mäng kestab 10 päeva
        print(f"\nPäev {päev}:")
        print(f"Praegu on sul raha: {mängija.raha} EUR.")
        
        tegevus = input("Kas soovid teha raha pesemist (1), müüa tooteid (2) või vaadata politsei olukorda (3)? ")

        if tegevus == '1':
            mängija.raha_pesemine()
        elif tegevus == '2':
            mängija.müüa_tooteid()
        elif tegevus == '3':
            mängija.politsei_ohud()
        else:
            print("Vigane valik.")

        if mängija.raha <= 0:
            print("Sul ei ole enam raha! Mäng on läbi.")
            break

        time.sleep(1)  # Oodake veidi enne järgmise päeva algust

    print(f"Kui kaugele jõudsid, {mängija.nimi}? Lõpetasite mängu summaga: {mängija.raha} EUR.")

# Mängu käivitamine
if __name__ == "__main__":
    mäng()
