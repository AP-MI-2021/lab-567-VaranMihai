from Domain.rezervare import creeaza_rezervare, get_id, get_nume, get_clasa, get_pret, get_chekin


def test_rezervare():
    rezervare = creeaza_rezervare("1" , "Pop" , "economy", 30 , "da")

    assert get_id(rezervare) == "1"
    assert get_nume(rezervare) == "Pop"
    assert get_clasa(rezervare) == "economy"
    assert get_pret(rezervare) == 30
    assert get_chekin(rezervare) == "da"