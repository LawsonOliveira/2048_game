#Projet des Coding Weeks de l'équipe TeamSix
 
##Description
 
Ce projet est le projet numéro 6 de la première semaine des Coding Weeks de CentraleSupélec.
 
##TeamSix
 - Jean Goepfert (jean.goepfert@student-cs.fr) étudiant en 1A à CS
 
 - Rémi FORASETTO : (remi.forasetto@student-cs.fr) étudiant en 1A à CS
 
- Gweltaz Pocher : (gweltaz.pocher@student-cs.fr) étudiant en 1A à CS
 
- Lawson Oliveira Lima (lawson.oliveira@student-cs.fr): étudiant en 1A à CS
 
- Benjamin Boutier : (benjamin.boutier@student-cs.fr) étudiant en 1A à CS 
 
###################################################################################################################
Projet : codage du jeu 2048
 
But du jeu : Fusionner des tuiles dont les valeurs sont des puissances de deux dans une grille n x n , afin d'obtenir une tuile 2048. 
 
Avancée du projet : Nous avons créé deux versions du jeu, un MVP qui se joue depuis le terminal, et une version avec interface graphique Tkinter, qui peut se jouer avec les flèches du clavier.
 
Test de couverture: Le test de couverture est dans l'archive game2048/index.html 
Tous les test sont ok.
##################################################################################################################
 
Utilisation du MVP : Se placer dans le fichier game2048/mise_en_place_du_jeu.py, et l'exécuter.
 
Vous aurez le choix entre le mode par défaut (chiffres), le mode "chimique" (avec des éléments du tableau périodique), et le mode "alphabet". Pour jouer, suivez les instructions données dans le terminal.
Les dépacements se font en entrant d,g,h,b qui signifient respectivement droite, gauche, haut et bas.
 
##################################################################################################################
 
Utilisation de la deuxième version avec interface graphique : 
- Se placer dans main.py et l'exécuter.
- Suivre les instructions du terminal pour choisir la taille de la grille et le mode de jeu (normal, chimique ou alphabet)
- Une fenêtre s'ouvre normalement sur le bureau, avec la grille de départ.
- Pour jouer, il suffit simplement d'utiliser les flèches du clavier suivant la direction dans laquelle vous souhaitez déplacer les tuiles. Pensez bien à attendre que le mouvement précédent soit terminé pour lancer le suivant (le calcul peut prendre une demi-seconde en fin de partie)
- le score s'affiche après chaque coup dans le terminal
- Appuyez simplement sur le bouton "Quit" pour quitter la partie
 
##################################################################################################################
# 2048_game
