def freq_chaine(str):
    """
    Compte le nombre d'occurences de chaque caractères d'une chaîne.
    :param str: Chaîne de caractères.
    :return: Dictionnaire contenant les occurences de chaque caractères.

    >>> freq_chaine('abbabba!')
    {'a': 3, 'b': 4, '!': 1}
    """
    dico = {}
    for c in str:
        if c not in dico:
            dico[c] = 0
        dico[c] += 1
    return dico


def max_dic(dico):
    """
    Renvoie la clé correspondant à la plus grande valeur.
    :param dico: Dictionnaire contennant des entiers.
    :return: Clé correspondant à la plus grande valeur.

    >>> max_dic({'a': 3, 'b': 5 , 'c': 0, 'd': 10})
    'd'
    """
    cle_max = list(dico)[0]
    val_max = dico[cle_max]
    for cle in dico:
        if dico[cle] > val_max:
            cle_max = cle
            val_max = dico[cle]
    return cle_max


def tri_cles(dico):
    """
    Renvoie la liste des clés par ordre décroissant des valeurs.
    :param dico: Dictionnaire contenant des entiers.
    :return: Liste des clés.

    >>> tri_cles({'a': 3, 'b': 5, 'c': 0, 'd': 10})
    ['d', 'b', 'a', 'c']
    """
    resultat = []
    dico_copie = dico.copy()
    for i in range(len(dico)):
        max_cle = max_dic(dico_copie)
        resultat.append(max_cle)
        dico_copie.pop(max_cle)
    return resultat
