from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_chekin
from Logic.CRUD import adauga_rezervare, get_by_id, stergere_rezervare


def test_adauga_rezervare():
    lista = adauga_rezervare("1" , "Pop" , "economy", 30 , "da", [])
    lista = adauga_rezervare("2", "Pop", "economy", 30, "da", lista)

    assert len(lista) == 2
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_nume(get_by_id("1", lista)) == "Pop"
    assert get_clasa(get_by_id("1", lista)) == "economy"
    assert get_pret(get_by_id("1", lista)) == 30
    assert get_chekin(get_by_id("1", lista)) == "da"

def test_stergere_rezervare():
    lista = adauga_rezervare("1", "Pop", "economy", 30, "da", [])
    lista = adauga_rezervare("2", "Pop", "economy", 30, "da", lista)

    lista = stergere_rezervare("1", lista)

    assert len(lista) == 1
    assert get_id("1") is None
    assert get_id("2") is not None

    lista = stergere_rezervare("3", lista)
    assert len(lista) == 1
    assert get_id("2") is not None