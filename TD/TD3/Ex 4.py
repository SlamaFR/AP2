def doublons(lst, unique=None):
    """
    Détecte si la liste contient des doublons
    :param lst: Liste.
    :param unique: Liste des éléments unique.
    :return: Booléen du résultat.

    >>> doublons([1, 2, 3, 4])
    False

    >>> doublons([1, 2, 3, 1])
    True
    """
    if unique is None:
        unique = list()

    if lst[0] not in unique:
        unique.append(lst[0])
        return doublons(lst[1:], unique) if len(lst) > 1 else False
    else:
        return True
