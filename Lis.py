from Zwierze import Zwierze
import random

class Lis(Zwierze):

    def __init__(self, pozX, pozY, s):
        super(Lis, self).__init__(s)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Lisa"
        self._color = "red"
        self._wiek = 0
        self._sila = 3
        self._inicjatywa = 7

    def akcja(self):
        self._wiek += 1
        #	1
        # 4	  2
        #	3
        kierunek = random.randint(1,4)
        if kierunek == 1:
            if self._pozY > 0:
                if self._plansza.czyWolne(self._pozX, self._pozY - 1) == False:
                    if self.sprPrzeciwnika(self._pozX, self._pozY - 1) < self.getSila():
                        self.kolizja(self._pozX, self._pozY, self._pozX, self._pozY - 1)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX, self._pozY - 1)
                    self._pozY -= 1
        elif kierunek == 2:
            if self._pozX < 18:
                if self._plansza.czyWolne(self._pozX + 1, self._pozY) == False:
                    if self.sprPrzeciwnika(self._pozX + 1, self._pozY) < self.getSila():
                        self.kolizja(self._pozX, self._pozY, self._pozX + 1, self._pozY)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX + 1, self._pozY)
                    self._pozX += 1
        elif kierunek == 3:
            if self._pozY < 18:
                if self._plansza.czyWolne(self._pozX, self._pozY + 1) == False:
                    if self.sprPrzeciwnika(self._pozX, self._pozY + 1) < self.getSila():
                        self.kolizja(self._pozX, self._pozY, self._pozX, self._pozY + 1)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX, self._pozY + 1)
                    self._pozY += 1
        elif kierunek == 4:
            if self._pozX > 0:
                if self._plansza.czyWolne(self._pozX - 1, self._pozY) == False:
                    if self.sprPrzeciwnika(self._pozX - 1, self._pozY) < self.getSila():
                        self.kolizja(self._pozX, self._pozY, self._pozX - 1, self._pozY)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX - 1, self._pozY)
                    self._pozX -= 1

    def noweZwierze(self, x, y):
        self._plansza.dodajOrganizm(Lis(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowy Lis\n")

    def sprPrzeciwnika(self, x, y):
        o = self._plansza.getPola(x, y)
        return o.getSila()
