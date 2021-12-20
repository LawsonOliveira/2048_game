import sys  
from pathlib import Path  
file = Path(__file__).resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))

from game2048.interface_graphique import *
from game2048.Initialisation import *
from game2048.affichage_grille import *
from game2048.grid_2048 import *
from game2048.textual_2048 import *

# Variables globales
theme = "0"
size = "0"
grid = []
cnv = None
root = None

# Cette fonction fait les mouvements de la grid sur l'interface graphique


def move_inter(dir):
    global theme
    global size
    global grid
    global cnv
    THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: " ", 2: "H", 4: "He", 8: "Li", 16: "Be",
                                                                                                                                                                                                       32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}
    # "right": 0, "left": 1, "up": 2, "down": 3
    dir_to_move = {"right": 0, "left": 1, "up": 2, "down": 3}
    # Boolean list/"right": 0, "left": 1, "up": 2, "down": 3
    move_possible_list = move_possible(grid)
    if not move_possible_list[dir_to_move[dir]]:
        print("Ce mouvement est impossible")
        return
    grid = move_grid(grid, dir)
    graphical_grid_reload(grid_with_size_and_theme(
        grid, THEMES[theme], size), cnv, theme)
    grid = grid_add_new_tile(grid)
    graphical_grid_reload(grid_with_size_and_theme(
        grid, THEMES[theme], size), cnv, theme)
    if is_game_won(grid):
        print("Vous avez gagné")
    if is_game_over(grid) and (not is_game_won(grid)):
        print("Gameover")


# Cette fonction est utilisée pour lire une touche sur le clavier
def key_pressed(event):
    if not is_game_over(grid):
        if event.keysym in ["Right", "Left", "Up", "Down"]:
            if event.keysym == 'Right':
                move_inter("right")
            elif event.keysym == 'Left':
                move_inter("left")
            elif event.keysym == 'Up':
                move_inter("up")
            elif event.keysym == 'Down':
                move_inter("down")
        else:
            print("Ce mouviment est impossible")


# Cette fonction est utilisée pour commencer le jeu avec l'interface graphique
def game_play_avec_inter():
    global grid
    global theme
    global size
    global cnv
    global root
    size = int(read_size_grid())
    theme = read_theme_grid()
    grid = init_game(size)
    root, cnv = graphical_grid_init(
        grid_with_size_and_theme(grid, THEMES[theme], size), theme)
    root.bind_all('<KeyRelease>', key_pressed)
    root.mainloop()


if __name__ == '__main__':
    game_play_avec_inter()
    exit(1)
