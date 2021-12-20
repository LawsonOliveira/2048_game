import sys  
from pathlib import Path  
file = Path(__file__).resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))

import random as rd
from Initialisation import *
from game2048.MVP.affichage_grille import *
from game2048.grid_2048 import *
from game2048.textual_2048 import *


# Cette fonction joue le jeu de manière aleatoire
def random_play():
    grid=init_game()
    k=0
    dir_to_move={"right": 0, "left": 1, "up": 2, "down": 3 }
    print(grid_to_string_with_size_and_theme(grid))
    while not is_game_over(grid):
        k=k+1
        dir=rd.choice(["down","up","right","left"])
        print("Move: ",dir)
        move_possible_list=move_possible(grid)  #Boolean list[1,0,0,1]
        while not move_possible_list[dir_to_move[dir]]:
            print("Ce moviment est impossible")
            dir=rd.choice(["down","up","right","left"])
        grid=move_grid(grid,dir)
        print("Phase:: ",k,"\n",grid_to_string_with_size_and_theme(grid),"\n\n\n\n")
        grid=grid_add_new_tile(grid)
        print("Phase: ",k,"\n",grid_to_string_with_size_and_theme(grid),"\n\n\n\n")
        if is_game_won(grid):
            print("Vous avez gagné")
            return
    print("Game over")


#Etape 2
#déjà fait dans textual

# Cette fonction est utilisée pour commencer le jeu sans l'interface grapique 
def game_play():
    THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}
    size=int(read_size_grid())
    theme=read_theme_grid()
    grid=init_game(size)
    k=0
    dir_to_move={"right": 0, "left": 1, "up": 2, "down": 3 }#"right": 0, "left": 1, "up": 2, "down": 3 
    dir_input={"d": "right", "g": "left", "h": "up", "b": "down" }#"right": 0, "left": 1, "up": 2, "down": 3 
    print(grid_to_string_with_size_and_theme(grid,THEMES[theme],size))
    while not is_game_over(grid):
        k=k+1
        dir=read_player_command()
        move_possible_list=move_possible(grid)  #Boolean list
        while not move_possible_list[dir_to_move[dir_input[dir]]]:
            print("Ce mouvement est impossible")
            dir=read_player_command()
        grid=move_grid(grid,dir_input[dir])
        print("Phase: ",k,"\n",grid_to_string_with_size_and_theme(grid,THEMES[theme],size),"\n\n\n\n")
        grid=grid_add_new_tile(grid)
        print("Phase: ",k,"\n",grid_to_string_with_size_and_theme(grid,THEMES[theme],size),"\n\n\n\n")
        if is_game_won(grid):
            print("Vous avez gagné")
            return
    print("Game over")


if __name__ == '__main__':
    game_play()
    random_play()
    exit(1)





