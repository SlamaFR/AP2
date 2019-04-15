from timeit import timeit

from matplotlib import pyplot as plt


# L1 MI UPEM, AP2 2017-2018, TP 7 - Recherche

# Exercice 1


def teste_recherche_premier_indice(f, nb_elem):
    """Teste la fonction f sur plusieurs types de listes (croissantes)
    de taille <= nb_elem (avec ou sans l'élément cherché).
    """
    nb_erreurs = 0
    # test sur liste vide
    res = f([], 1)
    if res is not None:
        print("Échec - recherche de 1 dans [] :", res, "au lieu de None")
        nb_erreurs += 1

    # tests sur listes non vides
    for n in range(1, nb_elem + 1):

        # listes de longueur n ne contenant pas l'élément
        for i in range(n + 1):
            lst = [0] * i + [2] * (n - i)
            res = f(lst, 1)
            if res is not None:
                print("Échec - recherche de 1 dans", lst, ":", res, "au lieu de None")
                nb_erreurs += 1

        # listes de longueur n contenant l'élément
        for j in range(1, n + 1):
            for i in range(n - j + 1):
                lst = [0] * i + [1] * j + [2] * (n - i - j)
                res = f(lst, 1)
                if res != i:
                    print("Échec - recherche de 1 dans", lst, ":", res, "au lieu de", i)
                    nb_erreurs += 1
    print("{} erreur(s)".format(nb_erreurs))


def recherche_native(lst, elem):
    """Cette fonction utilise la méthode prédéfinie index pour chercher
    l'indice de elem dans lst.
    Si la valeur n'est pas trouvée, la fonction renvoie None.
    Le mécanisme utilisé ici (appelé gestion d'exceptions) n'est pas au
    programme du cours.
    """
    try:
        return lst.index(elem)
    except ValueError:
        return None


print("Recherche native :")
teste_recherche_premier_indice(recherche_native, 3)


# On lit "0 erreur(s)" et c'est normal puisque la recherche native fonctionne.


def recherche_fausse(lst, elem):
    for e in lst:
        if e == elem:
            return e
    return None


print("Recherche fausse :")
teste_recherche_premier_indice(recherche_fausse, 3)


# On lit :
# Échec - recherche de 1 dans [1] : 1 au lieu de 0
# Échec - recherche de 1 dans [1, 2] : 1 au lieu de 0
# Échec - recherche de 1 dans [1, 1] : 1 au lieu de 0
# Échec - recherche de 1 dans [1, 2, 2] : 1 au lieu de 0
# Échec - recherche de 1 dans [0, 0, 1] : 1 au lieu de 2
# Échec - recherche de 1 dans [1, 1, 2] : 1 au lieu de 0
# Échec - recherche de 1 dans [1, 1, 1] : 1 au lieu de 0
# 7 erreur(s)

# La deuxième fonction provoque des erreurs car elle retourne l'élément
# au lieu de retourner l'indice de ce dernier.

# Question 3

# Pour nb_elems = 3 on test avec :
# []
# [2]
# [0]
# [2, 2]
# [0, 2]
# [0, 0]
# [2, 2, 2]
# [0, 2, 2]
# [0, 0, 2]
# [0, 0, 0]

# Exercice 2


def premier_indice_exh_iter(lst, elem):
    """
    Parcours la liste et retourne le plus indice de l'élement ou
    None si celui-ci n'est pas trouvé.
    :param lst: Liste à parcourir.
    :param elem: Élément à rechercher.
    :return: Indice de l'élément ou None.

    >>> premier_indice_exh_iter([2, 2, 3, 4, 5], 3)
    2
    """
    for i, e in enumerate(lst):
        if e == elem:
            return i
    return None


def premier_indice_exh_rec(lst, elem):
    """
    Parcours la liste et retourne le plus indice de l'élement ou
    None si celui-ci n'est pas trouvé.
    :param lst: Liste à parcourir.
    :param elem: Élément à rechercher.
    :return: Indice de l'élément ou None.

    >>> premier_indice_exh_rec([2, 2, 3, 4, 5], 3)
    2
    """
    if not lst:
        return None
    if lst[0] == elem:
        return 0
    else:
        indice = premier_indice_exh_rec(lst[1:], elem)
        return 1 + indice if indice is not None else None


print("Recherche exhaustive itérative :")
teste_recherche_premier_indice(premier_indice_exh_iter, 3)
print("Recherche exhaustive récursive :")
teste_recherche_premier_indice(premier_indice_exh_rec, 3)


