def enregister_etudiant():
    """
    Permet de saisir les informations d'un étudiant et retourne un dictionnaire les contenant.
    :return: Dictionnaire des infos.
    """
    dico = {}
    dico["numero"] = input("Saisir le numéro de l'étudiant : ")
    dico["nom"] = input("Saisir le nom de l'étudiant : ")
    dico["prenom"] = input("Saisir le prénom de l'étudiant : ")
    dico["date_naissance"] = input("Saisir la date de naissance de l'étudiant : ")
    dico["note_ap1"] = input("Saisir la note obtenue en AP1 : ")
    return dico


liste = []
nb = int(input("Combien d'étudiants voulez-vous saisir ? "))

for i in range(nb):
    liste.append(enregister_etudiant())

for etud in liste:
    print("{} : {} {} {} - Note : {}".format(
        etud["numero"],
        etud["nom"],
        etud["prenom"],
        etud["date_naissance"],
        etud["note_ap1"]
    ))
