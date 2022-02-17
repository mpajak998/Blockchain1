# blockchain

import json
import os
import hashlib
import time



hash256 = hashlib.sha256()


Projekt_dir = 'Bloki/'

#Funkcja haszująca
#RB odczyt binarny
def hash(poprzedni_blok):
    with open(Projekt_dir + poprzedni_blok, 'b+r') as p:
        content = p.read()
        #Algorytm kryptograficzny MD5
        
    return hashlib.sha256(content).hexdigest()




    
   





    

#Sprawdzenie inegralności - porównanie z każdym poprzednim blokiem
#Key-Sprawdzenie tylko liczby całkowite
def sprawdz_integralnosc():
    pliki = sorted(os.listdir(Projekt_dir), key=lambda x: int (x))

    wyniki = []

    for pliki in pliki[1:]:
        with open(Projekt_dir + pliki) as p:
            blok = json.load(p)
            #Hash ostatniego bloku
        poprzedni_hash = blok.get ('poprzedni_blok').get('hash')
        poprzedni_nr_bloku = blok.get ('poprzedni_blok').get('numer_bloku')

        #porównanie hasha z poprzedniego bloku-inaczej Blockchain nie będzie integralny!
        aktualny_hash = hash(poprzedni_nr_bloku)

        if poprzedni_hash == aktualny_hash:
            kom = 'Hash jest poprawny'
        else:
            kom = 'Hash się zmienił'
        
        #Wrzucenie do Tablicy wyników
        print(f'Blok {poprzedni_nr_bloku}: {kom}')
        wyniki.append({'blok': poprzedni_nr_bloku, 'wyniki': kom})
    return wyniki
    
#Tworzenie kolejnych bloków
def tworz_blok(Od_kogo,Do_kogo,Ilosc):
    
    licznik_blokow = len(os.listdir(Projekt_dir))
    poprzedni_blok = str(licznik_blokow)

    dane =      {
        "Od_kogo": Od_kogo,
        "Do_kogo": Do_kogo,
        "Ilosc": Ilosc,

        "poprzedni_blok": {
            "hash": hash(poprzedni_blok),
            "numer_bloku": poprzedni_blok
            }
                }

#Zwraca obecny blok
    obecny_blok = Projekt_dir + str(licznik_blokow + 1)

#Zapis kolejnych bloków do pliku json
    with open(obecny_blok , 'w') as p:
        #pobranie danych które zapiszemy
        json.dump(dane, p , indent=4, ensure_ascii=False)
        p.write('\n')


#głowna funkcja
def main():
    #tworz_blok(Od_kogo='Osoba1',Do_kogo='Osoba2',ilosc=100)
    sprawdz_integralnosc()

#Punkt wejścia do skryptu
if __name__=='__main__':
    main()










