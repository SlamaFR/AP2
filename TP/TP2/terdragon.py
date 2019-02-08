from turtle import *
from math import sqrt


def terdragon(l, n):
    """
    Dessine une courbe terdragon.
    :param l: Longueur de la courbe.
    :param n: Génération de la courbe.
    :return: Nombre de segments.
    """
    if n == 0:
        forward(l)
        return 1
    else:
        nb_segments = 0
        nb_segments += terdragon(l / sqrt(3), n - 1)
        right(180 - 60)
        nb_segments += terdragon(l / sqrt(3), n - 1)
        left(180 - 60)
        nb_segments += terdragon(l / sqrt(3), n - 1)
        return nb_segments


generation = 7

hauteur = 700
largeur = 900
setup(largeur, hauteur)

speed(0)
hideturtle()

penup()
setpos(-largeur / 4, 0)
left(generation * 30)
pendown()

print("Segments :", terdragon(largeur / 2, generation))

exitonclick()
