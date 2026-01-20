import requests
import csv
import io
from datetime import datetime
import time


URL = "https://danepubliczne.imgw.pl/api/data/synop/format/csv"


def pobierz_dane():
    odpowiedz = requests.get(URL, timeout=10)
    odpowiedz.raise_for_status()

    plik_csv = io.StringIO(odpowiedz.text)
    czytnik = csv.DictReader(plik_csv)

    return list(czytnik)


def wyswietl_stacje(dane):
    stacje = {}

    for rekord in dane:
        stacje[rekord["id_stacji"]] = rekord["stacja"]

    print("\nLista stacji synoptycznych:\n")
    for identyfikator, nazwa in sorted(stacje.items()):
        print(f"{identyfikator}: {nazwa}")

    return stacje


def wybierz_stacje(stacje):
    while True:
        wybrane = input("\nPodaj ID stacji: ").strip()

        if wybrane in stacje:
            print(f"\nWybrana stacja: {stacje[wybrane]} (ID {wybrane})")
            return wybrane
        else:
            print("Błędny identyfikator — spróbuj ponownie.")

from datetime import datetime


def pobierz_czas_koncowy():
    while True:
        tekst = input("\nPodaj datę i godzinę końcową (format: DD-MM-YYYY HH:MM): ")

        try:
            czas_koncowy = datetime.strptime(tekst, "%d-%m-%Y %H:%M")
            if czas_koncowy <= datetime.now():
                print("Podaj datę i godzinę z PRZYSZŁOŚCI.")
            else:
                return czas_koncowy

        except ValueError:
            print("Błędny format! Poprawny format to: YYYY-MM-DD HH")

def zbieraj_dane_do_czasu(id_stacji, czas_koncowy):
    temperatury = []
    zapisane_czasy = set()
    print("\nRozpoczynam zbieranie danych...\n")
    while datetime.now() < czas_koncowy:

        try:
            odpowiedz = requests.get(URL, timeout=10)
            odpowiedz.raise_for_status()

            plik_csv = io.StringIO(odpowiedz.text)
            czytnik = csv.DictReader(plik_csv)
            nowe_dane = False

            for rekord in czytnik:
                if rekord["id_stacji"] == id_stacji:
                    znacznik = f"{rekord['data_pomiaru']} {rekord['godzina_pomiaru']}"
                    if znacznik not in zapisane_czasy:
                        temperatura = rekord["temperatura"]

                        if temperatura not in (None, "", " "):
                            zapisane_czasy.add(znacznik)
                            temperatury.append(float(temperatura))

                            print(f"Nowy pomiar: {znacznik} → {temperatura}°C")
                            nowe_dane = True
            if not nowe_dane:
                print("Brak nowych danych — czekam 5 minut...\n")
                time.sleep(300)  
        except Exception as e:
            print("Błąd pobierania danych:", e)
            print("Ponawiam za 5 minut...\n")
            time.sleep(300)

    print("\nZbieranie zakończone — osiągnięto czas końcowy.\n")
    return temperatury, zapisane_czasy

def zapisz_wynik_csv(nazwa_stacji, id_stacji, temperatury, czasy):
    if temperatury:
        srednia = sum(temperatury) / len(temperatury)
    else:
        srednia = None

    with open("wynik.csv", "w", newline="", encoding="utf-8") as plik:
        writer = csv.writer(plik)

        writer.writerow([
            "stacja", "id_stacji", "czas_od", "czas_do",
            "liczba_pomiarow", "srednia_temperatura"
        ])

        writer.writerow([
            nazwa_stacji,
            id_stacji,
            min(czasy),
            max(czasy),
            len(temperatury),
            f"{srednia:.2f}" if srednia is not None else "brak danych"
        ])

    print("\nPlik wynik.csv został utworzony i zapisany.")


dane = pobierz_dane()
stacje = wyswietl_stacje(dane)
wybrana = wybierz_stacje(stacje)
czas_koncowy = pobierz_czas_koncowy()
print(f"\nProgram będzie działał do: {czas_koncowy}")
temperatury, czasy = zbieraj_dane_do_czasu(wybrana, czas_koncowy)
print("\nZakończono połączenie z serwisem IMGW.")
print("Wynik zapisano do pliku.")