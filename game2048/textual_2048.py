# Demande à l'utilisateur de rentrer une commande de jeu, répète la question si la commande n'est pas valide
def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)): ")
    while move not in ['g','d','h','b']:
        move = input("Entrez une commande valide(g (gauche), d (droite), h (haut), b (bas)): ")

    return move

# Demande à l'utilisateur de rentrer la taille de la grille de jeu
def read_size_grid():
    size = input("Entrez la taille de la grille (Un entier strictement supérieur à 1): ")
    while size not in [str(i) for i in range(2,50)]:
        size = input("Entrez la taille de la grille (Un entier strictement supérieur à 1): ")
    return(size)
    
# Demande à l'utilisateur de choisir un thème pour la grille de jeu
def read_theme_grid():
    theme = input("Entrez le thème voulu (0 (Default), 1 (Chemistry), 2 (Alphabet)): ")
    while theme not in ['0','1','2']:
        theme = input("Entrez le thème voulu (0 (Default), 1 (Chemistry), 2 (Alphabet)): ")
    return(theme)


'''
if __name__ == '__main__':
    game_play()
    random_play()
    exit(1)
'''

