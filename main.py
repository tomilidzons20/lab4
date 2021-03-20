from random import *

# Zad1
# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.

plik = open("zad1.txt", "w+")

lista1 = []
while len(lista1) != 5:
    x = randint(1, 100)
    if x % 4 == 0:
        lista1.append(x)
plik.writelines(str(lista1))
plik.close()

# Zad2
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość

print("Zad2")

plik = open("zad1.txt", "r+")
odczyt = plik.readline()
plik.close()
print(odczyt)

# Zad3
# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.

print("Zad3")

with open("zad3.txt", "w") as plik:
    for z in range(4):
        plik.write("To jest linia %d\n" % (z+1))

with open("zad3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")

# Zad4
# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# nazwa_produktu, ilosc, jednostka_miary, cena_jed
# oraz metody:
# konstruktor – który nadaje wartości
# wyświetl_produkt() – drukuje informacje o produkcie na ekranie
# ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# ile_kosztuje() – oblicza ile kosztuje dana ilość produktu
# np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2

print("Zad4")


class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        return ("Nazwa produktu", self.nazwa_produktu, "Ilosc produktow", self.ilosc,
                "Jednostka miary", self.jednostka_miary, "Cena jednostkowa", self.cena_jed)

    def ile_produktu(self):
        return "Ilosc produktu", str(self.ilosc) + " " + self.jednostka_miary

    def ile_kosztuje(self):
        return "Calosc kosztuje", self.ilosc * self.cena_jed


produkt = NaZakupy("Pizza pepperoni", 8, "Sztuk", 15)
print(produkt.wyswietl_produkt())
print(produkt.ile_produktu())
print(produkt.ile_kosztuje())

# Zad5
# Utwórz klasę, która definiuje ciągi arytmetyczne.
# Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
# - wyświetl_dane – drukuje elementy na ekran
# - pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# - pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# - policz_sume – liczy sume elementow
# - policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

print("Zad5")


class ciagAryt:
    wyniki = []
    a1 = 0
    r = 0
    n = 0

    def wyswietl_dane(self):
        return self.wyniki

    def pobierz_paramerty(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n

    def policz_sume(self):
        an = self.a1 + (self.n - 1) * self.r
        sn = (self.a1 + an) / 2 * self.n
        self.wyniki.extend(["Sn = %f" % sn])

    def policz_elementy(self):
        if self.r != 0 and self.a1 != 0:
            for i in range(1, self.n + 1):
                self.wyniki.extend(["a%d = %g" % (i, (self.a1 + (i - 1) * self.r))])


ciag1 = ciagAryt()
ciag1.pobierz_paramerty(2, 3, 5)
ciag1.policz_sume()
ciag1.policz_elementy()
print(ciag1.wyswietl_dane())

# Zad6
# Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka. Klasa powinna przechowywać współrzędne x, y,
#   krok (stała wartość kroku dla Robaczka), i powinna mieć następujące metody:
# konstruktor – który nadaje wartość dla x, y i krok
# idz_w_gore(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku
#   i ustawia nowe wartości współrzędnych x i y
# idz_w_dol(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku
#   i ustawia nowe wartości współrzędnych x i y
# idz_w_lewo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku
#   i ustawia nowe wartości współrzędnych x i y
# idz_w_prawo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku
#   i ustawia nowe wartości współrzędnych x i y
# pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne Robaczka
# Stwórz instancję klasy i sprawdź jak działają wszystkie metody

print("Zad6")


class robaczek:
    def __init__(self, wx, wy, krok):
        self.wx = wx
        self.wy = wy
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.wy += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.wy -= ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.wx -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.wx += ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        return self.wx, self.wy


robak1 = robaczek(2, 5, 2)
print(robak1.pokaz_gdzie_jestes())
robak1.idz_w_lewo(3)
robak1.idz_w_gore(4)
robak1.idz_w_prawo(5)
robak1.idz_w_dol(2)
print(robak1.pokaz_gdzie_jestes())
