from Domain.rezervare import get_nume, creeaza_rezervare, get_id, get_pret, get_chekin, get_clasa


def trecere_la_alta_clasa(string_nume, lista):
    """
    Trece toate rezervariile facute pe un nume dat la o clasa superioara
    :param string_nume: Numele dat
    :param lista: lista de rezervari
    :return: lista de rezervari cu rezervariile modificate
    """
    if str(string_nume) is False:
        raise ValueError("Numele este scris gresit!")
    lista_noua = []
    for rezervare in lista:
        if string_nume in get_nume(rezervare):
            if get_clasa(rezervare) == "economy":
                clasa_noua = "economy plus"
                rezervare_noua = creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    clasa_noua,
                    get_pret(rezervare),
                    get_chekin(rezervare),
                )
                lista_noua.append(rezervare_noua)
            elif get_clasa(rezervare) == "economy plus":
                clasa_noua = "buisness"
                rezervare_noua = creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    clasa_noua,
                    get_pret(rezervare),
                    get_chekin(rezervare),
                )
                lista_noua.append(rezervare_noua)
            else:
                lista_noua.append(rezervare)

        else:
            lista_noua.append(rezervare)
    return lista_noua


def ieftinire_pret(procentaj, lista):
    """
    Reduce pretul rezervariilor unde s-a facut checkin cu un procentaj dat
    :param procentaj: procentajul cu care se reduce pretul rezervarii
    :param lista: lista de rezervari
    :return: lista noua cu pretul rezervariilor redus
    """
    if procentaj < 0:
        raise ValueError("Procentajul nu poate fi negativ!")
    lista_noua = []
    for rezervare in lista:
        if get_chekin(rezervare) == "da":
            reducere = get_pret(rezervare)/100*procentaj
            rezervare_noua = creeaza_rezervare(
                get_id(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                get_pret(rezervare) - reducere,
                get_chekin(rezervare)
            )
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua


def pret_maxim_pentru_clase(lista):
    """
    Determina pretul maxim pentru fiecare clasa dintr-o lista
    :param lista: lista de rezervari
    :return: pretul maxim pentru fiecare clasa a rezervariilor din lista
    """
    rezultat = {}
    for rezervare in lista:
        clasa = get_clasa(rezervare)
        pret = get_pret(rezervare)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
            rezultat[clasa] = pret
    return rezultat


def ordonare_desc_dupa_pret(lista):
    """
    Ordoneaza descrescator rezervariile dintr-o lista dupa pret
    :param lista: lista de rezervari
    :return: lista de rezervari ordonata descrescator dupa pretul rezervariilor
    """
    return sorted(lista, key=lambda rezervare: get_pret(rezervare), reverse=True)


def suma_pret_pentru_nume(lista):
    """
    Afiseaza sumele preturilor dupa fiecare nume dintr-o lista
    :param lista: lista de rezervari
    :return: sumele preturilor pentru fiecare nume din lista
    """
    rezultat = {}
    for rezervare in lista:
        nume = get_nume(rezervare)
        pret = get_pret(rezervare)
        if nume in rezultat:
            rezultat[nume] += pret
        else:
            rezultat[nume] = pret
    return rezultat
