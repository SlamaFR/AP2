def factorielle_iterative(n):
    """
    Calculer la factorielle de n.
    :param n: (int) Nombre entier.
    :return: Factorielle de n.
    >>> factorielle_iterative(4)
    24
    """
    if n == 0:
        return 1
    resultat = n
    while n > 1:
        n -= 1
        resultat *= n
    return resultat


def factorielle_recursive(n):
    """
    Calculer la factorielle de n.
    :param n: Nombre entier.
    :return: Factorielle de n.
    >>> factorielle_recursive(0)
    1
    """
    if n < 2:
        return 1
    return n * factorielle_recursive(n - 1)
