def divisible_par_sept(n):
    """
    Détermine si un nombre n est divisible par 7.
    :param n: Nombre naturel n.
    :return: Divisibilité par 7.

    >>> divisible_par_sept(14)
    True
    """
    d = n // 10
    u = n % 10
    return True if abs(n) == 7 else divisible_par_sept(d - 2 * u)
