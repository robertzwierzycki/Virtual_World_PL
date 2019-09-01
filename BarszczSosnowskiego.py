from Roslina import Roslina

class BarszczSosnowskiego(Roslina):

    def __init__(self, pozX, pozY, p):
        super(BarszczSosnowskiego, self).__init__(p)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Barszcz"
        self._color = "dark olive green"
        self._wiek = 0
        self._sila = 10
        self._inicjatywa = 0

    def akcja(self):
        if self._pozY > 0:
            if self._plansza.czyWolne(self._pozX, self._pozY - 1) == False:
                if self._plansza.getPola(self._pozX,self._pozY-1).czyMogeUsunac() == True:
                    self._plansza.usunOrganizm(self._plansza.getPola(self._pozX, self._pozY - 1))
        if self._pozX < 18:
            if self._plansza.czyWolne(self._pozX + 1, self._pozY) == False:
                if self._plansza.getPola(self._pozX + 1, self._pozY).czyMogeUsunac() == True:
                    self._plansza.usunOrganizm(self._plansza.getPola(self._pozX + 1, self._pozY))
        if self._pozY < 18:
            if self._plansza.czyWolne(self._pozX, self._pozY + 1) == False:
                if self._plansza.getPola(self._pozX, self._pozY + 1).czyMogeUsunac() == True:
                    self._plansza.usunOrganizm(self._plansza.getPola(self._pozX, self._pozY + 1))
        if self._pozX > 0:
            if self._plansza.czyWolne(self._pozX - 1, self._pozY) == False:
                if self._plansza.getPola(self._pozX - 1, self._pozY).czyMogeUsunac() == True:
                    self._plansza.usunOrganizm(self._plansza.getPola(self._pozX - 1, self._pozY))

    def nowaRoslina(self, x, y):
        self._plansza.dodajOrganizm(BarszczSosnowskiego(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowy Barszcz\n")