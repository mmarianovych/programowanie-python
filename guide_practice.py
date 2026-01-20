import csv
import os
import numpy as np
moj_folder = "C:/Users/341354/Documents/programowanie/programowanie-python/pogoda/"

def lista_plikow(folder):
    lista = os.listdir(folder)
    return lista

def czytaj_plik_meteo(sciezka):
    lista= []
    with open(sciezka, 'r', encoding="utf8") as plikcsv:
        csvreader = csv.reader(plikcsv)
        next(csvreader)
        for wiersz in csvreader:
            lista.append(wiersz)
    tablica  = np.array(lista)
    return tablica

def oblic_min_temp(moja_tablica):
    temperatura =[]
    for i in range(0,len(moja_tablica[:,4])):
        temperatura.append(float(moja_tablica[i,4]))
    temperatura = np.array(temperatura)
    min_temp = min(temperatura)
    return min_temp


##########################################
moj_folder = "C:/Users/341354/Documents/programowanie/programowanie-python/pogoda/"
lista = lista_plikow(moj_folder)
wekor_min_temp = []

for plik in lista:
    nazwa = moj_folder + plik
    tablica = czytaj_plik_meteo (nazwa)
    tablica_danych = czytaj_plik_meteo(nazwa)
    minimalna_temperatura = oblic_min_temp (tablica_danych)
    wekor_min_temp.append(minimalna_temperatura)

print (wekor_min_temp)










lista_plikow = os.listdir(moj_folder)
print(lista_plikow)
lista= []
for plik in lista_plikow:
    nazwa = moj_folder + plik 
    print(nazwa)
    with open(nazwa, 'r', encoding="utf8") as plikcsv:
        csvreader = csv.reader(plikcsv)
        next(csvreader)

        for wiersz in csvreader:
            lista.append(wiersz)

print(lista)
tablica=np.array(lista)
print(tablica)

temperatura =[]
opad = []

for i in range(0,len(tablica[:,4])):
    temperatura.append(float(tablica[i,4]))
    opad.append(float(tablica[i,8]))
temperatura = np.array(temperatura)
opad = np.array(opad)
print(temperatura)
print(opad)

minimalna_temperatura = min(temperatura)
maksymalna_temperatura = max(temperatura)
print(minimalna_temperatura)
print(maksymalna_temperatura)

indeks_temperatura_minimalna = np.where(temperatura==minimalna_temperatura)
indeks_temperatura_maksymalna = np.where(temperatura==maksymalna_temperatura)
print(indeks_temperatura_minimalna)

godzina_min_temp = tablica[indeks_temperatura_minimalna,3]
data_min_temp = tablica [indeks_temperatura_minimalna,2]
lockalizacja_min_temp = tablica [indeks_temperatura_minimalna,1]

godzina_max_temp = tablica[indeks_temperatura_maksymalna,3]
data_max_temp = tablica [indeks_temperatura_maksymalna,2]
lockalizacja_max_temp = tablica [indeks_temperatura_maksymalna,1]

napis_temp_min = "Temperature minimalna wynoszaca" + str(minimalna_temperatura) + "st. C zanotowano na stacji "  + str(lockalizacja_min_temp[0][0]) + "dnia" + str(data_min_temp[0][0])+ "o godzinie" +str(godzina_min_temp)
print(napis_temp_min)

napis_temp_max = "Temperature maksymalna wynoszaca" + str(maksymalna_temperatura) + "st. C zanotowano na stacji "  + str(lockalizacja_max_temp[0][0]) + "dnia" + str(data_max_temp[0][0])+ "o godzinie" +str(godzina_max_temp)
print(napis_temp_max)

niezerowy_opad_index = np.where(opad>0)
godzina_niezerowy_opad = tablica[niezerowy_opad_index,3]
data_niezerowy_opad = tablica [niezerowy_opad_index,2]
lockalizacja_niezerowy_opad = tablica [niezerowy_opad_index,1]

print(lockalizacja_niezerowy_opad[0])
for j in range(0,len(lockalizacja_niezerowy_opad[0])):
    print("Opad wystąpil na stacji "  + str(lockalizacja_niezerowy_opad[0][j]) + "dnia" + str(data_niezerowy_opad[0][j])+ "o godzinie" +str(godzina_niezerowy_opad[0][j])+".")


