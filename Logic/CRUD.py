from Domain.rezervare import creeaza_rezervare, get_id


def adauga_rezervare(id, nume, clasa, pret, chekin, lista):
    '''
    Adauga o rezervare intr-o lista
    :param id: id-ul unei rezervari
    :param nume: numele rezervarii
    :param clasa: clasa la care a fost facuta rezervarea
    :param pret: pretul rezervarii
    :param chekin: daca s-a facut chekin sau nu
    :param lista: lista de rezervari
    :return: o lista continand lista veche si o rezervare noua adaugata listei
    '''
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    rezervare = creeaza_rezervare(id, nume, clasa, pret, chekin)
    return lista + [rezervare]


def get_by_id(id, lista):
    '''
    Determina o rezervare cu id-ul dat
    :param id: id-ul dat
    :param lista: lista de rezervari
    :return: rezervarea cu id-ul dat sau None daca nu exista
    '''

    for rezervare in lista:
        if get_id(rezervare) == id:
            return rezervare
    return None


def stergere_rezervare(id, lista):
    '''
    Sterge o rezervare dintr-o lista dupa id
    :param id: id-ul rezervarii
    :param lista: lista de rezervari
    :return: lista cu o rezervare stearsa
    '''
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o rezervare cu id-ul dat!")
    return [rezervare for rezervare in lista if get_id(rezervare) != id]


def modifica_rezervare(id, nume, clasa, pret, chekin, lista):
    '''
    Modifica o rezervare dintr-o lista
    :param id: id-ul dupa care se face modificarea
    :param nume: noul nume
    :param clasa: noua clasa
    :param pret: noul pret
    :param chekin: noul chekin
    :param lista: lista de rezervari
    :return: lista noua cu rezervarea modificata
    '''
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o rezervare cu id-ul dat!")
    lista_noua = []
    for rezervare in lista:
        if get_id(rezervare) == id:
            rezervare_noua = creeaza_rezervare(id, nume, clasa, pret, chekin)
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua
