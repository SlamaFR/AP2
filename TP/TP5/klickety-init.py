# Imports ---------------------------------------------------------------------
import random
import tkinter.font
from tkinter import Tk, Frame, Button, BOTH, Canvas, TOP, \
    BOTTOM, ALL

COULEURS = ["red", "blue", "green", "yellow", "magenta"]


def initialiser_plateau(hauteur, largeur):
    """Renvoie un plateau hauteur x largeur aléatoire de blocs de couleurs."""
    plateau = list()
    for i in range(hauteur):
        ligne = list()
        for j in range(largeur):
            ligne.append(COULEURS[random.randint(0, len(COULEURS) - 1)])
        plateau.append(ligne)
    return plateau


def detecter_piece(plateau, ligne, colonne, piece):
    """Remplit l'ensemble piece, initialement vide, à l'aide des coordonnées
    des entrées de plateau appartenant à la même pièce que 
    plateau[ligne][colonne]."""

    if (ligne, colonne) in piece:
        return

    piece.add((ligne, colonne))

    if ligne > 0 and plateau[ligne][colonne] == plateau[ligne - 1][colonne]:
        detecter_piece(plateau, ligne - 1, colonne, piece)
    if ligne < len(plateau) - 1 and plateau[ligne][colonne] == plateau[ligne + 1][colonne]:
        detecter_piece(plateau, ligne + 1, colonne, piece)
    if colonne > 0 and plateau[ligne][colonne] == plateau[ligne][colonne - 1]:
        detecter_piece(plateau, ligne, colonne - 1, piece)
    if colonne < len(plateau[0]) - 1 and plateau[ligne][colonne] == plateau[ligne][colonne + 1]:
        detecter_piece(plateau, ligne, colonne + 1, piece)


def mettre_a_jour(plateau, piece):
    """Modifie plateau de manière à ce que les trous liés à la suppression de la
    pièce donnée fassent chuter les autres blocs. Les coordonnées renseignées
    par piece correspondent à des cases déjà à None dans plateau."""
    for ligne in range(len(plateau)):
        for colonne in range(len(plateau[ligne])):
            if (ligne, colonne) not in piece:
                continue

            i = ligne
            while i > 0:
                plateau[i][colonne] = plateau[i - 1][colonne]
                plateau[i - 1][colonne] = None
                i -= 1


def eliminer_colonnes_vides(plateau):
    """Effectue les décalages nécessaires à la suppression des colonnes
    vides."""
    colonne = len(plateau[0]) - 1
    while colonne >= 0:
        if plateau[-1][colonne] is not None:
            colonne -= 1
            continue
        for i in range(len(plateau)):
            for j in range(colonne, len(plateau[0])):
                if j + 1 < len(plateau[i]):
                    plateau[i][j] = plateau[i][j + 1]
                    plateau[i][j + 1] = None
                else:
                    plateau[i][j] = None
        colonne -= 1


def partie_finie(plateau):
    """Renvoie True si la partie est finie, c'est-à-dire si le plateau est vide
    ou si les seules pièces restantes sont de taille 1, et False sinon"""
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j] is None:
                continue
            if i > 0 and plateau[i][j] == plateau[i - 1][j]:
                return False
            if i < len(plateau) - 1 and plateau[i][j] == plateau[i + 1][j]:
                return False
            if j > 0 and plateau[i][j] == plateau[i][j - 1]:
                return False
            if j < len(plateau[0]) - 1 and plateau[i][j] == plateau[i][j + 1]:
                return False
    return True


# =============================================================================
# PARTIE A NE PAS MODIFIER ====================================================
# =============================================================================


