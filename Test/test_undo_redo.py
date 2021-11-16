
from Logic.CRUD import adauga_rezervare


def test_undo_redo():
    lista = []
    undo_list = []
    redo_list = []
    lista = adauga_rezervare("1", "Pop", "economy", 30, "nu", [])
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_rezervare("2", "Dan", "buisness", 40, "da", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_rezervare("3", "Dan", "economy plus", 35, "da", lista)
    undo_list.append(lista)
    redo_list.clear()
    assert len(undo_list) == 3
    assert len(redo_list) == 0


    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(undo_list) == 2
    assert len(redo_list) == 1

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(undo_list) == 1
    assert len(redo_list) == 2

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(undo_list) == 0
    assert len(redo_list) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(undo_list) == 0
        assert len(redo_list) == 3
    else:
        pass

    lista = adauga_rezervare("1", "Ion", "economy", 30, "nu", [])
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_rezervare("2", "Andrei", "buisness", 40, "da", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_rezervare("3", "Cosmin", "economy plus", 35, "da", lista)
    undo_list.append(lista)
    redo_list.clear()

    assert len(undo_list) == 3
    assert len(redo_list) == 0

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(undo_list) == 1
        assert len(redo_list) == 2
    else:
        pass

    assert len(undo_list) == 3
    assert len(redo_list) == 0

    redo_list.append(lista)
    lista = undo_list.pop()
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(undo_list) == 1
    assert len(redo_list) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(undo_list) == 2
        assert len(redo_list) == 1
    else:
        pass

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(undo_list) == 3
        assert len(redo_list) == 0
    else:
        pass

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(undo_list) == 1
        assert len(redo_list) == 2
    else:
        pass

    lista = adauga_rezervare("4", "Razvan", "economy plus", 35, "da", lista)
    undo_list.append(lista)
    redo_list.clear()

    assert len(undo_list) == 2
    assert len(redo_list) == 0

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(undo_list) == 1
        assert len(redo_list) == 1
    else:
        pass

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(undo_list) == 1
        assert len(redo_list) == 1
    else:
        pass

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(undo_list) == 0
        assert len(redo_list) == 2
    else:
        pass

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(undo_list) == 2
        assert len(redo_list) == 0
    else:
        pass

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(undo_list) == 2
        assert len(redo_list) == 0
    else:
        pass




