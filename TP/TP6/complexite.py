# Exercice 1 - Tracé de courbes
import math
from timeit import timeit

from matplotlib import pyplot as plt


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


abcsisses = list()
courbe1 = list()
courbe2 = list()
courbe3 = list()
for i in range(1, 101):
    abcsisses.append(i)
    courbe1.append(math.log(i, 2))
    courbe2.append(len(bin(i)) - 2)
    courbe3.append(math.log(i, 2) + 1)


trace_courbes(abcsisses, [("log(x, 2)", courbe1), ("Nombre de chiffre écriture binaire de x", courbe2),
                          ("log(x, 2) + 1", courbe3)])


# Exercice 2 - Chronométrage de fonction


def chrono(fonction, args, nombre=100000):
    """Renvoie le temps d'exécution en secondes de 'nombre' répétitions de
    l'appel fonction(n)."""

    # le plus simple est de passer à la fonction timeit une fonction sans
    # argument, donc on doit définir une fonction auxiliaire
    def f():
        # passe un par un chaque argument de la liste args à
        # la fonction
        return fonction(*args)

    return timeit(f, number=nombre)


def croissant(n):
    """Renvoie la liste des nombres entiers de 0 à n-1 par ordre croissant."""
    res = []
    for i in range(n):
        res.append(i)
    return res


def decroissant(n):
    """Renvoie la liste des nombres entiers de 0 à n-1 par ordre décroissant."""
    res = []
    for i in range(n):
        res.insert(0, i)
    return res


print(chrono(croissant, [1000]))    # 6.62 Secondes.
print(chrono(decroissant, [1000]))  # 28.1 Secondes.


# Exercice 3 - Calculs de puissance

def puissance_native(a, n):
    return a ** n


def puissance1_rec(a, n):
    if n == 0:
        return 1
    else:
        return a * puissance1_rec(a, n - 1)


def puissance1_iter(a, n):
    res = 1
    for _ in range(n):
        res *= a
    return res


def puissance2_rec(a, n):
    if n == 0:
        return 1
    else:
        tmp = puissance2_rec(a * a, n // 2)
        if n % 2 == 1:
            tmp *= a
        return tmp


def puissance2_iter(a, n):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= a
        a *= a
        n //= 2
    return res


def puissance3_rec(a, n):
    if n == 0:
        return 1
    else:
        tmp = puissance3_rec(a, n // 2)
        tmp *= tmp
        if n % 2 == 1:
            tmp *= a
        return tmp


def puissance3_iter(a, n):
    res = 1
    for d in bin(n)[2:]:
        res *= res
        if d == '1':
            res *= a
    return res


temps = {"native": [],
         "1_iter": [],
         "1_rec": [],
         "2_iter": [],
         "2_rec": [],
         "3_iter": [],
         "3_rec": []}

for n in range(1, 100):
    temps["native"].append(chrono(puissance_native, [2, n]))
    temps["1_iter"].append(chrono(puissance1_iter, [2, n]))
    temps["1_rec"].append(chrono(puissance1_rec, [2, n]))
    temps["2_iter"].append(chrono(puissance2_iter, [2, n]))
    temps["2_rec"].append(chrono(puissance2_rec, [2, n]))
    temps["3_iter"].append(chrono(puissance3_iter, [2, n]))
    temps["3_rec"].append(chrono(puissance3_rec, [2, n]))

series = []

# for i, time in enumerate(sorted(temps, key=temps.get)):
#     print("{}e\t{}\t{}s".format(str(i + 1), time, str(round(temps[time], 3))))

for time in temps:
    series.append((time + "(n)", temps[time]))

trace_courbes(list(range(1, 100)), series, xlabel="Valeur de n", ylabel="Temps en secondes")


# Exercice 4 - Renversement de liste

def renverse_1(lst):
    if len(lst) == 0:
        return []
    else:
        return renverse_1(lst[1:]) + [lst[0]]


def renverse_2(lst):
    if len(lst) == 0:
        return []
    else:
        res = renverse_2(lst[1:])
        res.append(lst[0])
        return res


def renverse_3(lst, i=0):
    if i == len(lst):
        return []
    else:
        res = renverse_3(lst, i + 1)
        res.append(lst[i])
        return res


def renverse_4(lst):
    res = []
    for e in lst:
        res.insert(0, e)
    return res


def renverse_5(lst):
    res = []
    for e in lst[::-1]:
        res.append(e)
    return res


def renverse_6(lst):
    res = []
    for i in range(len(lst) - 1, -1, -1):
        res.append(lst[i])
    return res


def renverse_7(lst):
    return list(reversed(lst))


temps = {
    1: list(),
    2: list(),
    3: list(),
    4: list(),
    5: list(),
    6: list(),
    7: list()
}

series = []
MAXIMUM = 500

for i in range(1, MAXIMUM):
    temps[1].append(chrono(renverse_1, [[0] * i], 1))
    temps[2].append(chrono(renverse_2, [[0] * i], 1))
    temps[3].append(chrono(renverse_3, [[0] * i], 1))
    temps[4].append(chrono(renverse_4, [[0] * i], 1))
    temps[5].append(chrono(renverse_5, [[0] * i], 1))
    temps[6].append(chrono(renverse_6, [[0] * i], 1))
    temps[7].append(chrono(renverse_7, [[0] * i], 1))

for time in temps:
    series.append(("reverse_" + str(time), temps[time]))

trace_courbes(list(range(1, MAXIMUM)), series, xlabel="Taille de la liste", ylabel="Temps en secondes")
