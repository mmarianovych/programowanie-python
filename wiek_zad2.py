wiek_1 = input("Wiek pierwszego studenta")
with open ('wiek_drugiego_studenta.txt','r') as plik:
    wiek_2 = plik.read() 
wiek_1=int(wiek_1)
wiek_2=int(wiek_2)
if wiek_2>wiek_1:
    roznica= wiek_2 - wiek_1
    tekst = "Student pierwszy jest mlodszy od studenta drugiego o " +str(roznica) + "lat(a)."
    print(tekst)
with open("wiek2_na_zajeciach.txt",'a') as plik_wyjsciowy:
    plik_wyjsciowy.write(tekst)