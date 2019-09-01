from Organizm import Organizm
import random

class Zwierze(Organizm):

    def __init__(self, p):
        super(Zwierze, self).__init__(p)

    def akcja(self):
        self._wiek += 1
        #	1
        # 4	  2
        #	3
        kierunek = random.randint(1,4)
        if kierunek == 1:
            if self._pozY > 0:
                if self._plansza.czyWolne(self._pozX, self._pozY - 1) == False:
                    self.kolizja(self._pozX, self._pozY, self._pozX, self._pozY - 1)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX, self._pozY - 1)
                    self._pozY -= 1
        elif kierunek == 2:
            if self._pozX < 18:
                if self._plansza.czyWolne(self._pozX + 1, self._pozY) == False:
                    self.kolizja(self._pozX, self._pozY, self._pozX + 1, self._pozY)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX + 1, self._pozY)
                    self._pozX += 1
        elif kierunek == 3:
            if self._pozY < 18:
                if self._plansza.czyWolne(self._pozX, self._pozY + 1) == False:
                    self.kolizja(self._pozX, self._pozY, self._pozX, self._pozY + 1)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX, self._pozY + 1)
                    self._pozY += 1
        elif kierunek == 4:
            if self._pozX > 0:
                if self._plansza.czyWolne(self._pozX - 1, self._pozY) == False:
                    self.kolizja(self._pozX, self._pozY, self._pozX - 1, self._pozY)
                else:
                    self._plansza.przeniesOrganizm(self._pozX, self._pozY, self._pozX - 1, self._pozY)
                    self._pozX -= 1

    def noweZwierze(self, x, y):
        pass


    def kolizja(self, xp, yp, xk, yk):
        o1 = self._plansza.getPola(xp, yp)
        o2 = self._plansza.getPola(xk, yk)
        if o2.trujacaRoslina(o1, o2) == False:
            if o2.getSymbol() != o1.getSymbol():
                z1 = o1.getSila()
                z2 = o2.getSila()
                if o2.czyUciekl() == True:
                    self._plansza.przeniesOrganizm(xp, yp, xk, yk)
                    self._pozX = self._pozX + (xk - xp)
                    self._pozY = self._pozY + (yk - yp)
                else:
                    if o2.czyOdparlAtak(z1) == True:
                        return
                    else:
                        if z1 >= z2:
                            self._plansza.usunOrganizm(o2)
                            self._plansza.przeniesOrganizm(xp, yp, xk, yk)
                            self._pozX = self._pozX + (xk - xp)
                            self._pozY = self._pozY + (yk - yp)
                        else:
                            self._plansza.usunOrganizm(o1)
            else:
                if self._pozY > 0:
                    if self._plansza.czyWolne(self._pozX, self._pozY - 1) == True:
                        self.noweZwierze(self._pozX, self._pozY - 1)
                elif self._pozX < 18:
                    if self._plansza.czyWolne(self._pozX + 1, self._pozY) == True:
                        self.noweZwierze(self._pozX + 1, self._pozY)
                elif self._pozY < 18:
                    if self._plansza.czyWolne(self._pozX, self._pozY + 1) == True:
                        self.noweZwierze(self._pozX, self._pozY + 1)
                elif self._pozX > 0:
                    if self._plansza.czyWolne(self._pozX - 1, self._pozY) == True:
                        self.noweZwierze(self._pozX - 1, self._pozY)
        else:
            self._plansza.przeniesOrganizm(xp, yp, xk, yk)
            self._pozX = self._pozX + (xk - xp)
            self._pozY = self._pozY + (yk - yp)