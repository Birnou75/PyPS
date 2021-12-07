# PyPS_Frame -> Fichier constituant la fenêtre principale du logiciel

# --------------------------------------------------------------------
# Importations / Initialisation de la fenêtre
# --------------------------------------------------------------------

from tkinter import *

pyps = Tk()



# --------------------------------------------------------------------
# Fonctions relatifs au GUI
# --------------------------------------------------------------------

def changePaned(panedToDestroy, panedToPlace):
    panedToDestroy.place_forget()
    panedToPlace.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    if(panedToPlace != home):
        chooseTools.place_forget()
        homeButton['command']=lambda:[changePaned(panedToPlace, panedToDestroy), chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER), homeButton.place_forget()]
        homeButton.place(relx=0.017, rely=0.1, relheight=0.8, relwidth=0.1)



# --------------------------------------------------------------------
# Construction de la fenêtre
# --------------------------------------------------------------------

# Fenêtre #
pyps.title("PyPS | Python Physics Simulator")
pyps.geometry("900x600")
# pyps.iconbitmap("pyps_logo.ico")


# En-tête #
header = Frame(pyps, bg="red")
header.place(relx=0, rely=0, relwidth=1, relheight=0.05)

headerTitle = Label(header, text="En-tête")
headerTitle.place(relx=0.5, rely=0.5, anchor=CENTER)

homeButton = Button(header, text="Accueil", cursor="hand2")


# Menu #
menu = Frame(pyps, bg="purple")
menu.place(relx=0, rely=0.05, relwidth=0.3, relheight=0.9)

tools = PanedWindow(menu, bg="grey")
tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.65)

chooseTools = Label(tools, text="Choississez une simulation")
chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER)

options = Button(menu, text="Options", cursor="hand2")
options.place(relx=0.05, rely=0.74, relwidth=0.90, relheight=0.10)

creditsMenu = Button(menu, text="Histoire - Crédits", cursor="hand2")
creditsMenu.place(relx=0.05, rely=0.87, relwidth=0.90, relheight=0.10)


# Principal (Choix simulations) #
main = Frame(pyps, bg="green")
main.place(relx=0.3, rely=0.05, relwidth=0.7, relheight=0.9)

home = PanedWindow(main, bg="black")
home.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

penduleButton = Button(home, text="Pendule simple", cursor="hand2", command=lambda:changePaned(home, penduleSimulation))
penduleButton.place(relx=0.1, rely=0.1, relwidth=0.35, relheight=0.35)

penduleNButton = Button(home, text="Pendule de Newton", cursor="hand2", command=lambda:changePaned(home, penduleNSimulation))
penduleNButton.place(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.35)

bouleButton = Button(home, text="Chute d'une boule", cursor="hand2", command=lambda:changePaned(home, bouleSimulation))
bouleButton.place(relx=0.1, rely=0.55, relwidth=0.35, relheight=0.35)

soonButton = Button(home, text="Bientôt..", cursor="hand2")
soonButton.place(relx=0.55, rely=0.55, relwidth=0.35, relheight=0.35)


# A mettre dans d'autres classes
penduleSimulation = PanedWindow(main, bg="purple")

penduleNSimulation = PanedWindow(main, bg="pink")

bouleSimulation = PanedWindow(main, bg="blue")


# Pied de page #
footer = Frame(pyps, bg="red")
footer.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)

footerCredits = Label(footer, text="Version 1.0 | Par Nizar & Loic")
footerCredits.place(relx=0.5, rely=0.5, anchor=CENTER)


# --------------------------------------------------------------------
# Lancement de la fenêtre
# --------------------------------------------------------------------

pyps.mainloop()