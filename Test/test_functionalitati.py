from Domain.rezervare import get_clasa, get_id
from Logic.CRUD import adauga_rezervare, get_by_id
from Logic.functionalitati import trecere_la_alta_clasa, pret_maxim_pentru_clase, ordonare_desc_dupa_pret, \
    suma_pret_pentru_nume


def test_trecere_la_clasa_superioara():
    lista = []
    lista = adauga_rezervare("1", "Andrei", "economy", 30, "da", [])
    lista = adauga_rezervare("2", "Ion", "economy plus", 35, "da", lista)
    lista = adauga_rezervare("3", "Ion", "buisness", 40, "da", lista)

    lista = trecere_la_alta_clasa("Ion", lista)

    assert get_clasa(get_by_id("1", lista)) == "economy"
    assert get_clasa(get_by_id("2", lista)) == "buisness"
    assert get_clasa(get_by_id("3", lista)) == "buisness"


def test_pret_maxim_pentru_clase():
    lista = []
    lista = adauga_rezervare("1", "Andrei", "economy", 30, "da", [])
    lista = adauga_rezervare("2", "Ion", "economy", 35, "da", lista)
    lista = adauga_rezervare("3", "Ion", "buisness", 40, "da", lista)

    rezultat = pret_maxim_pentru_clase(lista)

    assert len(rezultat) == 2
    assert rezultat["economy"] == 35
    assert rezultat["buisness"] == 40


def test_ordonare_desc_dupa_pret():
    lista = []
    lista = adauga_rezervare("1", "Andrei", "economy", 30, "da", [])
    lista = adauga_rezervare("2", "Ion", "economy plus", 35, "da", lista)
    lista = adauga_rezervare("3", "Ion", "buisness", 40, "da", lista)

    rezultat = ordonare_desc_dupa_pret(lista)
    assert get_id(rezultat[0]) == "3"
    assert get_id(rezultat[1]) == "2"
    assert get_id(rezultat[2]) == "1"


def test_suma_pret_pentru_nume():
    lista = []
    lista = adauga_rezervare("1", "Andrei", "economy", 30, "da", [])
    lista = adauga_rezervare("2", "Ion", "economy plus", 35, "da", lista)
    lista = adauga_rezervare("3", "Ion", "buisness", 40, "da", lista)

    rezultat = suma_pret_pentru_nume(lista)

    assert len(rezultat) == 2
    assert rezultat["Ion"] == 75
    assert rezultat["Andrei"] == 30