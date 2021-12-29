# PyPS_Frame -> Fichier constituant la fenêtre principale du logiciel

# --------------------------------------------------------------------
# Importations / Initialisation de la fenêtre
# --------------------------------------------------------------------

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
            toolsScrollBar.configure(command=toolsButtons.yview)
            toolsButtons.configure(yscrollcommand=toolsScrollBar.set)
            toolsButtons.place(rely=0.12, relx=0.06, relwidth=0.82, relheight=0.8)
            toolsScrollBar.pack(side=RIGHT, fill=Y)

            """angle.pack(relx=0.05, rely=0.05, relwidth=0.9)
            angle2.place(relx=0.05, rely=0.45, relwidth=0.9)
            angle3.place(relx=0.05, rely=0.85, relwidth=0.9)
            angle4.place(relx=0.05, rely=1.25, relwidth=0.9)"""
            angle.pack(fill=X)
            angle2.pack(fill=X)
            angle3.pack(fill=X)
            angle4.pack(fill=X)
            
        else:
            toolsScrollBar.pack_forget()
            toolsButtons.place_forget()
            angle.pack_forget()
            angle2.pack_forget()
            angle3.pack_forget()
            angle4.pack_forget()

def penduleGraph():
	

	plt.show()
	


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
menu = Frame(pyps, bg="white", highlightthickness=2)
menu.place(relx=0, rely=0.05, relwidth=0.3, relheight=0.9)

tools = Frame(menu, bg="#232369")
tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.65)

chooseTools = Label(tools, text="Choississez une simulation", bg="#232369", fg="white", font=mainFont)
chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER)

options = Button(menu, text="Options", bg="#232369", fg="white", cursor="hand2", font=mainFont)
options.place(relx=0.05, rely=0.74, relwidth=0.90, relheight=0.10)

creditsMenu = Button(menu, text="Histoire - Credits", bg="#232369", fg="white", cursor="hand2", font=mainFont)
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

toolsButtons = Canvas(tools, bg="#232369")
toolsScrollBar = Scrollbar(tools, orient=VERTICAL)

angle = Scale(toolsButtons, orient="horizontal", from_=0, to=360, resolution=1, tickinterval=180, label='Angle (deg)', bg="#232369", fg="white", font=mainFont)
angle2 = Scale(toolsButtons, orient="horizontal", from_=0, to=360, resolution=1, tickinterval=180, label='Angle (deg)', bg="#232369", fg="white", font=mainFont)
angle3 = Scale(toolsButtons, orient="horizontal", from_=0, to=360, resolution=1, tickinterval=180, label='Angle (deg)', bg="#232369", fg="white", font=mainFont)
angle4 = Scale(toolsButtons, orient="horizontal", from_=0, to=360, resolution=1, tickinterval=180, label='Angle (deg)', bg="#232369", fg="white", font=mainFont)
angle5 = Scale(toolsButtons, orient="horizontal", from_=0, to=360, resolution=1, tickinterval=180, label='Angle (deg)', bg="#232369", fg="white", font=mainFont)

infosPendule = Label(penduleSimulation, text="Vitesse : 0 m/s \n Temps restant : 0h, 0m, 0s", bg="#232369", fg="white", font=mainFont)
infosPendule.place(relx=0.6, rely=0.9, relwidth=0.4, relheight=0.09)

	# Animation, partie majeure
animationPendule = Canvas(penduleSimulation, bg="#33fff3")
animationPendule.place(relx=0.025, rely=0.05, relheight=0.8, relwidth=0.95)

graphButton = Button(animationPendule, text="Lancer animation\n Version Test", bg="#232369", fg="white", cursor="hand2", command=lambda:penduleGraph(), font=mainFont)
graphButton.place(relx=0.5, rely=0.5, anchor=CENTER)


# Panel de la simulation "Pendule de Newton"
penduleNSimulation = PanedWindow(main, bg="white")

# Panel de la simulation "Boule"
bouleSimulation = PanedWindow(main, bg="white")


# Pied de page #
footer = Frame(pyps, bg="#232369")
footer.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)

footerCredits = Label(footer, text="Version 1.0 | Par Nizar & Loic", bg="#232369", fg="white", font=mainFont)
footerCredits.place(relx=0.5, rely=0.5, anchor=CENTER)


# Logo #




# --------------------------------------------------------------------
# Lancement de la fenêtre
# --------------------------------------------------------------------

pyps.mainloop()
