KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.lukujono:
            return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n) is False:
            self.lukujono[self.alkioiden_lkm] = n
            self.lukujono.append([0])
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            
            return True

        return False

    def poista(self, n):
        try:
            kohta = self.lukujono.index(n)
        except ValueError:
            return False # value not in list 
        self.lukujono.pop(kohta)
        self.alkioiden_lkm = self.alkioiden_lkm - 1
        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [self.lukujono[x] for x in range(0,self.alkioiden_lkm)]

    @staticmethod
    def yhdiste(a, b):
        yhdiste_taulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        yhdiste = a_taulu + b_taulu
        for numero in yhdiste:
            yhdiste_taulu.lisaa(numero)

        return yhdiste_taulu

    @staticmethod
    def leikkaus(a, b):
        leikkaus_taulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus_taulu.lisaa(b_taulu[j])

        return leikkaus_taulu

    @staticmethod
    def erotus(a, b):
        erotus_taulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        
        for i in range(0, len(a_taulu)):
            erotus_taulu.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus_taulu.poista(b_taulu[i])

        return erotus_taulu

    def __str__(self):
        tuotos = "{"
        if self.alkioiden_lkm == 0:
            pass
        else:
            tuotos += (', '.join(map(str, self.lukujono[:self.alkioiden_lkm])))
        tuotos += "}"
        return tuotos