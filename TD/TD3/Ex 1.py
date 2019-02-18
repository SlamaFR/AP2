def somme(lst):
    """
    Renvoie la somme des nombres d'une liste de manière récursive.
    :param lst: Liste de nombres.
    :return: Somme des nombres de la liste.

    >>> somme([1, 2, 3, 4, 5])
    15

    >>> somme([])
    0
    """
    if len(lst) > 0:
        return lst[0] + somme(lst[1:])
    else:
        return 0


def minimum(lst):
    """
    Renvoie le minimum des nombres d'une liste de manière récursive.
    :param lst: Liste de nombres.
    :return: Somme des nombres de la liste.

    >>> minimum([1, -2, 3, -4, 5])
    -4

    >>> minimum([])
    """
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[0] if lst[0] < minimum(lst[1:]) else minimum(lst[1:])


def premiere_occurence(lst, elem, indice=0):
    """
    Renvoie l'indice de la première occurence d'un élément dans une liste de manière récursive.
    :param lst: Liste à parcourir.
    :param elem: Élement à rechercher.
    :param indice: Indice actuel.
    :return: Indice de la première occurence de l'élément dans la liste.

    >>> premiere_occurence([0, 1, 2, 1, 3, 1], 1)
    1

    >>> premiere_occurence([1, 2, 1, 3, 1], 5)
    """
    if indice >= len(lst):
        return None
    return indice if lst[indice] == elem else premiere_occurence(lst, elem, indice + 1)


def compte_occurence(lst, elem):
    """
    Renvoie l'indice de la première occurence d'un élément dans une liste de manière récursive.
    :param lst: Liste à parcourir.
    :param elem: Élement à rechercher.
    :return: Indice de la première occurence de l'élément dans la liste.

    >>> compte_occurence([0, 1, 2, 1, 3, 1], 1)
    3

    >>> compte_occurence([1, 2, 1, 3, 1], 5)
    0
    """
    occurences = 0
    if not lst:
        return 0
    if len(lst) > 1:
        if lst[0] == elem:
            occurences += 1
        return occurences + compte_occurence(lst[1:], elem)
    else:
        return 1 if elem in lst else 0


def dictionnaire_occurence(lst, dico=None):
    """
    Complète un dictionnaire d'occurence des éléments d'une liste.
    :param lst: Liste à parcourir
    :param dico: Dictionnaire à compléter

    >>> dictionnaire_occurence([0, 1, 2, 1, 3, 1])
    {0: 1, 1: 3, 2: 1, 3: 1}
    """
    if dico is None:
        dico = dict()

    if lst[0] not in dico:
        dico[lst[0]] = compte_occurence(lst, lst[0])

    if len(lst) > 1:
        dictionnaire_occurence(lst[1:], dico)
    return dico
