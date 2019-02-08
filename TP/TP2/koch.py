from turtle import *


def courbe_koch(l, n):
    """
    Dessine une courbe de Koch.
    :param l: Longueur de la courbe.
    :param n: Génération de la courbe.
    :return: Nombre de segments.
    """

    # Cas de base. Peut être modifié.
    if n == 0:
        forward(l)
        return 1
    # Rajouter ici le reste du code...
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


# création de la fenêtre
hauteur = 500
largeur = 900
setup(largeur, hauteur)

# réglages de la tortue
speed(0)  # vitesse (0 = vitesse max)
hideturtle()  # cacher la tortue

# placement de la tortue en bas à gauche de la fenêtre
penup()  # on relève le stylo
setpos(-largeur / 2, -hauteur / 2 + 20)  # placement de la tortue
pendown()  # on abaisse le stylo

# tracé de la courbe
print("Segments :", courbe_koch(largeur, 2))

# attendre un clic avant de fermer la fenêtre
exitonclick()
