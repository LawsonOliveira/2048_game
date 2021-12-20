import sys  
from pathlib import Path  
file = Path(__file__).resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))

import argparse
from game2048.Initialisation import *
from game2048.MVP.affichage_grille import *
from game2048.grid_2048 import *
from game2048.textual_2048 import *

list=[]
for i in range(2,51):
    list.append(i)

parser=argparse.ArgumentParser(description="Jeu 2048")
parser.add_argument("size", type=int,help="Taile de la grid",default=4, choices=list)
parser.add_argument("theme", type=str,help="Theme choisi",default='0',choices=['0','1','2'])
args=parser.parse_args()
arg=parser.parse_args()


def game_play(size,theme):
    THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}  
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


game_play(arg.size,arg.theme)
