import time


def vol(a, compteur=0):
    """
    Calcule le temps de vol à partir de a.
    :param a: Terme initial.
    :param compteur: Nombre d'étapes effectuées.
    :return: Temps de vol.

    >>> vol(6)
    8
    """
    if a != 1:
        if a % 2 == 0:
            return vol(a // 2, compteur + 1)
        else:
            return vol(3 * a + 1, compteur + 1)
    else:
        return compteur


def vol_et_altitude(a, compteur=0, max_alt=None):
    """
    Calcule le temps de vol et l'altitude maximale à partir de a.
    :param a: Terme initial.
    :param compteur: Nombre d'étapes effectuées.
    :param max_alt: Altitude maximale constatée.
    :return: Temps de vol et altitude maximale.

    >>> vol_et_altitude(6)
    (8, 16)
    """
    if max_alt is None or a > max_alt:
        max_alt = a
    if a != 1:
        if a % 2 == 0:
            return vol_et_altitude(a // 2, compteur + 1, max_alt)
        else:
            return vol_et_altitude(3 * a + 1, compteur + 1, max_alt)
    else:
        return compteur, max_alt


def vol_et_altitude2(a, dico, compteur=0, max_alt=None):
    """
    Calcule le temps de vol et l'altitude maximale à partir de a.
    :param a: Terme initial.
    :param dico: Dictionnaire des listes de termes déjà calculés.
    :param compteur: Nombre d'étapes effectuées.
    :param max_alt: Altitude maximale constatée.
    :return: Temps de vol et altitude maximale.

    >>> vol_et_altitude2(6, dict())
    (8, 16)
    """
    if max_alt is None or a > max_alt:
        max_alt = a
    if a != 1:
        if a in dico:
            compteur_stock, max_alt_stock = dico[a]
            if max_alt_stock > max_alt:
                max_alt = max_alt_stock
            return compteur_stock + compteur, max_alt
        if a % 2 == 0:
            return vol_et_altitude2(a // 2, dico, compteur + 1, max_alt)
        else:
            return vol_et_altitude2(3 * a + 1, dico, compteur + 1, max_alt)
    else:
        return compteur, max_alt


# Avant optimisation : Environ 40K résultats en 1 seconde.

a = 1
debut = time.time()

while time.time() - debut < 1:
    vol_et_altitude(a)
    a += 1
print(a, vol_et_altitude(a))

# Après optimisation : Environ 400K résultats en 1 seconde.

a = 1
dico = dict()
debut = time.time()

while time.time() - debut < 1:
    dico[a] = vol_et_altitude2(a, dico)
    a += 1
print(a, vol_et_altitude2(a, dico))

# On constate que la fonction optimisée à l'aide d'un dictionnaire est 10 fois plus performante.
