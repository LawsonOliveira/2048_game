import sys  
from pathlib import Path  
file = Path(__file__).resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

# Affiche la grille sans prendre en compte le nombre de chiffres par case
def grid_to_string(grid, n):
    res=" ==="*n
    for i in range(len(grid)):
        l="|"
        for j in range(len(grid[i])):
            l+=" "+str(grid[i][j])+" |"              
        res+="\n"+l+"\n"+" ==="*n
    return res

# Donne le nombre max de chiffres par case
def long_value(grid):
    m=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if len(str(grid[i][j]))>m:             
                m=len(str(grid[i][j]))
    return m

# Affiche la grille en prenant en compte le nombre de chiffres par case (les nombres sont placés vers la droite dans chaque case)
def grid_to_string_with_size(grid,n):
    long_v=long_value(grid)
    res=(" "+"="*(long_v+2))*n
    for i in range(len(grid)):
        l="|"
        for j in range(len(grid[i])):               
            diff=long_v-len(str(grid[i][j]))
            l+=" "+" "*diff+str(grid[i][j])+" |"
        res+="\n"+l+"\n"+(" "+"="*(long_v+2))*n
    return res

# Donne le nombre max de lettres ou de chiffres correspondant au thème par case
def long_value_with_theme(grid,theme):         
    m=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if ' ' not in str(grid[i][j]):
                if len(str(theme[grid[i][j]]))>m:
                    m=len(str(theme[grid[i][j]]))
    return m


# Affiche la grille en prenant en compte le thème et la taille des cases
def grid_to_string_with_size_and_theme(grid,theme=THEMES["0"],n=4): 
    long_v=long_value_with_theme(grid,theme)
    res=(" "+"="*(long_v+2))*n
    for i in range(len(grid)):
        l="|"
        for j in range(len(grid)):
            if ' ' not in str(grid[i][j]):
                val=str(theme[grid[i][j]])
            else:
                val = ' '
            diff=long_v-len(val)
            l+=" "+" "*diff+val+" |"
        res+="\n"+l+"\n"+(" "+"="*(long_v+2))*n
    return res



