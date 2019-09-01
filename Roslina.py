from Organizm import Organizm
import random
class Roslina(Organizm):

    def __init__(self, p):
        super(Roslina, self).__init__(p)

    def akcja(self):
        self._wiek += 1
        rozsiej = random.randint(1,14)
        if rozsiej == 1:
            kierunek = random.randint(1,4)
            if kierunek == 1:
                if self._pozY > 0:
                    if self._plansza.czyWolne(self._pozX, self._pozY - 1) == True:
                        self.nowaRoslina(self._pozX, self._pozY - 1)
            elif kierunek == 2:
                if self._pozX < 18:
                    if self._plansza.czyWolne(self._pozX + 1, self._pozY) == True:
                        self.nowaRoslina(self._pozX + 1, self._pozY)
            elif kierunek == 3:
                if self._pozY < 18:
                    if self._plansza.czyWolne(self._pozX, self._pozY + 1) == True:
                        self.nowaRoslina(self._pozX, self._pozY + 1)
            elif kierunek == 4:
                if self._pozX > 0:
                    if self._plansza.czyWolne(self._pozX - 1, self._pozY) == True:
                        self.nowaRoslina(self._pozX - 1, self._pozY)

    def nowaRoslina(self, x, y):
        pass
