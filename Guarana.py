from Roslina import Roslina

class Guarana(Roslina):

    def __init__(self, pozX, pozY, s):
        super(Guarana, self).__init__(s)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Guarane"
        self._color = "sienna"
        self._wiek = 0
        self._sila = 0
        self._inicjatywa = 0

    def nowaRoslina(self, x, y):
        self._plansza.dodajOrganizm(Guarana(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowa Guarana\n")

    def trujacaRoslina(self, a, b):
        a.setSila(a.getSila() + 3)
        self._plansza.usunOrganizm(b)
        return True
