# Le dictionnaire en début de partie est vide :

dico = {}


# La fonction print(plateau) affiche :

# {'NO':'X', 'NE': 'X', 'C': 'O', 'SO': 'O'}
# {'O': 'X', 'C': 'O', 'SO': 'X', 'SE': 'O'}


def affiche_grille(plateau):
    """
    Affiche la plateau mis en forme.
    :param plateau: Dictionnaire du plateau.

    >>> affiche_grille({'NO':'X', 'NE': 'X', 'C': 'O', 'SO': 'O'})
     X |   | X
    ---+---+---
       | O |
    ---+---+---
     O |   |
    """
    print(" {} | {} | {} ".format(plateau.get('NO', ' '), plateau.get('N', ' '), plateau.get('NE', ' ')))
    print("---+---+---")
    print(" {} | {} | {} ".format(plateau.get('O', ' '), plateau.get('C', ' '), plateau.get('E', ' ')))
    print("---+---+---")
    print(" {} | {} | {} ".format(plateau.get('SO', ' '), plateau.get('S', ' '), plateau.get('SE', ' ')))


def pose_pion(plateau, position, j):
    """
    Poser un pion.
    :param plateau: Dictionnaire du plateau.
    :param position: Position du pion.
    :param j: Joueur.
    :return: Booléan exprimant la possibilité du coup.
    """
    if position in plateau:
        return False
    plateau[position] = j
    return True


def rempli(plateau):
    """
    :param plateau: Dictionnaire du plateau.
    :return: Booléen exprimant le remplissage intégral du plateau.
    """
    return len(plateau) == 9


LIGNES = [
    ['NO', 'N', 'NE'],
    ['O', 'C', 'E'],
    ['SO', 'S', 'SE'],
    ['NE', 'E', 'SE'],
    ['N', 'C', 'S'],
    ['NO', 'O', 'SO'],
    ['NO', 'C', 'SE'],
    ['NE', 'C', 'SO'],
]


def ligne_gagnante(plateau, ligne):
    """
    Détermine si une ligne est gagnante.
    :param plateau: Dictionnaire du plateau.
    :param ligne: Liste des positions de la ligne.
    :return: Symbole du joueur gagnant ou False.
    """
    pions = []
    for position in ligne:
        if position in plateau:
            pions.append(plateau[position])
    if 'X' in pions and 'O' not in pions and len(pions) == 3:
        return 'X'
    if 'O' in pions and 'X' not in pions and len(pions) == 3:
        return 'O'
    return False


def gagnant(plateau):
    """
    Détermine si un joueur à gagné.
    :param plateau: Dictionnaire du plateau.
    :return: Symbole du joueur gagnant ou False.
    """
    for ligne in LIGNES:
        if not ligne_gagnante(plateau, ligne):
            continue
        return ligne_gagnante(plateau, ligne)
    return False
