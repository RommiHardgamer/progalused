class taisnurkne_kolmnurk:
    def __init__(self, kylg):
        self.kylg = kylg

    def pindala(self):
        return (self.kylg**2) / 2


kolmnurk = taisnurkne_kolmnurk(8)
print(kolmnurk.pindala())  