import sys  
from pathlib import Path  
file = Path(__file__).resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))

import tkinter as tk
THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

# Affiche la grille en prenant en compte le thème et la taille des cases(C'est utilisé pour l'interface graphique)
def grid_with_size_and_theme(grid,theme=THEMES["0"],n=4): 
    res=[]
    for i in range(len(grid)):
        res.append([' ']*n)   
    for i in range(len(grid)):
        for j in range(len(grid)):
            if ' ' not in str(grid[i][j]):
                res[i][j]=str(theme[grid[i][j]])
            else:
                res[i][j] = ' '
    return res


# Faire la première interface graphique
def graphical_grid_init(grid,theme):
    global root
    if theme=='0':
        dir_color = {'0':'#cdc1b4',' ':'#cdc1b4','2':'#eee4da','4':'#ede0c8','8':'#f2b179','16':'#f59563','32':'#f67c5f','64':'#f65e3b','128':'#edcf72','256':'#edcc61','512':'#edc850','1024':'#edc53f','2048':'#edc22e','4096':'#edc22e','8192':'#edc22e'}    
    elif theme=='1':
        dir_color = {'0':'#cdc1b4',' ':'#cdc1b4','H':'#eee4da','He':'#ede0c8','Li':'#f2b179','Be':'#f59563','B':'#f67c5f','C':'#f65e3b','N':'#edcf72','O':'#edcc61','F':'#edc850','Ne':'#edc53f','Na':'#edc22e','Mg':'#edc22e','Al':'#edc22e'}
    elif theme=='2':
        dir_color = {'0':'#cdc1b4',' ':'#cdc1b4','A':'#eee4da','B':'#ede0c8','C':'#f2b179','D':'#f59563','E':'#f67c5f','F':'#f65e3b','G':'#edcf72','H':'#edcc61','I':'#edc850','J':'#edc53f','K':'#edc22e','L':'#edc22e','M':'#edc22e'}         
    root=tk.Tk()
    root.title("2048")
    tk.Toplevel(root)
    n=len(grid)
    cnv=tk.Canvas(root,width=50*n+10,height=50*n+10,bg="ivory",bd=2)
    for i in range(n):
        for j in range(n):
            x=grid[j][i]
            if x not in [0,' ','']:
                cnv.create_rectangle(10+50*i,10+50*j,60+50*i,60+50*j,fill=dir_color[str(x)])
                cnv.create_text(35+50*i,35+50*j,fill="black",text=str(x))
            else:
                cnv.create_rectangle(10+50*i,10+50*j,60+50*i,60+50*j,fill='#cdc1b4')
    sortir = tk.Button(root,text="QUIT",activebackground = "blue",fg="red",command=quit)
    sortir.grid(row=2,column=0)
    cnv.grid(row=1,column=0)                
    return root, cnv


# Mise a jour l'interface graphique
def graphical_grid_reload(grid, cnv, theme):
    global root
    if theme=='0':
        dir_color = {'0':'#cdc1b4',' ':'#cdc1b4','2':'#eee4da','4':'#ede0c8','8':'#f2b179','16':'#f59563','32':'#f67c5f','64':'#f65e3b','128':'#edcf72','256':'#edcc61','512':'#edc850','1024':'#edc53f','2048':'#edc22e','4096':'#edc22e','8192':'#edc22e'}    
    elif theme=='1':
        dir_color = {'0':'#cdc1b4',' ':'#cdc1b4','H':'#eee4da','He':'#ede0c8','Li':'#f2b179','Be':'#f59563','B':'#f67c5f','C':'#f65e3b','N':'#edcf72','O':'#edcc61','F':'#edc850','Ne':'#edc53f','Na':'#edc22e','Mg':'#edc22e','Al':'#edc22e'}
    elif theme=='2':
        dir_color = {'0':'#cdc1b4',' ':'#cdc1b4','A':'#eee4da','B':'#ede0c8','C':'#f2b179','D':'#f59563','E':'#f67c5f','F':'#f65e3b','G':'#edcf72','H':'#edcc61','I':'#edc850','J':'#edc53f','K':'#edc22e','L':'#edc22e','M':'#edc22e'}         
    n=len(grid)
    for i in range(n):
        for j in range(n):
            x=grid[j][i]                     #On doit utiliser la matrix transpose
            if x not in [0,' ','']:
                cnv.create_rectangle(10+50*i,10+50*j,60+50*i,60+50*j,fill=dir_color[str(x)])
                cnv.create_text(35+50*i,35+50*j,fill="black",text=str(x))
            else:
                cnv.create_rectangle(10+50*i,10+50*j,60+50*i,60+50*j,fill='#cdc1b4')
    sortir = tk.Button(root,text="QUIT",activebackground = "blue",fg="red",command=quit)
    sortir.grid(row=2,column=0)
    cnv.grid(row=1,column=0) 
    
