from turtle import *


def courbe_koch(l, n):
    """
    Dessine une courbe quadrique de Koch de type 1.
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
        left(90)
        nb_segments += courbe_koch(l / 3, n - 1)
        right(90)
        nb_segments += courbe_koch(l / 3, n - 1)
        right(90)
        nb_segments += courbe_koch(l / 3, n - 1)
        left(90)
        nb_segments += courbe_koch(l / 3, n - 1)
        return nb_segments


hauteur = 500
largeur = 900
setup(largeur, hauteur)

speed(0)
hideturtle()

penup()
setpos(-largeur / 2, -hauteur / 2 + 20)
pendown()

print("Segments :", courbe_koch(largeur, 3))

exitonclick()
