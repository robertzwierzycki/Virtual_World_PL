from Zwierze import Zwierze
class Wilk(Zwierze):

    def __init__(self, pozX,pozY,p):
        super(Wilk, self).__init__(p)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Wilka"
        self._color = "gray"
        self._wiek = 0
        self._sila = 9
        self._inicjatywa = 5

    def noweZwierze(self, x, y):
        self._plansza.dodajOrganizm(Wilk(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowy Wilk\n")
        print("Nowy Wilk")
