from Zwierze import Zwierze

class Owca(Zwierze):

    def __init__(self, pozX, pozY, p):
        super(Owca, self).__init__(p)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Owce"
        self._color = "white"
        self._wiek = 0
        self._sila = 4
        self._inicjatywa = 4

    # @Override
    def noweZwierze(self, x, y):
        self._plansza.dodajOrganizm(Owca(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowa Owca\n")
