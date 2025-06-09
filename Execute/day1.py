import pandas as pd
from collections import Counter

## Part 1 

df = pd.read_csv("Data/day1.csv", sep=r"\s+", header=None, names=["col1", "col2"])

liste1, liste2 = sorted(df["col1"]), sorted(df["col2"])

distance = [abs(x - y) for x, y in zip(liste1, liste2)]

print("La distance est de : " ,sum(distance))

## Part 2 

compteur1 = Counter(liste2)
similarite = sum(x * compteur1[x] for x in liste1)

print("Score de similarité :", similarite)