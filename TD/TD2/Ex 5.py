def pgcd(a, b):
    """
    Calcule le plus grand diviseur commun à a et b.
    :param a: Terme a.
    :param b: Terme b.
    :return: Plus grand diviseur commun.

    >>> pgcd(2, 4)
    2
    """
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return 1
    if a != 0:
        return pgcd(a, b % a)
    if b != 0:
        return pgcd(b, a % b)
