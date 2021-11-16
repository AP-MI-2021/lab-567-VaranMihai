from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, stergere_rezervare, modifica_rezervare
from Logic.functionalitati import trecere_la_alta_clasa, ieftinire_pret, pret_maxim_pentru_clase, \
    ordonare_desc_dupa_pret, suma_pret_pentru_nume


def print_menu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea la clasa superioara")
    print("5. Ieftinire rezervari")
    print("6. Determinarea pretului maxim pentru fiecare clasa")
    print("7. Ordonare rezervarilor descrescator dupa pret")
    print("8. Afisarea sumelor preturilor dupa nume")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare rezervari")
    print("x. Iesire")


def ui_adaugare_rezervare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        chekin = input("Dati chekin: ")

        rezultat = adauga_rezervare(id, nume, clasa, pret, chekin, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_stergere_rezervare(lista, undo_list, redo_list):
    try:
        id = input("dati id-ul rezervarii de sters: ")
        rezultat = stergere_rezervare(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modificare_rezervare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        chekin = input("Dati chekin: ")

        rezultat = modifica_rezervare(id, nume, clasa, pret, chekin, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def ui_trecerea_la_clasa_superioara(lista):
    try:
        string_nume = input("Dati numele rezervariilor: ")
        return trecere_la_alta_clasa(string_nume, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_ieftinire_rezervari(lista):
    try:
        procentaj = int(input("Dati un procentaj de ieftinire: "))
        return ieftinire_pret(procentaj, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_pret_maxim_pentru_clase(lista):
    rezultat = pret_maxim_pentru_clase(lista)
    for clasa in rezultat:
        print("Clasa {} are pretul maxim {}".format(clasa, rezultat[clasa]))


def ui_ordonare_desc_dupa_pret(lista):
    show_all(ordonare_desc_dupa_pret(lista))


def ui_suma_pret_pentru_nume(lista):
    rezultat = suma_pret_pentru_nume(lista)
    for nume in rezultat:
        print("Numele {} are suma preturilor {}".format(nume, rezultat[nume]))


def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = ui_adaugare_rezervare(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_stergere_rezervare(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modificare_rezervare(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_trecerea_la_clasa_superioara(lista)
        elif optiune == "5":
            lista = ui_ieftinire_rezervari(lista)
        elif optiune == "6":
            ui_pret_maxim_pentru_clase(lista)
        elif optiune == "7":
            ui_ordonare_desc_dupa_pret(lista)
        elif optiune == "8":
            ui_suma_pret_pentru_nume(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Reincercati!")
