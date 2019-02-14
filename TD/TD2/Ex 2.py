def somme_iterative(n):
    """
    Calculer la somme des n premiers entiers.
    :param n: (int) Nombre entier.
    :return: Factorielle de n.
    >>> somme_iterative(4)
    10
    """
    if n == 0:
        return 1
    resultat = n
    while n > 1:
        n -= 1
        resultat += n
    return resultat


def somme_recursive(n):
    """
    Calculer la somme des n premiers entiers.
    :param n: Nombre entier.
    :return: Factorielle de n.
    >>> somme_recursive(0)
    1
    """
    if n < 2:
        return 1
    return n + somme_recursive(n - 1)


# Modifiez les expressions pour la sommes des cubes des n premiers entiers.


def somme_cubes_iterative(n):
    """
    Calculer la somme des cubes des n premiers entiers.
    :param n: (int) Nombre entier.
    :return: Factorielle de n.
    >>> somme_cubes_iterative(4)
    100
    """
    if n == 0:
        return 1
    resultat = n
    while n > 1:
        n -= 1
        resultat += n
    return resultat ** 2


def somme_cubes_recursive(n):
    """
    Calculer la somme des cubes des n premiers entiers.
    :param n: Nombre entier.
    :return: Factorielle de n.
    >>> somme_cubes_recursive(0)
    1
    """
    if n < 2:
        return 1
    return (n + somme_recursive(n - 1)) ** 2
