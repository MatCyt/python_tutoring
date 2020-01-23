class Samochod:

    # czy trzeba je tu wszystkie wypisywać? kiedy tak? one sa obowiazkowe? jak mozna podac nie obowiazkowe?
    def __init__(self, max_predkosc, spalanie, obecna_predkosc = 0, pokonany_dystans = 0, czas_podrozy = 0):
        self.max_predkosc = max_predkosc
        self.spalanie = spalanie
        self.obecna_predkosc = obecna_predkosc
        self.pokonany_dystans = pokonany_dystans
        self.czas_podrozy = czas_podrozy

    def przyspiesz(self, wieksza_predkosc):
        self.obecna_predkosc += wieksza_predkosc

    def zwolnij(self, mniejsza_predkosc):
        nowa_predkosc = self.obecna_predkosc - mniejsza_predkosc
        self.obecna_predkosc = max(0, nowa_predkosc)

    def hamuj(self):
        self.obecna_predkosc = 0

    def turbo(self):
        self.obecna_predkosc = self.max_predkosc

    def jedz(self, nowy_dystans):
        self.pokonany_dystans += nowy_dystans
        dodatkowy_czas = nowy_dystans / self.obecna_predkosc
        self.czas_podrozy += dodatkowy_czas

    def podroz(self):
        benzyna = self.pokonany_dystans / self.spalanie
        print('Samochod przejechal {}, co zajelo {} godziny, i spalilo {}l benzyny'.format(self.pokonany_dystans, self.czas_podrozy, benzyna))



samochod = Samochod(200, 10) 

samochod.przyspiesz(100) # samochód jedzie 100km/h
print(samochod.obecna_predkosc)

samochod.jedz(100) # dystans = 100km, czas = 1h
print(samochod.pokonany_dystans)
print(samochod.czas_podrozy)

samochod.turbo() # prędkość = 200km/h
print(samochod.obecna_predkosc)

samochod.jedz(100) # dystans = 100 + 100km, czas = 1 + 0.5h
print(samochod.pokonany_dystans)
print(samochod.czas_podrozy)

samochod.podroz()
    
