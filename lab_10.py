
import numpy as np

# ==========================================
# Task 1: Créer l'espace de travail & Définir les données
# ==========================================
arr_vec = np.array([10, 20, 30, 40, 50])
mat_grid = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Tableau 1D A :", arr_vec)
print("Tableau 2D M :\n", mat_grid)


# ==========================================
# Task 2: Indexation (1D & 2D)
# ==========================================
# 2.1 Indexer un tableau 1D
item_3 = arr_vec[2]
item_end = arr_vec[-1]
print("A[2] =", item_3)
print("A[-1] =", item_end)

# 2.2 Indexer une matrice 2D
val_r1c2 = mat_grid[1, 2]
val_last = mat_grid[-1, -1]
print("M[1, 2] =", val_r1c2)
print("M[-1, -1] =", val_last)


# ==========================================
# Task 3: Slicing d'un tableau 1D
# ==========================================
part_1d = arr_vec[1:4]
print("A[1:4] =", part_1d)


# ==========================================
# Task 4: Slicing d'un tableau 2D
# ==========================================
# 4.1 Extraire un bloc M[0:2, 1:]
sub_block = mat_grid[0:2, 1:]
print("M[0:2, 1:] =\n", sub_block)

# 4.2 Récupérer une ligne complète
row_data = mat_grid[1, :]
print("Ligne 2 :", row_data)

# 4.3 Récupérer une colonne complète
col_data = mat_grid[:, 2]
print("Colonne 3 :", col_data)


# ==========================================
# Task 5: Slicing avancé & variations
# ==========================================
# 5.1 Blocs centrés
center_sub = mat_grid[0:3, 1:3]
print("Bloc central :\n", center_sub)

# 5.2 Slicing avec saut (step)
alt_cols = mat_grid[:, ::2]
print("Colonnes 0 et 2 :\n", alt_cols)


# ==========================================
# Task 6: Comprendre la vue (View)
# ==========================================
# 6.1 Créer et modifier une vue
view_data = mat_grid[0:2, 1:3]
print("Vue initiale :\n", view_data)

view_data[0, 0] = 999
print("Vue modifiée :\n", view_data)
print("M après modification via la vue :\n", mat_grid)

# 6.2 Remise à zéro
mat_grid = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])


# ==========================================
# Task 7: Sécuriser avec .copy()
# ==========================================
# 7.1 Sous-tableau indépendant
independent_copy = mat_grid[0:2, 1:3].copy()
print("Copie avant modification :\n", independent_copy)

independent_copy[0, 0] = 999
print("Copie modifiée :\n", independent_copy)
print("M restée intacte :\n", mat_grid)


# ==========================================
# Task 8: Exercices d'application guidés
# ==========================================
# Exercise 8.1 – Dernière colonne x10
mat_grid[:, -1] *= 10
print("M après multiplication de la dernière colonne :\n", mat_grid)

# Réinitialiser M
mat_grid = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Exercise 8.2 – Bloc modifié (via vue)
view_patch = mat_grid[1:, :2]
view_patch[:] = -1
print("M après bloc -1 (via vue) :\n", mat_grid)

# Réinitialiser M
mat_grid = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Exercise 8.3 – Bloc indépendant (via copie)
copy_patch = mat_grid[1:, :2].copy()
copy_patch[:] = -1
print("Bloc copy modifié :\n", copy_patch)
print("M (copie intacte) :\n", mat_grid)

# Exercise 8.4 – Vecteur 1D slicing
original_vec = arr_vec.copy()
arr_vec[1:-1] = 0
print("A modifié :", arr_vec)
arr_vec = original_vec



