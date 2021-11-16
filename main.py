from Logic.CRUD import adauga_rezervare
from Test.test_all import run_all_tests
from UI.console import run_menu


def main():
    run_all_tests()
    lista = []
    lista = adauga_rezervare("1", "Pop", "economy", 30, "nu", [])
    lista = adauga_rezervare("2", "Dan", "buisness", 40, "da", lista)
    lista = adauga_rezervare("3", "Dan", "economy plus", 35, "da", lista)
    run_menu(lista)


main()
