from Zwierze import Zwierze
import random
from tkinter import Label
class Czlowiek(Zwierze):

    def __init__(self, pozX, pozY, p):
        super(Czlowiek, self).__init__(p)
        self._pozX = pozX
        self._pozY = pozY
        self._color = "blue"
        self._symbol = "C"
        self._wiek = 0
        self._q = 0
        self._sila = 5
        self._inicjatywa = 4
        self._turaUzycaSkill = -10

    def akcja(self):
        self._wiek += 1
        kierunek = self._plansza.getK_czlowieka()
        if kierunek == 0:
            pass
        elif kierunek == 1:
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
        elif kierunek == 5:
            self.skill()
            self._plansza.setK_czlowieka(0)
        if self._q > 0:
            s = 'Aktywowano Specjalną Umiejętność - siła = %d' % (self._sila)
            self._plansza.lSkill(s)
            print("Aktywowano Specjalną Umiejętność - siła = ", self._sila)
            self._sila -= 1
            self._q -= 1

    def noweZwierze(self, x, y):
        pass

    def skill(self):
        if self._turaUzycaSkill + 10 <= self._plansza.getNr_Tury():
            self._plansza.dodajDoRaport("Aktywowano Skill\n")
            print("aktywowano skill")
            self._turaUzycaSkill = self._plansza.getNr_Tury()
            self._sila = self._sila + 5
            self._q = 5
