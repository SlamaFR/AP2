def donnees_croissantes(lst):
    """
    Détermine si les données d'une liste sont croissantes.
    :param lst: Liste.
    :return: Booléen du résultat.

    >>> donnees_croissantes([1, 2, 3])
    True

    >>> donnees_croissantes([1, 4, 2, 3])
    False

    >>> donnees_croissantes([])
    True
    """
    if not lst:
        return True
    if len(lst) > 2:
        if lst[1] > lst[0]:
            return donnees_croissantes(lst[1:])
        else:
            return False
    return lst[1] > lst[0]
