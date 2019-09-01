from Roslina import Roslina

class Trawa(Roslina):

    def __init__(self, pozX, pozY, s):
        super(Trawa, self).__init__(s)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Trawe"
        self._color = "green"
        self._wiek = 0
        self._sila = 0
        self._inicjatywa = 0

    def nowaRoslina(self, x, y):
        self._plansza.dodajOrganizm(Trawa(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowa Trawa\n")
