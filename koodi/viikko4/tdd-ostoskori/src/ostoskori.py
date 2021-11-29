from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavaroita = 0
        for tavara in self.ostoskori:
            tavaroita += tavara.lukumaara()
        return tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self.ostoskori:
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostos_korissa = [ostos for ostos in self.ostoskori if ostos.tuotteen_nimi() == lisattava.nimi()]
        if len(ostos_korissa) == 0:
            ostos = Ostos(lisattava)
            self.ostoskori.append(ostos)
        else:
            ostos_korissa[0].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        tuote_ostoskorissa = [ostos for ostos in self.ostoskori if ostos.tuotteen_nimi() == poistettava.nimi()]
        if len(tuote_ostoskorissa) == 0:
            return
        else:
            tuote = tuote_ostoskorissa[0]
            if tuote.lukumaara() > 1:
                tuote.muuta_lukumaaraa(-1)
            else:
                self.ostoskori = [ostos for ostos in self.ostoskori if ostos.tuotteen_nimi() != poistettava.nimi()]

        

    def tyhjenna(self):
        self.ostoskori = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
