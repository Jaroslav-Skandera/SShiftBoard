# SShiftBoard – Text-based Staff Organizer
# Autor: Jaroslav Skandera | www.jskandera.tech

import os
import json
from datetime import datetime, timedelta

JSON_SOUBOR_BACKEND = "personal_backend.json"
JSON_SOUBOR_CLEANROOM = "personal_cleanroom.json"
JSON_SOUBOR_TELEFONY = "telefoni_seznam.json"
JSON_SOUBOR_TODO = "todo_list.json"
JSON_SOUBOR_HESLA = "hesla_stanice.json"

# ===== Načtení a uložení =====
def nacti_personal_backend():
    if os.path.exists(JSON_SOUBOR_BACKEND):
        with open(JSON_SOUBOR_BACKEND, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def uloz_personal_backend():
    with open(JSON_SOUBOR_BACKEND, "w", encoding="utf-8") as f:
        json.dump(personal_backend, f, indent=2, ensure_ascii=False)

def nacti_personal_cleanroom():
    if os.path.exists(JSON_SOUBOR_CLEANROOM):
        with open(JSON_SOUBOR_CLEANROOM, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def uloz_personal_cleanroom():
    with open(JSON_SOUBOR_CLEANROOM, "w", encoding="utf-8") as f:
        json.dump(personal_cleanroom, f, indent=2, ensure_ascii=False)

def nacti_telefoni_seznam():
    if os.path.exists(JSON_SOUBOR_TELEFONY):
        with open(JSON_SOUBOR_TELEFONY, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def uloz_telefoni_seznam():
    with open(JSON_SOUBOR_TELEFONY, "w", encoding="utf-8") as f:
        json.dump(telefoni_seznam_data, f, indent=2, ensure_ascii=False)

def nacti_todo():
    if os.path.exists(JSON_SOUBOR_TODO):
        with open(JSON_SOUBOR_TODO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def uloz_todo(seznam):
    with open(JSON_SOUBOR_TODO, "w", encoding="utf-8") as f:
        json.dump(seznam, f, indent=2, ensure_ascii=False)

def nacti_hesla():
    if os.path.exists(JSON_SOUBOR_HESLA):
        with open(JSON_SOUBOR_HESLA, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def uloz_hesla(seznam):
    with open(JSON_SOUBOR_HESLA, "w", encoding="utf-8") as f:
        json.dump(seznam, f, indent=2, ensure_ascii=False)


# ===== Načti seznamy po spuštění =====
personal_backend = nacti_personal_backend()
personal_cleanroom = nacti_personal_cleanroom()
telefoni_seznam_data = nacti_telefoni_seznam()
todo_list = nacti_todo()
hesla_stanice = nacti_hesla()

# ===== Pomocný slovník pro české názvy dnů =====
dny_cz = {
    "Monday": "Pondělí", "Tuesday": "Úterý", "Wednesday": "Středa",
    "Thursday": "Čtvrtek", "Friday": "Pátek", "Saturday": "Sobota", "Sunday": "Neděle"
}

# ===== Kalendář směn podle vzoru =====
def kalendar_smen():
    print("\n--- Směnový kalendář ---")
    dnes = datetime.now().date()
    start = datetime(2025, 6, 30).date()  # den nástupu do práce
    cyklus = ["R", "R", "V", "V", "N", "N", "N", "V", "V"]  # R=ranní, V=volno, N=noční
    posun = (dnes - start).days % len(cyklus)
    dnesni_smena = cyklus[posun]

    smena_text = {"R": "Ranní", "N": "Noční", "V": "Volno"}.get(dnesni_smena, dnesni_smena)
    den_en = dnes.strftime('%A')
    den_cz = dny_cz.get(den_en, den_en)
    print(f"Dnes je {den_cz} {dnes.strftime('%d.%m.%Y')} a máš směnu: {smena_text}")

    print("\nPlán směn na 14 dní:")
    print("Datum       | Den          | Směna")
    print("--------------------------------------")
    for i in range(14):
        datum = dnes + timedelta(days=i)
        smena_kod = cyklus[(posun + i) % len(cyklus)]
        smena_txt = {"R": "Ranní", "N": "Noční", "V": "Volno"}.get(smena_kod, smena_kod)
        den_cz_i = dny_cz.get(datum.strftime('%A'), datum.strftime('%A'))
        print(f"{datum.strftime('%d.%m.%Y')} | {den_cz_i:<12} | {smena_txt}")

# ===== Hlavní menu =====
def hlavni_menu():
    while True:
        print("\n==============================")
        print("     📂️  SShiftBoard Menu")
        print("==============================")
        print("1. Personal (BE / ČP)")
        print("2. Telefonní kontakty")
        print("3. ToDo / Úkoly")
        print("4. Hesla")
        print("5. Kalendář směn")
        print("0. Konec")
        print("==============================")

        try:
            volba = int(input("Zadej volbu: "))
        except ValueError:
            print("Zadej platné číslo.")
            continue

        if volba == 1:
            personal_menu()
        elif volba == 2:
            telefoni_seznam()
        elif volba == 3:
            todo_menu()
        elif volba == 4:
            hesla_menu()
        elif volba == 5:
            kalendar_smen()
        elif volba == 0:
            print("Ukončuji aplikaci...")
            break
        else:
            print("Neplatná volba, zkus to znovu.")


def personal_menu():
    while True:
        print("\n==============================")
        print("     🧑‍🤝‍🧑  Personal Menu")
        print("==============================")
        print("1. Backend")
        print("2. Clean Room")
        print("3. Zpět na hlavní menu")

        try:
            volba = int(input("Zadej volbu: "))
        except ValueError:
            print("Zadej platné číslo.")
            continue

        if volba == 1:
            backend()
        elif volba == 2:
            clean_room()
        elif volba == 3:
            break
        else:
            print("Neplatná volba.")

def backend():    # Backend → Personal Menu
    while True:
        print("\n==============================")
        print("     📂️  Backend Menu")
        print("==============================")
        print("1. Zobrazit Personal")
        print("2. Vyhledat Personal")
        print("3. Přidat Personal")
        print("4. Vymazat Personal")
        print("5. Zpět")
        try:
            backend_personal = int(input("Zadej volbu: "))
        except ValueError:
            print("Zadej platné číslo.")
            continue
        if backend_personal == 1:
            zobrazit_personal(personal_backend)
        elif backend_personal == 2:
            vyhledat_personal(personal_backend)
        elif backend_personal == 3:
            pridat_personal(personal_backend, uloz_personal_backend)
        elif backend_personal == 4:
            vymazat_personal(personal_backend, uloz_personal_backend)
        elif backend_personal == 5:
            break
        else:
            print("Tato volba zatím není dostupná.")


def clean_room():    # Clean Room → Personal Menu
    while True:
        print("\n==============================")
        print("     📂️  Clean Room Menu")
        print("==============================")
        print("1. Zobrazit Personal")
        print("2. Vyhledat Personal")
        print("3. Přidat Personal")
        print("4. Vymazat Personal")
        print("5. Zpět")
        try:
            cleanroom_personal = int(input("Zadej volbu: "))
        except ValueError:
            print("Zadej platné číslo.")
            continue
        if cleanroom_personal == 1:
            zobrazit_personal(personal_cleanroom)
        elif cleanroom_personal == 2:
            vyhledat_personal(personal_cleanroom)
        elif cleanroom_personal == 3:
            pridat_personal(personal_cleanroom, uloz_personal_cleanroom)
        elif cleanroom_personal == 4:
            vymazat_personal(personal_cleanroom, uloz_personal_cleanroom)
        elif cleanroom_personal == 5:
            break
        else:
            print("Tato volba zatím není dostupná.")

def zobrazit_personal(seznam):
    print("\n--- Seznam zaměstnanců ---")
    if not seznam:
        print("Seznam je prázdný.")
    else:
        print(f"{'ID':<12} | {'Jméno':<15} | {'Příjmení':<20} | {'Pozice':<25}")
        print("-" * 75)
        for osoba in seznam:
            print(f"{osoba['id']:<12} | {osoba['jmeno']:<15} | {osoba['prijmeni']:<20} | {osoba['pozice']:<25}")

def pridat_personal(seznam, uloz_funkce):
    print("\n--- Přidat nového zaměstnance ---")
    id = input("Zadej osobní číslo: ")
    jmeno = input("Zadej jméno: ")
    prijmeni = input("Zadej příjmení: ")
    pozice = input("Zadej pozici: ")

    if not id or not jmeno or not prijmeni or not pozice:
        print("Všechna pole jsou povinná.")
        return

    seznam.append({"id": id, "jmeno": jmeno, "prijmeni": prijmeni, "pozice": pozice})
    uloz_funkce()
    print("Zaměstnanec byl ússpěšně přidán.")

def vyhledat_personal(seznam):
    hledani = input("Zadej příjmení nebo osobní číslo: ").strip().lower()
    nalezeno = False

    for osoba in seznam:
        if (hledani in osoba['prijmeni'].lower()) or (hledani == osoba['id'].lower()):
            if not nalezeno:
                print(f"\n{'ID':<12} | {'Jméno':<15} | {'Příjmení':<20} | {'Pozice':<25}")
                print("-" * 75)
                nalezeno = True
            print(f"{osoba['id']:<12} | {osoba['jmeno']:<15} | {osoba['prijmeni']:<20} | {osoba['pozice']:<25}")

    if not nalezeno:
        print("Nenalezen žádný záznam.")

def vymazat_personal(seznam, uloz_funkce):
    hledani = input("Zadej příjmení nebo osobní číslo ke smazání: ").strip().lower()
    kandidati = []

    for i, osoba in enumerate(seznam):
        if hledani in osoba['prijmeni'].lower() or hledani == osoba['id'].lower():
            kandidati.append((i, osoba))

    if not kandidati:
        print("Nebyly nalezeny žádné odpovídající záznamy.")
        return

    print(f"\n{'#':<3} | {'ID':<12} | {'Jméno':<15} | {'Příjmení':<20} | {'Pozice':<25}")
    print("-" * 85)
    for idx, (i, osoba) in enumerate(kandidati):
        print(f"{idx + 1:<3} | {osoba['id']:<12} | {osoba['jmeno']:<15} | {osoba['prijmeni']:<20} | {osoba['pozice']:<25}")

    try:
        volba = int(input("Zadej číslo záznamu ke smazání: "))
        if 1 <= volba <= len(kandidati):
            index_ke_smazani, osoba = kandidati[volba - 1]
            potvrzeni = input(f"Opravdu chceš smazat: {osoba['id']} | {osoba['jmeno']} {osoba['prijmeni']}? (a/n): ").strip().lower()
            if potvrzeni == "a":
                del seznam[index_ke_smazani]
                uloz_funkce()
                print("Záznam byl smazán.")
            else:
                print("Smazání zrušeno.")
        else:
            print("Neplatné číslo.")
    except ValueError:
        print("Neplatný vstup.")

# ===== Telefonní seznam =====
def telefoni_seznam():
    while True:
        print("\n==============================")
        print("     ☎️ Telefonní seznam")
        print("==============================")
        print("1. Zobrazit kontakty")
        print("2. Přidat kontakt")
        print("3. Smazat kontakt")
        print("4. Zpět")

        try:
            volba = int(input("Zadej volbu: "))
        except ValueError:
            print("Zadej platné číslo.")
            continue

        if volba == 1:
            if not telefoni_seznam_data:
                print("Seznam je prázdný.")

            else:
                print("\n--- Telefonní seznam ---")
                print(f"{'Jméno a přijmení':<15} | {'Telefon':<15} | {'Poznámka':<25}")
                print("-" * 60)
                for kontakt in telefoni_seznam_data:
                    print(f"{kontakt['jmeno']:<15} | {kontakt['cislo']:<15} | {kontakt.get('poznamka', ''):<25}")


        elif volba == 2:
            jmeno = input("Zadej jméno a přijmení: ")
            cislo = input("Zadej telefonní číslo: ")
            poznamka = input("Poznámka (volitelná): ")

            if not jmeno or not cislo:
                print("Jméno a číslo jsou povinná.")
            else:
                telefoni_seznam_data.append({"jmeno": jmeno, "cislo": cislo, "poznamka": poznamka})
                uloz_telefoni_seznam()
                print("Kontakt přidán.")

        elif volba == 3:
            hledani = input("Zadej jméno nebo číslo pro smazání: ").strip().lower()
            kandidati = [(i, k) for i, k in enumerate(telefoni_seznam_data) if hledani in k['jmeno'].lower() or hledani in k['cislo']]

            if not kandidati:
                print("Nenalezen žádný kontakt.")
            else:
                print("\n# | Jméno            | Telefon         | Poznámka")
                print("-" * 60)
                for idx, (i, k) in enumerate(kandidati):
                    print(f"{idx + 1:<2} | {k['jmeno']:<15} | {k['cislo']:<15} | {k.get('poznamka', ''):<25}")

                try:
                    volba_smaz = int(input("Zadej číslo kontaktu ke smazání: "))
                    if 1 <= volba_smaz <= len(kandidati):
                        index, kontakt = kandidati[volba_smaz - 1]
                        potvrzeni = input(f"Opravdu smazat {kontakt['jmeno']} ({kontakt['cislo']})? (a/n): ").strip().lower()
                        if potvrzeni == 'a':
                            del telefoni_seznam_data[index]
                            uloz_telefoni_seznam()
                            print("Kontakt smazán.")
                        else:
                            print("Smazání zrušeno.")
                    else:
                        print("Neplatná volba.")
                except ValueError:
                    print("Zadej platné číslo.")

        elif volba == 4:
            break
        else:
            print("Neplatná volba.")

def todo_menu():
    todo_list = nacti_todo()

    while True:
        print("\n==============================")
        print("     ✅ ToDo Úkoly")
        print("==============================")
        print("1. Zobrazit úkoly")
        print("2. Přidat úkol")
        print("3. Odebrat úkol")
        print("4. Zpět")

        try:
            volba = int(input("Zadej volbu: "))
        except ValueError:
            print("Zadej platné číslo.")
            continue

        if volba == 1:
            if not todo_list:
                print("Žádné úkoly.")
            else:
                print("\n--- Seznam úkolů ---")
                for i, ukol in enumerate(todo_list, start=1):
                    print(f"{i}. {ukol}")

        elif volba == 2:
            novy_ukol = input("Zadej nový úkol: ")
            if novy_ukol:
                todo_list.append(novy_ukol)
                uloz_todo(todo_list)
                print("Úkol přidán.")

        elif volba == 3:
            if not todo_list:
                print("Seznam je prázdný.")
                continue
            print("\n--- Seznam úkolů ---")
            for i, ukol in enumerate(todo_list, start=1):
                print(f"{i}. {ukol}")
            try:
                volba_smaz = int(input("Zadej číslo úkolu ke smazání: "))
                if 1 <= volba_smaz <= len(todo_list):
                    odebrany = todo_list.pop(volba_smaz - 1)
                    uloz_todo(todo_list)
                    print(f"Úkol \"{odebrany}\" byl smazán.")
                else:
                    print("Neplatné číslo.")
            except ValueError:
                print("Zadej platné číslo.")

        elif volba == 4:
            break
        else:
            print("Neplatná volba.")

# ===== Seznam hesel =====
def hesla_menu():
    while True:
        print("\n==============================")
        print("     🔐 Hesla od stanic")
        print("==============================")
        print("1. Zobrazit hesla")
        print("2. Přidat záznam")
        print("3. Odebrat záznam")
        print("4. Zpět")

        try:
            volba = int(input("Zadej volbu: "))
        except ValueError:
            print("Zadej platné číslo.")
            continue

        if volba == 1:
            if not hesla_stanice:
                print("Žádné záznamy.")
            else:
                print(f"\n{'Stanice':<20} | {'Login':<20} | {'Heslo':<20}")
                print("-" * 65)
                for zaznam in hesla_stanice:
                    print(f"{zaznam['stanice']:<20} | {zaznam['login']:<20} | {zaznam['heslo']:<20}")

        elif volba == 2:
            stanice = input("Název stanice: ")
            login = input("Login: ")
            heslo = input("Heslo: ")
            if stanice and login and heslo:
                hesla_stanice.append({"stanice": stanice, "login": login, "heslo": heslo})
                uloz_hesla(hesla_stanice)
                print("Záznam přidán.")

        elif volba == 3:
            if not hesla_stanice:
                print("Seznam je prázdný.")
                continue
            for i, zaznam in enumerate(hesla_stanice, start=1):
                print(f"{i}. {zaznam['stanice']} ({zaznam['login']})")
            try:
                volba_smaz = int(input("Zadej číslo záznamu ke smazání: "))
                if 1 <= volba_smaz <= len(hesla_stanice):
                    odebrany = hesla_stanice.pop(volba_smaz - 1)
                    uloz_hesla(hesla_stanice)
                    print(f"Záznam pro stanici \"{odebrany['stanice']}\" byl smazán.")
                else:
                    print("Neplatné číslo.")
            except ValueError:
                print("Zadej platné číslo.")

        elif volba == 4:
            break
        else:
            print("Neplatná volba.")

# ===== Spuštění programu =====
hlavni_menu()

