import sys  
from pathlib import Path  
file = Path(__file__).resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))

import random as rd
from game2048.grid_2048 import *

# Cette fonction crée une chiffre de manière aleatoire. P(2)=90% et P(4)=10%
def get_value_new_tile():
    return rd.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

# Cette fonction crée un list lequel reçoit les eléments de game_grid. Le vide est remplacé par le chiffre 0
def get_all_tiles(game_grid):
    tiles = []
    for line in game_grid:
        for i in line:
            if i == ' ':
                tiles.append(0)
            else:
                tiles.append(i)
    return tiles

# Cette fonction vérifie tous les positions de tiles vides
def get_empty_tiles_positions(game_grid):
    tiles = []
    for i in range(0, len(game_grid)):
        for j in range(0, len(game_grid)):
            if game_grid[i][j] in [0, ' ']:
                tiles.append((i, j))
    return tiles

# Cette fonction génère de façon aleatoire une nouvelle position
def get_new_position(game_grid):
    x, y = rd.choice(get_empty_tiles_positions(game_grid))
    return x, y

# Cette fonction modifie ' ' de la tile afin de remplacer par 0
def grid_get_value(game_grid, x, y):
    value = game_grid[x][y]
    if value == ' ':
        value = 0
    return value

# Cette fonction met un nouveau chiffre sur une position de game_grid 
def grid_add_new_tile(game_grid):
    x, y = get_new_position(game_grid)
    game_grid[x][y] = get_value_new_tile()
    return game_grid

# Cette fonction commencer le jeu
def init_game(m=4):
    game_grid = create_grid(m)
    game_grid = grid_add_new_tile(game_grid)
    game_grid = grid_add_new_tile(game_grid)
    return game_grid

