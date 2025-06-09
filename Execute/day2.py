# Ouverture des listes
groupes = []

with open("Data/day2.csv", "r") as f:
    groupes = [[int(x) for x in ligne.strip().split()] for ligne in f if ligne.strip()]

"""
for groupe in groupes:
    print(groupe)
"""

# Partie 1

def is_safe(rapport):
    return (
        (
            all(rapport[i+1] > rapport[i] for i in range(len(rapport) - 1)) or
            all(rapport[i+1] < rapport[i] for i in range(len(rapport) - 1))
        )
        and all((1 <= abs(rapport[i+1] - rapport[i]) <= 3) for i in range(len(rapport) - 1))
    )


nbr_de_safe = sum(
    1 for rapport in groupes
    if (
        is_safe(rapport)
    )
)

print ("le nombre de raport safe est de ",nbr_de_safe)

# Partie 2

def is_safe_suppr(rapport):
    if is_safe(rapport):
        return True

    for i in range(len(rapport)):
        copie = rapport[:i] + rapport[i+1:]  # crée une nouvelle liste sans l’élément à l’index i
        if is_safe(copie):
            return True

    return False

nbr_real_safe = sum(1 for rapport in groupes if is_safe_suppr(rapport))
print("Le nombre de rapports safe en prenant compte le problème est :", nbr_real_safe)
