import doctest
from string import punctuation
from sys import argv


def maj_dico_compte(dico, mot, ligne):
    """
    Ajoute la ligne à la clé mot dans le dico.
    :param dico: Dictionnaire à modifier.
    :param mot: Clé à incrémenter.
    """
    if mot.lower() not in dico:
        dico[mot.lower()] = [ligne]
    else:
        dico[mot.lower()].append(ligne)


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


def compte_mots(str, ligne):
    """
    Renvoie un dictionnaire contenant le nombre d'occurences de chaque mot.
    :param str: Chaîne de caractères à analyser.
    :return: Dictionnaire des occurences.

    >>> compte_mots("Bonjour tout le monde ! Comment allez vous ?", 1)
    {'bonjour': [1], 'tout': [1], 'le': [1], 'monde': [1], 'comment': [1], 'allez': [1], 'vous': [1]}
    """
    dico = {}
    for mot in supprime_ponctuation(str).split():
        maj_dico_compte(dico, mot, ligne)
    return dico


def affiche_mots(dico):
    """
    Affiche de nombre de mots total, de mots différents et le nombre d'occurences
    de chaque mots.
    :param dico: Dictionnaire d'occurences.

    >>> affiche_mots({'a': [3], 'b': [2], 'c': [1]})
    a [3]
    b [2]
    c [1]
    """
    for elem in dico:
        print("{} {}".format(elem, dico[elem]))


if __name__ == "__main__":
    doctest.testmod()

    fichier = open(argv[1], "r")
    dico = {}

    for i, ligne in enumerate(fichier):
        for mot in compte_mots(ligne, i):
            maj_dico_compte(dico, mot, i)
    fichier.close()

    affiche_mots(dico)
