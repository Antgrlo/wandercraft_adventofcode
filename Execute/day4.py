with open("Data/day4.txt", "r") as f:
    lignes = [line.strip() for line in f if line.strip()] #liste des lignes

grille = [list(ligne) for ligne in lignes]

# Partie 1

# Les 8 directions : (delta_x, delta_y)
directions = [
    (0, 1),   # ➡ droite
    (0, -1),  # ⬅ gauche
    (1, 0),   # ⬇ bas
    (-1, 0),  # ⬆ haut
    (1, 1),   # ↘ diagonale bas-droite
    (-1, -1), # ↖ diagonale haut-gauche
    (1, -1),  # ↙ diagonale bas-gauche
    (-1, 1),  # ↗ diagonale haut-droite
]

mot = "XMAS"

def trouver_xmas(grille):
    lignes = len(grille)
    colonnes = len(grille[0])
    total = 0

    for i in range(lignes):
        for j in range(colonnes):
            for dx, dy in directions:
                x, y = i, j
                trouvé = True
                for k in range(len(mot)):
                    nx, ny = x + dx * k, y + dy * k
                    if not (0 <= nx < lignes and 0 <= ny < colonnes):
                        trouvé = False
                        break
                    if grille[nx][ny] != mot[k]:
                        trouvé = False
                        break
                if trouvé:
                    total += 1
    return total

print("Nombre total de XMAS trouvés :", trouver_xmas(grille))

# Partie 2

def est_mas(seq):
    return seq == ['M', 'A', 'S'] or seq == ['S', 'A', 'M']

def compter_xmas(grille):
    lignes = len(grille)
    colonnes = len(grille[0])
    total = 0

    for i in range(1, lignes - 1):
        for j in range(1, colonnes - 1):
            # Extraire les deux diagonales du carré 3x3 centré sur (i, j)
            diagonale1 = [grille[i-1][j-1], grille[i][j], grille[i+1][j+1]]  # ↘
            diagonale2 = [grille[i-1][j+1], grille[i][j], grille[i+1][j-1]]  # ↙

            if est_mas(diagonale1) and est_mas(diagonale2):
                total += 1

    return total

print("Nombre de X-MAS trouvés :", compter_xmas(grille))