def diagonale_g(n):
    """
    Affiche une diagonale d'étoiles descendant vers la gauche.
    :param n: Nombre d'étoiles.

    >>> diagonale_g(5)
        *
       *
      *
     *
    *
    """
    if n < 1:
        return
    print(" " * (n - 1) + "*")
    diagonale_g(n - 1)


def diagonale_d(n):
    """
    Affiche une diagonale d'étoiles descendant vers la gauche.
    :param n: Nombre d'étoiles.

    >>> diagonale_d(5)
    *
     *
      *
       *
        *
    """
    if n < 1:
        return
    diagonale_d(n - 1)
    print(" " * (n - 1) + "*")


def triangle(n, i=0):
    """
    Affiche un triangle d'étoile de hauteur n.
    :param n: Hauteur du triangle.
    :param i: Indice de la ligne.

    >>> triangle(5)
        *
       ***
      *****
     *******
    *********
    """
    if n < 1:
        return
    print((n - 1) * " " + (2 * i + 1) * "*")
    triangle(n - 1, i + 1)


def triangle2(n, i=0):
    """
    Affiche un triangle renversé d'étoiles de hauteur n.
    :param n: Hauteur du triangle.
    :param i: Indice de la ligne.

    >>> triangle2(5)
    *********
     *******
      *****
       ***
        *
    """
    if n < 1:
        return
    triangle2(n - 1, i + 1)
    print((n - 1) * " " + (2 * i + 1) * "*")


def sablier(n, i=0):
    """
    Affiche un sablier d'étoiles de hauteur n.
    :param n: Hauteur du sablier.
    :param i: Indice de la ligne.

    >>> sablier(5)
    *****
     ***
      *
     ***
    *****
    """
    if n < 1:
        return
    if n - i > 0:
        print(i * " " + (n - i) * "*")
    elif n > 1:
        print(abs(n * 2 - i) * " " + (abs(n - i) + 2) * "*")
    else:
        print((abs(n - i) + 2) * "*")
    sablier(n - 1, i + 1)
