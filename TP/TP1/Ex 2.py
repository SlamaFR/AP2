import doctest
from string import punctuation
from sys import argv

un_dico = {'toto': 3, 'titi': 1, 'tutu': 42}

un_dico["tata"] = 8

un_dico['titi'] += 1


def maj_dico_compte(dico, mot):
    """
    Ajoute 1 à la clé mot dans le dico.
    :param dico: Dictionnaire à modifier.
    :param mot: Clé à incrémenter.
    """
    if mot.lower() not in dico:
        dico[mot.lower()] = 1
    else:
        dico[mot.lower()] += 1


def supprime_ponctuation(str):
    """
    Supprime la ponctuation de la chaîne de caractères données.
    :param str: Chaîne de caractères.
    :return: Nouvelle chaîne de caractères.

    >>> supprime_ponctuation("Bonjour tout le monde ! Comment-allez vous ?")
    'Bonjour tout le monde  Commentallez vous '
    """
    for c in punctuation:
        str = str.replace(c, "")
    return str


def compte_mots(str):
    """
    Renvoie un dictionnaire contenant le nombre d'occurences de chaque mot.
    :param str: Chaîne de caractères à analyser.
    :return: Dictionnaire des occurences.

    >>> compte_mots("Bonjour tout le monde ! Comment allez vous ?")
    {'bonjour': 1, 'tout': 1, 'le': 1, 'monde': 1, 'comment': 1, 'allez': 1, 'vous': 1}
    """
    dico = {}
    for mot in supprime_ponctuation(str).split():
        maj_dico_compte(dico, mot)
    return dico


def compte_mots_total(dico):
    """
    Compte le nombre total de mot dans un dictionnaire d'occurences.
    :param dico: Dictionnaire d'occurence.
    :return: Nombre total de mots.

    >>> compte_mots_total({'tata': 8, 'tutu': 42, 'tati': 1, 'titi': 3, 'toto': 3})
    57
    """
    return sum(dico.values())


def affiche_mots(dico):
    """
    Affiche de nombre de mots total, de mots différents et le nombre d'occurences
    de chaque mots.
    :param dico: Dictionnaire d'occurences.

    >>> affiche_mots({'a': 3, 'b': 2, 'c':1})
    Nombre de mots : 6 - Nombre de mots différents : 3
    a : 3
    b : 2
    c : 1
    """
    print("Nombre de mots : {} - Nombre de mots différents : {}".format(
        compte_mots_total(dico),
        len(dico)
    ))
    for elem in dico:
        print("{} : {}".format(elem, dico[elem]))


def affiche_mots_importants(dico):
    """
    Affiche de nombre de mots total, de mots différents et le nombre d'occurences
    de chaque mots qui apparait entre 0.02% et 0.2% du temps.
    :param dico: Dictionnaire d'occurences.

    >>> affiche_mots_importants({'a': 3, 'b': 2, 'c':1})
    c : 1
    """
    for elem in dico:
        if 0.02 <= dico[elem] / compte_mots_total(dico) <= 0.2:
            print("{} : {}".format(elem, dico[elem]))


if __name__ == "__main__":
    fichier = open(argv[1], "r")
    dico = {}

    for ligne in fichier:
        for mot in compte_mots(ligne):
            maj_dico_compte(dico, mot)
    fichier.close()

    affiche_mots_importants(dico)

    doctest.testmod()
