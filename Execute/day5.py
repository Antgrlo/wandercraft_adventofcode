import csv

# Lecture des données
with open('Data/day5/day5.csv', 'r', encoding='utf-8') as f:
    donnees = [list(map(int, ligne)) for ligne in csv.reader(f) if ligne]

# Lecture et transformation des règles
with open('Data/day5/day5.txt', 'r') as f:
    regles = set(tuple(map(int, ligne.strip().split('|'))) for ligne in f if ligne.strip())

# Vérification
def ligne_est_valide(ligne, regles):
    for i in range(len(ligne)):
        for j in range(len(ligne)):
            if (i < j and (ligne[j], ligne[i]) in regles) or (j < i and (ligne[i], ligne[j]) in regles):
                return False
    return True

# Traitement
resultat = [ligne[len(ligne)//2] for ligne in donnees if ligne_est_valide(ligne, regles)]

# Résultat
print("Le résultat est :", sum(resultat))