class KlicketyGUI:
    """Interface pour le jeu Klickety."""

    def __init__(self):
        # initialisation des structures de données ----------------------------
        self.dim_plateau = (16,  # nombre de lignes du plateau
                            10)  # nombre de colonnes du plateau
        self.cote_case = 32  # la longueur du côté d'un bloc à dessiner
        self.hauteur_plateau = self.cote_case * self.dim_plateau[0]
        self.largeur_plateau = self.cote_case * self.dim_plateau[1]
        self.plateau = []

        # initialisation des éléments graphiques ------------------------------
        self.window = Tk()  # la fenêtre principale
        self.window.resizable(0, 0)  # empêcher les redimensionnements
        self.partie_haut = Frame(
            self.window, width=self.largeur_plateau,
            height=self.hauteur_plateau
        )
        self.partie_haut.pack(side=TOP)
        self.partie_bas = Frame(self.window)
        self.partie_bas.pack(side=BOTTOM)

        # le canevas affichant le plateau de jeu
        self.plateau_affiche = Canvas(self.partie_haut,
                                      width=self.largeur_plateau,
                                      height=self.hauteur_plateau)
        self.plateau_affiche.pack()
        self.plateau_affiche.bind('<ButtonPress-1>', self.clic_plateau)

        # le bouton "Réinitialiser"
        self.btn = Button(self.partie_bas, text='Réinitialiser',
                          command=self.reinitialiser_jeu)
        self.btn.pack(fill=BOTH)

        # affichage du nombre de blocs restants
        self.nb_blocs = 0
        self.nb_blocs_affiche = Canvas(self.partie_bas,
                                       width=self.largeur_plateau, height=32)
        self.nb_blocs_affiche.pack(fill=BOTH)

        self.reinitialiser_jeu()

        self.window.title('Klickety')
        self.window.mainloop()

    def rafraichir_nombre_blocs(self, piece=None):
        """Rafraîchit l'affichage du nombre de blocs restants, sur base de la
        pièce que l'on vient de retirer."""
        self.nb_blocs_affiche.delete(ALL)
        if piece is None:  # appel initial, tous les blocs sont encore présents
            self.nb_blocs = self.dim_plateau[0] * self.dim_plateau[1]

        else:  # soustraire du nombre de blocs celui de la pièce retirée
            self.nb_blocs -= len(piece)

        self.nb_blocs_affiche.create_text(
            self.largeur_plateau // 2, self.cote_case // 2,
            text="Blocs restants: " + str(self.nb_blocs), fill="black"
        )

    def rafraichir_plateau(self):
        """Redessine le plateau de jeu à afficher."""
        # tracer les blocs
        self.plateau_affiche.delete(ALL)
        couleur_fond = "black"
        for i in range(self.dim_plateau[1]):  # par défaut 10
            for j in range(self.dim_plateau[0]):  # par défaut 16
                # remarque: le canevas de tkinter interprète (i, j)
                # géométriquement (au lieu de (ligne, colonne)), d'où
                # l'inversion de coordonnées dans la ligne ci-dessous
                case = self.plateau[j][i]
                if case is not None:  # afficher le pion
                    self.plateau_affiche.create_rectangle(
                        i * self.cote_case, j * self.cote_case,
                        (i + 1) * self.cote_case, (j + 1) * self.cote_case,
                        outline=case, fill=case
                    )
                else:
                    self.plateau_affiche.create_rectangle(
                        i * self.cote_case, j * self.cote_case,
                        (i + 1) * self.cote_case, (j + 1) * self.cote_case,
                        outline=couleur_fond, fill=couleur_fond
                    )

        # tracer le contour des pièces
        # 1) tracer les séparations entre deux pièces adjacentes de
        # couleurs différentes dans la même colonne
        for i in range(0, self.dim_plateau[1]):  # par défaut 10
            for j in range(1, self.dim_plateau[0]):  # par défaut 16
                if self.plateau[j - 1][i] != self.plateau[j][i]:
                    self.plateau_affiche.create_rectangle(
                        i * self.cote_case, j * self.cote_case,
                        (i + 1) * self.cote_case, j * self.cote_case,
                        outline=couleur_fond, fill=couleur_fond, width=1
                    )

        # 2) tracer les séparations entre deux pièces adjacentes de
        # couleurs différentes dans la même ligne
        for i in range(1, self.dim_plateau[1]):  # par défaut 10
            for j in range(0, self.dim_plateau[0]):  # par défaut 16
                if self.plateau[j][i - 1] != self.plateau[j][i]:
                    self.plateau_affiche.create_rectangle(
                        i * self.cote_case, j * self.cote_case,
                        i * self.cote_case, (j + 1) * self.cote_case,
                        outline=couleur_fond, fill=couleur_fond, width=1
                    )

    def clic_plateau(self, event):
        """Récupère les coordonnées de la case sélectionnée, et joue le coup
        correspondant s'il est permis."""
        # remarque: le canevas de tkinter interprète (i, j) géométriquement
        # (au lieu de (ligne, colonne)), d'où l'inversion de coordonnées dans
        # la ligne ci-dessous
        (j, i) = (event.x // self.cote_case, event.y // self.cote_case)

        if self.plateau[i][j] is not None:
            piece = set()
            detecter_piece(self.plateau, i, j, piece)

            if len(piece) > 1:  # si la pièce est valide, on la retire
                # retirer la piece en mettant ses cases à None
                for (p, q) in piece:
                    self.plateau[p][q] = None

                # faire descendre les blocs situés au-dessus de la pièce
                mettre_a_jour(self.plateau, piece)

                # tasser le restant du plateau en supprimant les colonnes vides
                eliminer_colonnes_vides(self.plateau)

                # rafraîchir le plateau pour répercuter les modifications
                self.rafraichir_plateau()

                self.rafraichir_nombre_blocs(piece)
                if partie_finie(self.plateau):
                    self.plateau_affiche.create_text(
                        int(self.plateau_affiche.cget("width")) // 2,
                        self.cote_case // 2,
                        text="LA PARTIE EST TERMINÉE",
                        font=tkinter.font.Font(
                            family="Courier", size=12, weight=tkinter.font.BOLD
                        ),
                        fill="red"
                    )

    def reinitialiser_jeu(self):
        """Réinitialise le plateau de jeu et les scores."""
        self.reinitialiser_plateau()
        self.rafraichir_nombre_blocs()

    def reinitialiser_plateau(self):
        """Réinitialise le plateau de jeu."""
        # réinitialiser la matrice
        self.plateau = initialiser_plateau(*self.dim_plateau)

        # réinitialiser l'affichage
        self.plateau_affiche.delete(ALL)

        if self.plateau is not None:
            self.rafraichir_plateau()


if __name__ == "__main__":
    KlicketyGUI()
