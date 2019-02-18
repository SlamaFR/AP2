def nombres_croissants(n, liste=None):
    """
    Retourne une liste de 1 à n dans l'ordre croissant.
    :param n: Entier n.
    :param liste: Liste des entiers.
    :return: Liste des entiers finale.

    >>> nombres_croissants(4)
    [1, 2, 3, 4]
    """
    if liste is None:
        liste = list()

    if len(liste) < n:
        liste.append(len(liste) + 1)
        return nombres_croissants(n, liste)
    else:
        return liste


def nombres_decroissants(n, liste=None):
    """
    Retourne une liste de 1 à n dans l'ordre décroissant.
    :param n: Entier n.
    :param liste: Liste des entiers.
    :return: Liste des entiers finale.

    >>> nombres_decroissants(4)
    [4, 3, 2, 1]
    """
    if liste is None:
        liste = list()

    if len(liste) < n:
        liste.append(n - len(liste))
        return nombres_decroissants(n, liste)
    else:
        return liste
