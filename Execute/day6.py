import copy

# --- Lecture du plateau de base ---
with open("Data/day6.csv", "r") as f:
    plateau_original = [list(l.strip()) for l in f]

# --- Position et direction initiales ---
caracteres_cibles = {'^', 'v', '<', '>'}
for i, ligne in enumerate(plateau_original):
    for j, c in enumerate(ligne):
        if c in caracteres_cibles:
            pos_depart = (i, j)
            dir_depart = c

dx_dy = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
redirection = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

# --- Fonction de déplacement du garde ---
def avancement(x, y, direction, plateau):
    for _ in range(2):  # max 1 rotation
        dx, dy = dx_dy[direction]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < len(plateau) and 0 <= ny < len(plateau[0])):
            return x, y, direction, True  # sortie atteinte
        if plateau[nx][ny] != '#':
            return nx, ny, direction, False  # déplacement réussi
        direction = redirection[direction]  # sinon on tourne

    # Deux directions testées : bloqué dans un coin
    return x, y, direction, False


# --- Partie 1 ---
plateau_partie1 = copy.deepcopy(plateau_original)
x, y = pos_depart
direction = dir_depart
sortie = False
plateau_partie1[x][y] = 'X'

while not sortie:
    x, y, direction, sortie = avancement(x, y, direction, plateau_partie1)
    if not sortie:
        plateau_partie1[x][y] = 'X'

nb_visites = sum(l.count('X') for l in plateau_partie1)
print("Partie 1 — Nombre de cases visitées :", nb_visites)

# --- Partie 2 ---
nb_boucles = 0
for i in range(len(plateau_original)):
    for j in range(len(plateau_original[0])):
        if (i, j) == pos_depart or plateau_original[i][j] != '.':
            continue

        plateau_test = copy.deepcopy(plateau_original)
        plateau_test[i][j] = '#'
        x, y = pos_depart
        direction = dir_depart
        chemin = set()
        sortie = False
        boucle = False

        while not sortie:
            etat = (x, y, direction)
            if etat in chemin:
                boucle = True
                break
            chemin.add(etat)
            x, y, direction, sortie = avancement(x, y, direction, plateau_test)

        if boucle:
            nb_boucles += 1

print("Partie 2 — Nombre de positions provoquant une boucle :", nb_boucles)
