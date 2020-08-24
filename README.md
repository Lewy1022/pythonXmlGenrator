# RecordGenerator
> Jest to prosty skrypt generujacy dane do bazy danych

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)


## General info
Skrypt jest generatorem danych mającym symulować działanie aplikacji.
Zadaniem generatora jest wygenerowanie w dowolnym momencie dużej liczby wierszy. Generator
działa przyrostowo (kolejne uruchomienie dodaje kolejne wiersze). Skrypt jest przygotowany jago zadanie na studia z przedmiotu aplikacje bazodonowe.
![Baza danych](./img/sc1.png)



## Technologies
* Python 3.8
* cx_oracle


## Setup
1. Należy otworzyć wiersz poleceń i należy zmienić ściężkę do folderu wkórym znajduje się generator.
2. Następnie należy wywołąć komendę w wierszu poleceń:'python generator.py <argument1> <argument2>' gdzie:
   - argument1 - jest to nazwa tabeli do, której chemy generowaćinserty. Dostępne wartości:
     - klient
     - trener
     - kontakty
     - cennik
     - cwiczenia
     - plan_treningu
     - Plan_cwiczen
     - Rejestr_wejsc_wyjsc
     - Adresy
   - argument2 - jest to ilość insertów, które chcemy wygenerować
   Przykład użycia:'python generator.py cwiczenia 100'
3. inserty zapisywane są w pliku inserty.txt, który znajduje się w folderze generatora.




## Status
Project is:  _no longer continue_ 

