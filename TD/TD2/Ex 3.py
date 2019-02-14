def somme_chiffres(n):
    """
    Calcule la sommes des chiffres composant un entier n.
    :param n: Nombre entiers.
    :return: Somme des chiffres.

    >>> somme_chiffres(123)
    6
    """
    if n < 10:
        return n

    somme = n % 10 + somme_chiffres(n // 10)
    return somme


def chiffre_somme_chiffres(n):
    """
    Calcule la sommes des chiffres de la somme des chiffres composant un entier n.
    :param n: Nombre entiers.
    :return: Somme des chiffres.

    >>> chiffre_somme_chiffres(12345)
    6
    """
    return somme_chiffres(somme_chiffres(n))
