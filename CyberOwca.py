from Zwierze import Zwierze
import random

class CyberOwca(Zwierze):

    def __init__(self, pozX, pozY, p):
        super(CyberOwca, self).__init__(p)
        self._pozX = pozX
        self._pozY = pozY
        self._symbol = "Cyber_Owce"
        self._color = "black"
        self._wiek = 0
        self._sila = 11
        self._inicjatywa = 4

    def akcja(self):
        self._wiek += 1
        proba = 0
        kier = 0
        zwrot = 0
        #	1
        #4	  2
        #	3
        kierunek = 0
        o = self._plansza.findBarszcz(self._pozX,self._pozY)
        if o != 0:
            if self._pozX-o.get_pozX()<0:
                kierunek = 2
            elif o.get_pozX()-self._pozX<0:
                kierunek = 4
            elif self._pozY-o.get_pozY()<0:
                kierunek = 3
            elif o.get_pozY()-self._pozY<0:
                kierunek = 1
        else:
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
        self._plansza.dodajOrganizm(CyberOwca(x, y, self._plansza), self._plansza)
        self._plansza.dodajDoRaport("Nowa Cyber Owca\n")

    def czyMogeUsunac(self):
        return False