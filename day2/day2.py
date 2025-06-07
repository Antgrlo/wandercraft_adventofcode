import os

# Ouverture des listes
groupes = []
dossier_script = os.path.dirname(__file__)
chemin_fichier = os.path.join(dossier_script, "data.csv")
with open(chemin_fichier, "r") as f:
    groupes = [[int(x) for x in ligne.strip().split()] for ligne in f if ligne.strip()]

"""
for groupe in groupes:
    print(groupe)
"""

# Partie 1

nbr_de_safe = sum(
    1 for rapport in groupes
    if (
        all(rapport[i+1] > rapport[i] for i in range(len(rapport)-1)) or
        all(rapport[i+1] < rapport[i] for i in range(len(rapport)-1))
    )
    and all(1 <= abs(rapport[i+1] - rapport[i]) <= 3 for i in range(len(rapport)-1))
)

print ("le nombre de raport safe est de ",nbr_de_safe)