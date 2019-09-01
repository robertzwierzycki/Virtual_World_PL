from tkinter import *
from Antylopa import Antylopa
from BarszczSosnowskiego import BarszczSosnowskiego
from CyberOwca import CyberOwca
from Czlowiek import Czlowiek
from Guarana import Guarana
from Lis import Lis
from Mlecz import Mlecz
from Owca import Owca
from Trawa import Trawa
from WilczeJagody import WilczeJagody
from Wilk import Wilk
from Zolw import Zolw
from tkinter import messagebox
from typing import List, Any
import linecache

class Swiat(object):
    okno = Tk()
    okno.minsize(width=600, height=450)
    okno.geometry('%dx%d+%d+%d' % (600, 450, 80, 80))
    okno.config(bg="green")
    okno.title("Robert Zwierzycki 172121")
    buttons = [[0 for x in range(20)] for y in range(20)]
    pola = [[0 for x in range(19)] for y in range(19)]
    for x in range(19):
        for y in range(19):
            pola[x][y]=None
    popup = Menu(okno, tearoff=0)
    T = Text(okno, height=20, width=20,borderwidth=3)
    T.place(x=420,y=30)
    vec = []
    ilosc_org = 0
    nr_Tury = 0
    k_czlowieka=0
    newX=0
    newY=0

    def czyWolne(self, x, y):
        #print(x,y)
        if self.pola[y][x] == None:
            return True
        else:
            # System.out.println("Zajete pole" + x + " " + y + "\n");
            return False

    def wykonajTure(self):
        self.nr_Tury += 1
        i = 0
        self.T.delete(1.0,END)
        self.lSkill("")
        #print(self.ilosc_org)
        while i < self.ilosc_org:
            self.vec[i].akcja()
            i += 1

    # System.out.println(ilosc_org);
    def getPola(self, x, y):
        return self.pola[y][x]

    def getK_czlowieka(self):
        return self.k_czlowieka

    def setK_czlowieka(self, k_czlowieka):
        self._k_czlowieka = k_czlowieka

    def setKoniec(self, koniec):
        self._koniec = koniec

    w = Label(okno, text="",bg="green",font=("Helvetica", 12))
    def lSkill(self,s):
        self.w.configure(text=s)
        self.w.place(x=40,y=410)

    def findBarszcz(self,x,y):
        dxy=100
        X = -1
        Y = -1
        i = 0
        while i < self.ilosc_org:
            if self.vec[i].getSymbol() == "Barszcz":
                if abs(self.vec[i].get_pozX()-x)+abs(self.vec[i].get_pozY()-y)<dxy :
                    X = self.vec[i].get_pozX()
                    Y = self.vec[i].get_pozY()
                    dxy = abs(self.vec[i].get_pozX()-x)+abs(self.vec[i].get_pozY()-y)

            i += 1
        if X==-1:
            return 0
        else:
            return self.pola[Y][X]

    def getNr_Tury(self):
        return self.nr_Tury

    def get_ilosc_org(self):
        return self.ilosc_org

    def set_ilosc_org(self, a):
        self.ilosc_org = a

    def bChangeColor(self, x, y, color, symbol):
        self.buttons[y][x].config(bg=color)

    def przeniesOrganizm(self, Xp, Yp, Xk, Yk):
        if self.pola[Yp][Xp] == None:
            #Console.WriteLine(Xp + " " + Yp + " " + Xk + " " + Yk)
            return
        c = self.pola[Yp][Xp].getColor()
        self.pola[Yk][Xk] = self.pola[Yp][Xp]
        self.pola[Yp][Xp] = None
        self.buttons[Yk][Xk].config(bg=c)
        self.buttons[Yp][Xp].config(bg="orange")

    def ulokujOrganizm(self, o):
        self.pola[o.get_pozY()][o.get_pozX()] = o
        o.rysowanie()

    def dodajOrganizm(self, o, s):
        self.vec.append(o)
        self.ulokujOrganizm(self.vec[self.ilosc_org])
        self.ilosc_org = self.ilosc_org + 1

    def dodajDoRaport(self, s):
        self.T.insert(END, s)

    def usunOrganizm(self, o):
        if o.getSymbol() != "C":
            self.dodajDoRaport("Zjedzono " + o.getSymbol() + "\n")
            self.vec.remove(o)
            self.buttons[o.get_pozY()][o.get_pozX()].config(bg="orange")
            self.pola[o.get_pozY()][o.get_pozX()] = None
            self.ilosc_org -= 1
        else:
            self.dodajDoRaport("Zjedzono Człowieka\n")
            self.dodajDoRaport("GAME OVER")
            print("GAME OVER")
            messagebox.showerror("","GAME OVER")
            exit()

    def zapisz(self):
        plik = open('D:\save.txt', 'w')
        i=0
        n = '%d\n' % (self.ilosc_org)
        plik.writelines(n)
        while i < self.ilosc_org:
            o1 = '%s\n' % (self.vec[i].getSymbol())
            o2 = '%d\n' % (self.vec[i].getSila())
            o3 = '%d\n' % (self.vec[i].get_pozX())
            o4 = '%d\n' % (self.vec[i].get_pozY())
            plik.writelines(o1)
            plik.writelines(o2)
            plik.writelines(o3)
            plik.writelines(o4)
            i = i + 1
        plik.close()
        self.dodajDoRaport("Zapisano Stan Gry\n")

    def wczytaj(self):
        i = 1
        while i < self.ilosc_org:
            if self.vec[i].getSymbol() != 'C':
                self.usunOrganizm(self.vec[i])
            else:
                i = i + 1
        self.T.delete(1.0, END)
        self.dodajDoRaport("Wczytano Zapis Gry\n")
        plik = open('D:\save.txt', 'r')
        try:
            i = 0
            n = int(linecache.getline('D:\save.txt', i + 1))
            while i < 4*n:
                symbol = linecache.getline('D:\save.txt', i + 2)
                ssila = linecache.getline('D:\save.txt', i + 3)
                sX = linecache.getline('D:\save.txt', i + 4)
                sY = linecache.getline('D:\save.txt', i + 5)
                sila = int(ssila)
                X = int(sX)
                Y = int(sY)
                if symbol == 'C\n':
                    self.vec[0].setSila(sila)
                    self.przeniesOrganizm(self.vec[0].get_pozX(),self.vec[0].get_pozY(),X,Y)
                    self.vec[0].set_pozX(X)
                    self.vec[0].set_pozY(Y)
                elif symbol == 'Antylope\n':
                    self.dodajOrganizm(Antylopa(X, Y, self), self)
                    self.vec[self.ilosc_org-1].setSila(sila)
                elif symbol == 'Barszcz\n':
                    self.dodajOrganizm(BarszczSosnowskiego(X, Y, self), self)
                elif symbol == 'Cyber_Owce\n':
                    self.dodajOrganizm(CyberOwca(X, Y, self), self)
                    self.vec[self.ilosc_org - 1].setSila(sila)
                elif symbol == 'Guarane\n':
                    self.dodajOrganizm(Guarana(X, Y, self), self)
                elif symbol == 'Lisa\n':
                    self.dodajOrganizm(Lis(X, Y, self), self)
                    self.vec[self.ilosc_org - 1].setSila(sila)
                elif symbol == 'Mlecza\n':
                    self.dodajOrganizm(Mlecz(X, Y, self), self)
                elif symbol == 'Owce\n':
                    self.dodajOrganizm(Owca(X, Y, self), self)
                    self.vec[self.ilosc_org - 1].setSila(sila)
                elif symbol == 'Trawe\n':
                    self.dodajOrganizm(Trawa(X, Y, self), self)
                elif symbol == 'Wilcze_Jagody\n':
                    self.dodajOrganizm(WilczeJagody(X, Y, self), self)
                    self.vec[self.ilosc_org - 1].setSila(sila)
                elif symbol == 'Wilka\n':
                    self.dodajOrganizm(Wilk(X, Y, self), self)
                    self.vec[self.ilosc_org - 1].setSila(sila)
                elif symbol == 'Zolwia\n':
                    self.dodajOrganizm(Zolw(X, Y, self), self)
                    self.vec[self.ilosc_org - 1].setSila(sila)
                i = i + 4
        finally:
            plik.close()

    def kier(self,event):
        if event.keysym == "Right":
            self.k_czlowieka = 2
            self.wykonajTure()
            self.k_czlowieka = 0
        elif  event.keysym == "Left":
            self.k_czlowieka = 4
            self.wykonajTure()
            self.k_czlowieka = 0
        elif event.keysym == "Up":
            self.k_czlowieka = 1
            self.wykonajTure()
            self.k_czlowieka = 0
        elif event.keysym == "Down":
            self.k_czlowieka = 3
            self.wykonajTure()
            self.k_czlowieka = 0
        elif event.keysym == "Escape":
            exit()
        elif event.keysym == "q":
            self.k_czlowieka = 5
            self.wykonajTure()
            self.k_czlowieka = 0
        elif event.keysym == "z":
            self.zapisz()
        elif event.keysym == "w":
            self.wczytaj()

    def printXY(self, event):
        pozX = ((event.x_root-110) // 20)
        pozY = ((event.y_root-130) // 20)
        if pozX<19 and pozY<19:
            print(pozX, pozY)
            if self.czyWolne(pozX,pozY):
                self.newX = pozX
                self.newY = pozY
                self.do_popup(event)

    def do_popup(self,event):
        # display the popup menu
        try:
            self.popup.tk_popup(550, 200, 0)
        finally:
            print("")

    def __init__(self):
        bNowaTura = Button(self.okno, command=self.wykonajTure,text="Nowa Tura",bg="cornflower blue")
        bNowaTura.place(x=480,y=380,width =100,height=50)
        for x in range(19):
            for y in range(19):
                self.buttons[y][x] = Button(self.okno, bg = "blue")
                self.buttons[y][x].place(x=20 + x * 20, y=20 + y * 20, width=20)
                self.buttons[y][x].config(bg="orange")

        self.popup.add_command(label="Antylopa",command=lambda: self.dodajOrganizm(Antylopa(self.newX, self.newY, self), self))
        self.popup.add_command(label="Barszcz",command=lambda: self.dodajOrganizm(BarszczSosnowskiego(self.newX, self.newY, self), self))
        self.popup.add_command(label="Cyber Owca",command=lambda: self.dodajOrganizm(CyberOwca(self.newX, self.newY, self), self))
        self.popup.add_command(label="Guarana",command=lambda: self.dodajOrganizm(Guarana(self.newX, self.newY, self), self))
        self.popup.add_command(label="Lis",command=lambda: self.dodajOrganizm(Lis(self.newX, self.newY, self), self))
        self.popup.add_command(label="Mlecz",command=lambda :self.dodajOrganizm(Mlecz(self.newX, self.newY, self), self))
        self.popup.add_command(label="Owca",command=lambda: self.dodajOrganizm(Owca(self.newX, self.newY, self), self))
        self.popup.add_command(label="Trawa",command=lambda: self.dodajOrganizm(Trawa(self.newX, self.newY, self), self))
        self.popup.add_command(label="W.Jagody",command=lambda: self.dodajOrganizm(WilczeJagody(self.newX, self.newY, self), self))
        self.popup.add_command(label="Wilk",command=lambda: self.dodajOrganizm(Wilk(self.newX, self.newY, self), self))
        self.popup.add_command(label="Żółw",command=lambda: self.dodajOrganizm(Zolw(self.newX, self.newY, self), self))

        self.dodajOrganizm(Czlowiek(6,6,self),self)
        self.dodajOrganizm(Antylopa(10,15,self),self)
        self.dodajOrganizm(Antylopa(1, 15, self), self)
        self.dodajOrganizm(BarszczSosnowskiego(8, 15, self), self)
        self.dodajOrganizm(BarszczSosnowskiego(10, 13, self), self)
        self.dodajOrganizm(CyberOwca(10, 6, self), self)
        self.dodajOrganizm(WilczeJagody(12, 4, self), self)
        self.dodajOrganizm(Trawa(15, 15, self), self)
        self.dodajOrganizm(Owca(13, 8, self), self)
        self.dodajOrganizm(Owca(16, 8, self), self)
        self.dodajOrganizm(Wilk(13, 7, self), self)
        self.dodajOrganizm(Wilk(1, 3, self), self)
        self.dodajOrganizm(Zolw(15, 11, self), self)
        self.dodajOrganizm(Zolw(16, 12, self), self)

        self.okno.bind("<Key>", self.kier)
        self.okno.bind("<Button-1>", self.printXY)
        self.okno.mainloop()