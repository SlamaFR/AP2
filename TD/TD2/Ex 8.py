CHAINE_CONVERSION = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decimal_vers_binaire(n):
    """
    Convertit un nombre décimal en nombre binaire.
    :param n: Nombre décimal.
    :return: Nombre binaire.

    >>> decimal_vers_binaire(10)
    1010
    """
    if n < 2:
        return n
    else:
        q = n // 2
        r = n % 2
        return decimal_vers_binaire(q) * 10 + r


def decimal_vers_binaire2(n):
    """
    Convertit un nombre décimal en nombre binaire.
    :param n: Nombre décimal.
    :return: Nombre binaire sous forme de chaîne de caractères.

    >>> decimal_vers_binaire2(10)
    '1010'
    """
    if n < 2:
        return str(n)
    else:
        q = n // 2
        r = n % 2
        return decimal_vers_binaire2(q) + str(r)


def decimal_vers_base(n, b):
    """
    Convertit un nombre décimal en base b inférieure à 10.
    :param n: Nombre décimal.
    :param b: Nouvelle base.
    :return: Nombre en base b.

    >>> decimal_vers_base(10, 4)
    22
    """
    if n < b:
        return n
    else:
        q = n // b
        r = n % b
        return decimal_vers_base(q, b) * 10 + r


# Pour étendre à des bases supérieures à 10, on doit utiliser d'autre caractères.
# Grâce à l'alphabet on peut étendre jusqu'à la base 36.


def decimal_vers_base_b(n, b):
    """
    Convertit un nombre décimal en base b.
    :param n: Nombre décimal.
    :param b: Nouvelle base.
    :return: Nombre en base b.

    >>> decimal_vers_base_b(255, 16)
    'FF'
    """
    if n < b:
        return CHAINE_CONVERSION[n]
    else:
        q = n // b
        r = n % b
        return decimal_vers_base_b(q, b) + CHAINE_CONVERSION[r]
