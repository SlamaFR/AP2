def fibo1(n):
    """
    Calcule le n-ième terme de la suite de Fibonacci
    :param n: Indice du terme.
    :return: N-ième terme et nombre d'appels de la fonction.

    >>> fibo1(4)
    (3, 9)
    """
    if 0 <= n <= 1:
        return n, 1
    else:
        a, compteur1 = fibo1(n - 1)
        b, compteur2 = fibo1(n - 2)
        return a + b, compteur1 + compteur2 + 1


# La fonction est très lente car pour l'indice 4 il faut appeler
# 9 fois, dont 8 fois de manière récursive.

def fibo2(n):
    """
    Affiche les deux derniers termes de la suite de Fibonacci.
    :param n: Indice du terme.
    :return: N-ième terme et terme précédent.

    >>> fibo2(4)
    (2, 3)
    """
    if n == 1:
        return 0, 1
    f0, f1 = fibo2(n - 1)
    return f1, f0 + f1


def fibo3(n, dico):
    """
    Calcule le n-ième terme de la suite de Fibonacci
    :param n: Indice du terme.
    :param dico: Dictionnaire contenant les termes déjà calculés.
    :return: N-ième terme.

    >>> fibo3(4, {})
    3
    """
    if 0 <= n <= 1:
        return n
    if n not in dico:
        dico[n] = fibo3(n - 1, dico) + fibo3(n - 2, dico)
    return dico[n]


print(fibo3(190, dict()))