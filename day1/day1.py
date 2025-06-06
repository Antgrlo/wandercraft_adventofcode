import pandas as pd

distance = []
df = pd.read_csv("data.csv", sep=r"\s+", header=None, names=["col1", "col2"])

liste1, liste2 = sorted(df["col1"]), sorted(df["col2"])

distance = [abs(x - y) for x, y in zip(liste1, liste2)]

print(sum(distance))