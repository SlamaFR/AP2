def affiche_premiers_naturels_croissant(n):
    """
    Affiche les n premiers naturels de manière croissante.
    :param n: Nombre naturel n.

    >>> affiche_premiers_naturels_croissant(4)
    0
    1
    2
    3
    4
    """
    if n > 0:
        affiche_premiers_naturels_croissant(n - 1)
    print(n)


def affiche_premiers_naturels_decroissant(n):
    """
    Affiche les n premiers naturels de manière décroissante.
    :param n: Nombre naturel n.

    >>> affiche_premiers_naturels_decroissant(4)
    4
    3
    2
    1
    0
    """
    print(n)
    if n > 0:
        affiche_premiers_naturels_decroissant(n - 1)


def affiche_premiers_naturels_decroissant_puis_croissant(n, i=0):
    """
    Affiche les n premiers naturels de manière décroissante puis croissante.
    :param n: Nombre naturel n.

    >>> affiche_premiers_naturels_decroissant_puis_croissant(4)
    4
    3
    2
    1
    0
    1
    2
    3
    4
    """
    if 2 * n < i:
        return
    print(abs(n - i))
    affiche_premiers_naturels_decroissant_puis_croissant(n, i + 1)


def affiche_premiers_naturels_croissant_puis_decroissant(n):
    """
    Affiche les n premiers naturels de manière croissante puis décroissante.
    :param n: Nombre naturel n.

    >>> affiche_premiers_naturels_croissant_puis_decroissant(4)
    0
    1
    2
    3
    4
    3
    2
    1
    0
    """
    affiche_premiers_naturels_croissant(n)
    affiche_premiers_naturels_decroissant(n - 1)
