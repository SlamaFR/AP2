from turtle import *


def courbe_koch(l, n):
    """
    Dessine une courbe de Koch.
    :param l: Longueur de la courbe.
    :param n: Génération de la courbe.
    :return: Nombre de segments.
    """
    if n == 0:
        forward(l)
        return 1
    else:
        nb_segments = 0
        nb_segments += courbe_koch(l / 3, n - 1)
        left(60)
        nb_segments += courbe_koch(l / 3, n - 1)
        right(180 - 60)
        nb_segments += courbe_koch(l / 3, n - 1)
        left(60)
        nb_segments += courbe_koch(l / 3, n - 1)
        return nb_segments


def flocon_kock(l, n):
    """
    Dessine un flocon de Koch.
    :param l: Longueur du flocon.
    :param n: Génération du flocon.
    :return: Nombre de segments.
    """
    penup()
    setpos(-l / 2, l / 3)
    pendown()
    nb_segment = 0
    for i in range(3):
        nb_segment += courbe_koch(l, n)
        right(180 - 60)
    return nb_segment


hauteur = 500
largeur = 900
setup(largeur, hauteur)

speed(0)
hideturtle()

print("Segments :", flocon_kock(largeur/4, 4))

exitonclick()
