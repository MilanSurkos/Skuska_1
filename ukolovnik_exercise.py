# Task 9 - úkolovník
# Cílem úkolu je vytvořit poznámkový blok V poznámkovém bloku můžeme přidávat,
# odebírat nebo měnit řádky. Když spustíme program tak máme následující možnosti:
#
# Přidat poznámku (nakonec)
# Vypsat všechny poznámky
# Smazat poznámku (budeme vyzváni, jaký řádek smazat)
# Upravit poznámku (budeve vyzváni, jaký řádek a jak upravit)
# Uložit poznámky do souboru .csv (budeme vyzváni do jakého souboru)
# (Volitelně uložení i přes pickle)
# Načíst poznámky ze souboru .csv (budeme vyzváni z jakého souboru)
import csv

tasks_list = []


def pridat_task():
    task = input("Zadaj task: ")
    tasks_list.append(task)
    print(f"Task {task} bol pridany do zoznamu.")

def vypisat_task():
    if tasks_list:
        print("Tvoje tasky: ")
        for i, task in enumerate(tasks_list, start=1):
            print(f"{i}. {task}.")


def delete_task():
    vypisat_task()
    try:
        cislo = int(input("Zadajte číslo tasku na zmazanie: "))
        if 1 <= cislo <= len(tasks_list):
            zmazane = tasks_list.pop(cislo - 1)
            print(f"Task {zmazane} bol zmazany.")
        else:
            print("Nesprávne číslo.")
    except ValueError:
        print("Zadajte platné číslo")



def upravit_task():
    vypisat_task()
    try:
        cislo = int(input("Zadajte číslo tasku na upravenie: "))
        if 1 <= cislo <= len(tasks_list):
            novy_task = input("Zadaj nový task: ")
            tasks_list[cislo -1] = novy_task
            print(f"Task číslo {cislo} bol upravený na {novy_task}")
        else:
            print("Nesprávne číslo")
    except ValueError:
        print("Zadajte platné číslo")

def ulozit_task_do_csv():
    nazov_tasku = input("Zadaj názov súboru na uloženie: ")
    try:
        with open(nazov_tasku, "w", encoding="utf-8") as subor:
            writer = csv.writer(subor)
            for task in tasks_list:
                writer.writerow([task])
                print(f"Task list bol ulozený do súboru {nazov_tasku}")
    except Exception as e:
        print(f"Chyba pri ukladaní: {e}")

def nacitat_task_z_csv():
    nazov_tasku = input("Zadajte názov súboru na načítanie: ")
    try:
        with open(nazov_tasku, "r", encoding="utf-8") as subor:
            reader = csv.reader(subor)
            global tasks_list
            tasks_list = [riadok[0] for riadok in reader]
            print(f"Task list bol načítaný zo súboru {nazov_tasku}.")
    except Exception as e:
        print(f"Chyba pri načítaný: {e} ")




while True:
    print("\nWelcome to task-master")
    print("1. Pridat task")
    print("2. Vypísať všetky tasky")
    print("3. Delete task")
    print("4. Upraviť task")
    print("5. Ulozit task do súboru")
    print("6. Načítať task zo súboru")
    print("7. Exit")

    choice = input("Vyber moznosť: ")
    if choice == "1":
        pridat_task()
    elif choice == "2":
        vypisat_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        upravit_task()
    elif choice == "5":
        ulozit_task_do_csv()
    elif choice == "6":
        nacitat_task_z_csv()
    elif choice == "7":
        print("Ukoncujem program")
        break
    else:
        print("Zlý výber. Prosím vyber medzi 1-5")




