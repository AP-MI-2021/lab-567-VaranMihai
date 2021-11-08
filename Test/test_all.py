from Test.test_CRUD import test_adauga_rezervare, test_stergere_rezervare
from Test.test_domain import test_rezervare
from Test.test_functionalitati import test_trecere_la_clasa_superioara, test_pret_maxim_pentru_clase, \
    test_ordonare_desc_dupa_pret, test_suma_pret_pentru_nume


def run_all_tests():
    test_rezervare()
    test_adauga_rezervare()
    test_trecere_la_clasa_superioara()
    test_pret_maxim_pentru_clase()
    test_ordonare_desc_dupa_pret()
    test_suma_pret_pentru_nume()
