import os
import re

dossier_script = os.path.dirname(__file__)
chemin_fichier = os.path.join(dossier_script, "data.txt")

with open(chemin_fichier, "r") as f:
    data = f.read()

# Partie 1

filtré_mul = re.findall(r"mul\((\d+),(\d+)\)", data)
#print(filtré_mul)

produits = [int(x) * int(y) for x, y in filtré_mul]

somme_totale = sum(produits)

print("La somme totale des produits est :", somme_totale)

# Partie 2*

filtre_complet = re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", data)
#print(filtre_complet)

somme_totale = 0
enabled = True

for instructions in filtre_complet:
    if instructions.group() == "do()":
        enabled = True
    elif instructions.group() == "don't()":
        enabled = False
    else:
        if enabled:
            x, y = instructions.groups()
            somme_totale += int(x) * int(y)

print("La somme totale des produits avec les nouvel instructions :", somme_totale)