wiek_1 = input("Wiek pierwszego studenta")
wiek_2 = input("Wiek drugiego studenta studenta")

wiek_1=int(wiek_1)
wiek_2=int(wiek_2)
if wiek_1>wiek_2:
    tekst="Pierwszy student jest starszy i ma"+str(wiek_1)+"lat"
with open('wiek.txt','a') as plik:
    plik.write(tekst)



