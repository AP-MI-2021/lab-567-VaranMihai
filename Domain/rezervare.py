def creeaza_rezervare(id, nume, clasa, pret, chekin):
    """
    Creeaza un dictionar ce contine o rezervare
    :param id: id-ul rezervarii
    :param nume: numele pe baza caruia s-a facut rezervarea
    :param clasa: clasa la care s-a facut rezervarea
    :param pret: pretul rezervarii
    :param chekin: daca s-a facut chekin sau nu
    :return: un dictionar ce contine o rezervare
    """
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "chekin": chekin,
    }


def get_id(rezervare):
    """
    Determina id-ul unei rezervari
    :param rezervare: un dictionar de tip rezervare
    :return: id-ul rezervarii
    """
    return rezervare["id"]


def get_nume(rezervare):
    """
    Determina numele unei rezervari
    :param rezervare: un dictionare de tip rezervare
    :return: numele rezervarii
    """
    return rezervare["nume"]


def get_clasa(rezervare):
    """
    Determina clasa unei rezervari
    :param rezervare: un dictionare de tip rezervare
    :return: clasa rezervarii
    """
    return rezervare["clasa"]


def get_pret(rezervare):
    """
    Determina pretul unei rezervari
    :param rezervare: un dictionare de tip rezervare
    :return: pretul rezervarii
    """
    return rezervare["pret"]


def get_chekin(rezervare):
    """
    Determina chekin-ul unei rezervari
    :param rezervare: un dictionare de tip rezervare
    :return: chekin-ul rezervarii
    """
    return rezervare["chekin"]


def to_string(rezervare):
    return "id: {}, nume: {}, clasa: {}, pret: {}, chekin: {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_chekin(rezervare)
    )
