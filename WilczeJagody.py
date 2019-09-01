from Roslina import Roslina
class WilczeJagody(Roslina):

    def __init__(self, pozX, pozY, s):
        super(WilczeJagody, self).__init__(s)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Wilcze_Jagody"
        self._color = "purple"
        self._wiek = 0
        self._sila = 99
        self._inicjatywa = 0

    def nowaRoslina(self, x, y):
        self._plansza.dodajOrganizm(WilczeJagody(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowe W. Jagody\n")

    def trujacaRoslina(self, a, b):
        self._plansza.usunOrganizm(a)
        self._plansza.usunOrganizm(b)
        return True
