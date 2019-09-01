
class Organizm:
    def __init__(self, p):
        self._plansza = p
        self._pozX = 0
        self._pozY = 0
        self._sila = 0
        self._inicjatywa = 0
        self._wiek = 0
        self._symbol = "Wilk"
        self._color = "black"

    def get_pozX(self):
        return self._pozX

    def get_pozY(self):
        return self._pozY

    def set_pozX(self, _pozX):
        self._pozX = _pozX

    def set_pozY(self, _pozY):
        self._pozY = _pozY

    def czyMogeUsunac(self):
        return True

    def getSila(self):
        return self._sila

    def getColor(self):
        return self._color

    def czyOdparlAtak(self, a):
        return False

    def czyUciekl(self):
        return False

    def trujacaRoslina(self, a, b):
        return False

    def setSila(self, sila):
        self._sila = sila

    def getInicjatywa(self):
        return self._inicjatywa

    def getWiek(self):
        return self._wiek

    def getSymbol(self):
        return self._symbol

    def akcja(self):
        pass

    def kolizja(self, xp, yp, xk, yk):
        pass

    def rysowanie(self):
        self._plansza.bChangeColor(self._pozX, self._pozY, self._color, self._symbol)
