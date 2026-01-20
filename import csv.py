import csv 
plik = "meteo1.csv"
import numpy as np


lista = []
with open(plik,'r') as plikcsv:
     
     csvreader = csv.reader(plikcsv)
     naglowek = next(csvreader)
     print(naglowek)

     for wiersz in csvreader:
         lista.append(wiersz)
print(lista)

tablica = np.array(lista)
print (naglowek)
print(tablica)

suma_temperatur = 0
for i in range(0,5):
     temperatura = float(tablica[i][4])

     print(temperatura)
     suma_temperatur = suma_temperatur + temperatura
     print(suma_temperatur)

liczba_elementow = len(tablica)
srednia_temperatura = suma_temperatur/liczba_elementow
print(srednia_temperatura)

suma_wilgotnosc = 0
for i in range(0,5):
     wilgotnosc = float(tablica[i][-3])

     print(wilgotnosc)
     suma_wilgotnosc = suma_wilgotnosc + wilgotnosc
     print(suma_wilgotnosc)

liczba_elementow = len(tablica)
srednia_wilgotnosc = suma_wilgotnosc/liczba_elementow
print(srednia_wilgotnosc)
