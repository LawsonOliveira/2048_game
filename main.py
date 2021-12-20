import sys  
from pathlib import Path  
file = Path(__file__).resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))

from game2048.mise_en_place_du_jeu_avec_interface import *


game_play_avec_inter()
