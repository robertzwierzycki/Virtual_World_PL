from Roslina import  Roslina

class Mlecz(Roslina):

    def __init__(self, pozX, pozY, p):
        super(Mlecz, self).__init__(p)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Mlecza"
        self._color = "yellow"
        self._wiek = 0
        self._sila = 0
        self._inicjatywa = 0

    def akcja(self):
        i = 0
        while i < 3:
            super(Mlecz, self).akcja()
            i += 1

    def nowaRoslina(self, x, y):
        self._plansza.dodajOrganizm(Mlecz(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowy Mlecz\n")
