from Zwierze import Zwierze
import random

class Antylopa(Zwierze):

    def __init__(self, pozX, pozY, p):
        super(Antylopa, self).__init__(p)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Antylope"
        self._color = "indian red"
        self._wiek = 0
        self._sila = 4
        self._inicjatywa = 4

    def akcja(self):
        self._wiek += 1
        proba = 0
        kier = 0
        zwrot = 0
        #	1
        #4	  2
        #	3
        kierunek = random.randint(1,4)
        if kierunek == 1:
            if self._pozY > 1:
                if self._plansza.czyWolne(self._pozX, self._pozY - 2) == False:
                    self.kolizja(self._pozX, self._pozY, self._pozX, self._pozY - 2)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX, self._pozY - 2)
                    self._pozY = self._pozY - 2
        elif kierunek == 2:
            if self._pozX < 17:
                if self._plansza.czyWolne(self._pozX + 2, self._pozY) == False:
                    self.kolizja(self._pozX, self._pozY, self._pozX + 2, self._pozY)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX + 2, self._pozY)
                    self._pozX = self._pozX + 2
        elif kierunek == 3:
            if self._pozY < 17:
                if self._plansza.czyWolne(self._pozX, self._pozY + 2) == False:
                    self.kolizja(self._pozX, self._pozY, self._pozX, self._pozY + 2)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX, self._pozY + 2)
                    self._pozY = self._pozY + 2
        elif kierunek == 4:
            if self._pozX > 1:
                if self._plansza.czyWolne(self._pozX - 2, self._pozY) == False:
                    self.kolizja(self._pozX, self._pozY, self._pozX - 2, self._pozY)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX - 2, self._pozY)
                    self._pozX -= 2

    def noweZwierze(self, x, y):
        self._plansza.dodajOrganizm(Antylopa(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowa Antylopa\n")


    def czyUciekl(self):
        if random.randint(1,2) == 1:
            if self._plansza.czyWolne(self._pozX - 1, self._pozY) == True:
                self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX - 1, self._pozY)
                self._pozX -= 1
            elif self._plansza.czyWolne(self._pozX, self._pozY + 1) == True:
                self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX, self._pozY + 1)
                self._pozY += 1
            elif self._plansza.czyWolne(self._pozX + 1, self._pozY) == True:
                self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX + 1, self._pozY)
                self._pozX += 1
            elif self._plansza.czyWolne(self._pozX, self._pozY - 1) == False:
                self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX, self._pozY - 1)
                self._pozY -= 1
                self._plansza.dodajDoRaport("Antyllopa uciekła\n")
            return True
        else:
            return False