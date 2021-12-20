import numpy as np

# Création de la grille vide au départ
def create_grid(n=4): 
    n=int(n)
    game_grid = []
    for i in range(n):
        game_grid.append([' ']*n)
    return game_grid

# Déplacements des tuiles
def move_row_left(row): #fait le déplacement élémentaire d'une ligne vers la gauche : 
                         #la tuile se déplace s'il y a des zéros, et fusion si deux caractères identiques sont côte a côte.
    l=[]                       
    m=[]                       
    for i in range(len(row)):
        if row[i] not in [0, ' ']:
            m.append(row[i])        #m est la liste des valeurs non nulles de row
    for i in range(len(m)):
        if i!=len(m)-1 and m[i]==m[i+1] :
            l.append(2*m[i])       #l est la liste des valeurs non nulles après avoir fait les sommes
            m[i+1]=0
        else:
            if m[i] not in [0,' ']:
                l.append(m[i])
    diff=len(row)-len(l)   
    return l+[0]*diff


# Fait le déplacement vers la droite, en utilisant la fonction de déplacement vers la gauche
def move_row_right(row): 
    rowrev=list(reversed(row))
    l=move_row_left(rowrev)
    l.reverse()
    return l


# Fait le déplacement de la grille selon le déplacement d associé
def move_grid(grid,d): 
    new_grid=[]
    n=len(grid)
    if d=="right": #pour un déplacement vers la droite, on fait juste le déplacement vers la droite de chaque ligne
        for row in grid:
            new_grid.append(move_row_right(row))
    elif d=="left":#idem pour le déplacement vers la gauche
        for row in grid:
            new_grid.append(move_row_left(row))
    elif d=="up": #pour un déplacement vers le haut, on transpose la matrice, et on fait le déplacement des lignes vers la gauche puis on retranspose.
        for k in range(n):
            new_grid.append([])
        for j in range(n):
            colonne=[]
            for i in range(n):
                colonne.append(grid[i][j])
            new_colonne = move_row_left(colonne)

            for i in range(n):
                new_grid[i].append(new_colonne[i])
    elif d=="down": #pareil, on transpose puis on déplace les lignes vers la droite, puis on retranspose
        for k in range(n):
            new_grid.append([])
        for j in range(n):
            colonne=[]
            for i in range(n):
                colonne.append(grid[i][j])
            new_colonne = move_row_right(colonne)

            for i in range(n):
                new_grid[i].append(new_colonne[i])
    return new_grid


# Cettte fonction est utilisé pour vérifier si la grid est totalement rempli    
def is_grid_full(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] in [' ',0]:
                return False
    return True

# Cettte fonction est utilisé pour vérifier les mouviments possibles. Elle retourne un vector de booleans [x,x,x,x].
# Les positions sont représenté de la façon suivante: ["right","left","up","down"]
def move_possible(grid):
    return [move_grid(grid,"right")!=grid,move_grid(grid,"left")!=grid,move_grid(grid,"up")!=grid,move_grid(grid,"down")!=grid]

# Cette fonction est utilisé pour vérifier s'il y aurait gameover.
# Ainsi, elle retourne un vector boolean. Les positions sont représenté de la façon suivante: ["right","left","up","down"]
def is_game_over(grid):
    return move_possible(grid)==[False]*4

# Cette fonction est utilisé pour obtenir le valeur maximale qu'il y a dans la grid.
def get_gride_tile_max(grid):
    max=0
    for line in grid:
        for i in line:
            if i!=' ' and i>max:
                max=i
    return max

#Cette fonction est utilisé pour vérifier si le joueur a gagné le jeu.
def is_game_won(grid):
    return is_game_over(grid) and get_gride_tile_max(grid)>=2048
        
