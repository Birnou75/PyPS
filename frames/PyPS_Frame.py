# PyPS_Frame -> Fichier constituant la fenêtre principale du logiciel

# --------------------------------------------------------------------
# Importations / Initialisation de la fenêtre
# --------------------------------------------------------------------

from tkinter import *

pyps = Tk()



# --------------------------------------------------------------------
# Fonctions et variables relatifs au GUI
# --------------------------------------------------------------------

def changePaned(panedToDestroy, panedToPlace, buttonPanedName):
    panedToDestroy.place_forget()
    panedToPlace.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    headerTitle['text'] = buttonPanedName['text']

    if(panedToPlace != home):
        homeButton['command']=lambda:[changePaned(panedToPlace, panedToDestroy, homeButton)]
        homeButton.place(relx=0.017, rely=0.1, relheight=0.8, relwidth=0.1)
        chooseTools.place(relx=0.5, rely=0.05, anchor=CENTER)
        chooseTools.config(text="Paramètres")
        simulationSettings(panedToPlace, True)
    else:
        simulationSettings(panedToDestroy, False)
        chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER)
        chooseTools.config(text="Choisissez une simulation")
        homeButton.place_forget()

def simulationSettings(paned, enable):
    if(paned == penduleSimulation):
        if(enable == True):
            angle.place(relx=0.5, rely=0.25, relwidth=0.9, anchor=CENTER)
        else:
            angle.place_forget()


mainFont = "Roboto 12 bold"



# --------------------------------------------------------------------
# Construction de la fenêtre
# --------------------------------------------------------------------

# Fenêtre #
pyps.title("PyPS | Python Physics Simulator")
pyps.geometry("900x600")
# pyps.iconbitmap("pyps_logo.ico")


# En-tête #
header = Frame(pyps, bg="#232369")
header.place(relx=0, rely=0, relwidth=1, relheight=0.05)

headerTitle = Label(header, text="Accueil", bg="#232369", fg="white", font=mainFont)
headerTitle.place(relx=0.5, rely=0.5, anchor=CENTER)

homeButton = Button(header, text="Accueil", bg="#232369", fg="white", cursor="hand2", font=mainFont)


# Menu #
menu = Frame(pyps, bg="white", highlightthickness=1)
menu.place(relx=0, rely=0.05, relwidth=0.3, relheight=0.9)

tools = PanedWindow(menu, bg="#232369")
tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.65)

chooseTools = Label(tools, text="Choississez une simulation", bg="#232369", fg="white", font=mainFont)
chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER)

options = Button(menu, text="Options", bg="#232369", fg="white", cursor="hand2", font=mainFont)
options.place(relx=0.05, rely=0.74, relwidth=0.90, relheight=0.10)

creditsMenu = Button(menu, text="Histoire - Crédits", bg="#232369", fg="white", cursor="hand2", font=mainFont)
creditsMenu.place(relx=0.05, rely=0.87, relwidth=0.90, relheight=0.10)


# Principal (Choix simulations) #
main = Frame(pyps, bg="white")
main.place(relx=0.3, rely=0.05, relwidth=0.7, relheight=0.9)

home = PanedWindow(main, bg="white")
home.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

penduleButton = Button(home, text="Pendule simple", bg="#232369", fg="white", cursor="hand2", command=lambda:changePaned(home, penduleSimulation, penduleButton), font=mainFont)
penduleButton.place(relx=0.1, rely=0.1, relwidth=0.35, relheight=0.35)

penduleNButton = Button(home, text="Pendule de Newton", bg="#232369", fg="white", cursor="hand2", command=lambda:changePaned(home, penduleNSimulation, penduleNButton), font=mainFont)
penduleNButton.place(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.35)

bouleButton = Button(home, text="Chute d'une boule", bg="#232369", fg="white", cursor="hand2", command=lambda:changePaned(home, bouleSimulation, bouleButton), font=mainFont)
bouleButton.place(relx=0.1, rely=0.55, relwidth=0.35, relheight=0.35)

soonButton = Button(home, text="Bientôt..", bg="#232369", fg="white", cursor="hand2", font=mainFont)
soonButton.place(relx=0.55, rely=0.55, relwidth=0.35, relheight=0.35)


# Panel de la simulation "Pendule"
penduleSimulation = PanedWindow(main, bg="white")

angle = Scale(tools, orient="horizontal", from_=0, to=360, resolution=0.1, tickinterval=90, label='Angle (deg)', bg="#232369", fg="white", font=mainFont)

# Panel de la simulation "Pendule de Newton"
penduleNSimulation = PanedWindow(main, bg="white")

# Panel de la simulation "Boule"
bouleSimulation = PanedWindow(main, bg="white")


# Pied de page #
footer = Frame(pyps, bg="#232369")
footer.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)

footerCredits = Label(footer, text="Version 1.0 | Par Nizar & Loic", bg="#232369", fg="white", font=mainFont)
footerCredits.place(relx=0.5, rely=0.5, anchor=CENTER)


# --------------------------------------------------------------------
# Lancement de la fenêtre
# --------------------------------------------------------------------

pyps.mainloop()