# Les fonctions effectuent le plus de calcul sur des listes où l'élément à chercher se trouve
# vers la fin. À l'inverse elle font moins de calculs lorsque l'élément est au début.

# La fonction itérative a une complexité de O(n).
# La fonction récursive a une complexité de O(2n).

# Exercice 3


def indice_dicho_iter(lst, elem):
    """
    Parcours la liste par dichotomie et retourne un indice de l'élement ou
    None si celui-ci n'est pas trouvé.
    :param lst: Liste à parcourir.
    :param elem: Élément à rechercher.
    :return: Indice de l'élément ou None.

    >>> indice_dicho_iter([2, 2, 3, 4, 5], 3)
    2
    """
    if not lst:
        return None
    minimum = 0
    maximum = len(lst) - 1
    while abs(minimum - maximum) > 1:
        milieu = (minimum + maximum) // 2
        if lst[milieu] > elem:
            maximum = milieu
        elif lst[milieu] < elem:
            minimum = milieu
        else:
            return milieu
    if lst[minimum] == elem:
        return minimum
    elif lst[maximum] == elem:
        return maximum
    else:
        return None


print("Recherche dichotomique itérative :")
teste_recherche_premier_indice(indice_dicho_iter, 3)


# On voit que la fonction produits des erreurs car elle retourne un indice mais pas
# nécessairement le premier.

# La fonction itérative a une complexité de O(log(2, n)).
# La fonction récursive a une complexité de O(log(2, n)).


def indice_dicho_rec(lst, elem):
    """
    Parcours la liste par dichotomie et retourne un indice de l'élement ou
    None si celui-ci n'est pas trouvé.
    :param lst: Liste à parcourir.
    :param elem: Élément à rechercher.
    :return: Indice de l'élément ou None.

    >>> indice_dicho_rec([2, 2, 3, 4, 5], 3)
    2
    """
    if not lst:
        return None
    if len(lst) == 1 and lst[0] != elem:
        return None
    milieu = (len(lst) - 1) // 2
    if lst[milieu] > elem:
        suivant = indice_dicho_rec(lst[:milieu + 1], elem)
        return suivant if suivant is None else milieu - 1 - suivant
    if lst[milieu] < elem:
        suivant = indice_dicho_rec(lst[milieu + 1:], elem)
        return suivant if suivant is None else milieu + 1 + suivant
    if lst[milieu] == elem:
        return milieu


print("Recherche dichotomique récursive :")
teste_recherche_premier_indice(indice_dicho_rec, 3)


# Comme pour la fonction précédente, cette fonction crée des erreurs car elle retourne un indice
# mais nécessairement le premier.


# Exercice 4


def trace_courbes(abscisses, series, title='', xlabel='', ylabel=''):
    """Pour chaque couple (nom, ordonnées) de la liste series, trace la courbe
    des ordonnees avec la legende nom dans matplotlib. L'abscisse des points
    est donnée par la liste abscisses.
    Le paramètres optionnels title, xlabel et ylabel donnent le titre du
    graphique et les étiquettes des axes x et y."""
    for nom, donnees in series:
        plt.plot(abscisses, donnees, label=nom)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()


def chrono(fonction, args, nombre=100000):
    """Renvoie le temps d'exécution en secondes de 'nombre' répétitions de
    l'appel fonction(*args)."""

    # le plus simple est de passer à la fonction timeit une fonction sans
    # argument, donc on doit définir une fonction auxiliaire
    def f():
        # passe un par un chaque argument de la liste args à
        # la fonction
        return fonction(*args)

    return timeit(f, number=nombre)


temps = {
    "Native": list(),
    "Fausse": list(),
    "Exhaustive itérative": list(),
    "Exhaustive récursive": list(),
    "Dichotomique itérative": list(),
    "Dichotomique récursive": list()
}

series = []

MAXIMUM = 60

for i in range(MAXIMUM):
    liste = list(range(i))
    temps["Native"].append(chrono(recherche_native, [liste, i]))
    temps["Fausse"].append(chrono(recherche_fausse, [liste, i]))
    temps["Exhaustive itérative"].append(chrono(premier_indice_exh_iter, [liste, i]))
    temps["Exhaustive récursive"].append(chrono(premier_indice_exh_rec, [liste, i]))
    temps["Dichotomique itérative"].append(chrono(indice_dicho_iter, [liste, i]))
    temps["Dichotomique récursive"].append(chrono(indice_dicho_rec, [liste, i]))

for e in temps:
    series.append((e, temps[e]))

trace_courbes(list(range(MAXIMUM)), series, xlabel="Taille de la liste", ylabel="Temps en secondes")
