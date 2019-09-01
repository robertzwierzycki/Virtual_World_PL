from Zwierze import Zwierze
import random

class Zolw(Zwierze):

    def __init__(self, pozX, pozY, p):
        super(Zolw, self).__init__(p)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Zolwia"
        self._color = "brown"
        self._wiek = 0
        self._sila = 2
        self._inicjatywa = 1

    def akcja(self):
        ruszamy = random.randint(1,4)
        if ruszamy == 3:
            super(Zolw, self).akcja()

    def noweZwierze(self, x, y):
        self._plansza.dodajOrganizm(Zolw(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowy Żółw\n")


    def czyOdparlAtak(self, a):
        if a < 5:
            self._plansza.dodajDoRaport("Zolw odparł atak\n")
            print("Zolw odparł atak")
            return True
        else:
            return False