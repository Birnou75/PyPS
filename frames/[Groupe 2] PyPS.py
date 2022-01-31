# PyPS_Frame -> Fichier constituant la fenêtre principale du logiciel

# --------------------------------------------------------------------
# Importations / Initialisation de la fenêtre
# --------------------------------------------------------------------
import webbrowser

from tkinter import *
import tkinter.filedialog

from turtle import *

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

from math import *

pyps = Tk()
pyps.minsize(width=900, height=625)


# --------------------------------------------------------------------
# Fonctions et variables relatifs au GUI
# --------------------------------------------------------------------

# Listes d'élements en fonction de leurs attributs
BgFgElements = []
FgBgElements = []
BgElements = []
FgElements = []
scrollElements = []
borderElements = []
# Ces listes sont complétées au fur et à mesure de la création des éléments de l'application et sont appelées dans les fonctions qui modifient la couleur de l'application


#------------Fonctions générales
#   Fonction de changement de fenêtre
def changePaned(panedToDestroy, panedToPlace, buttonPanedName):
    panedToDestroy.place_forget() #Supprime la fenêtre actuelle
    panedToPlace.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98) # Initialise les dimensions de la fenêtre à ouvrir
    headerTitle['text'] = buttonPanedName['text']

    if(panedToPlace != home):
# Si on sort du menu principal :
        homeButton['command']=lambda:[changePaned(panedToPlace, panedToDestroy, homeButton)]
        homeButton.place(relx=0.017, rely=0.1, relheight=0.8, relwidth=0.1) # Place un bouton "Accueil" pour retourner au menu
        chooseTools.place(relx=0.5, rely=0.05, anchor=CENTER)
        chooseTools.config(text="Paramètres") # Place un panel paramètre qui servira à paramétrer les simulations
        options.place_forget() # Supprime le bouton "options"
        creditsMenu.place_forget() # Supprime le bouton "crédits"
        tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.9)
        simulationSettings(panedToPlace, True)
    else:
# Si on revient dans le menu principal :
        simulationSettings(panedToDestroy, False)
        chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER)
        chooseTools.config(text="Choisissez une simulation") #Fais appararaître la fenêtre indicative "Choisissez une simulation"
        homeButton.place_forget() # Fait disparaître le bouton "Accueil"
        tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.65)
        options.place(relx=0.05, rely=0.74, relwidth=0.90, relheight=0.10) # Place le bouton "Options"
        creditsMenu.place(relx=0.05, rely=0.87, relwidth=0.90, relheight=0.10) # Place le bouton "Histoire - Crédits"
    if(panedToPlace == optionPaned or panedToPlace == historyPaned):
# Si on accède à la partie "Options" ou à la partie "Histoire - Crédits":
        tools.place_forget() # Supprime le panel "Paramètres" pour libérer de l'espace
        panedToPlace.place_forget()
        panedToPlace.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.86)

def simulationSettings(paned, enable):
# Initialise le panel "Paramètres" de chaque simulation
    # Si on ouvre le panel "Pendule simple", charge les formulaires du pendule simple qui récupèrent les valeurs données par l'utilisateur à gauche dans le panel "Paramètres"
    if(paned == penduleSimulation):
        if(enable == True):
            toolsButtons.place(rely=0.12, relx=0.087, relwidth=0.82, relheight=0.8)
            anglePendule.pack(fill=X)
            threadPendule.pack(fill=X)
            gravityPendule.pack(fill=X)
            timePendule.pack(fill=X)
        else:
            toolsButtons.place_forget()
            anglePendule.pack_forget()
            threadPendule.pack_forget()
            gravityPendule.pack_forget()
            timePendule.pack_forget()
    # Si on ouvre le panel "Chute d'une boule", charge les formulaires de la boule qui récupèrent les valeurs données par l'utilisateur à gauche dans le panel "Paramètres"
    if(paned == bouleSimulation):
        if(enable == True):
            toolsButtons.place(rely=0.12, relx=0.087, relwidth=0.82, relheight=0.8)
            hauteurBouleLabel.pack(pady=7)
            hauteurBoule.pack(fill=X)
            rayonBouleLabel.pack(pady=7)
            rayonBoule.pack(fill=X)
            masseBouleLabel.pack(pady=7)
            masseBoule.pack(fill=X)
            startBouleSimulation.place(relx=0.07, rely=0.75, relwidth=0.86, relheight=0.2)
        else:
            toolsButtons.place_forget()
            hauteurBoule.pack_forget()
            hauteurBouleLabel.pack_forget()
            rayonBoule.pack_forget()
            rayonBouleLabel.pack_forget()
            masseBoule.pack_forget()
            masseBouleLabel.pack_forget()
            errorBouleLabel.place_forget()
            startBouleSimulation.place_forget()


# Fonctions relatives au "Pendule simple"
# Les coordonnées sont calculées à l'aide d'une base polaire (notions de physique)

# Fonction qui prend en argument la longueur du fil et le nouvel angle ( calculé en fonction du temps dans une autre fonction ) pour calculer les coordonnées du pendule et créer une image du pendule à la position calculée
# Cette fonction sera utilisée lors de l'animation en créant plusieurs images à chaque instant t
def updatePenduleAnimation(thetaMaxUpdate, rUpdate, gUpdate, thetaUpdate):
	pendulePlot.clear()

	ax.spines['left'].set_position('zero')
	ax.spines['bottom'].set_position('zero')
	pendulePlot.set_xlim([-3.5, 3.5])
	pendulePlot.set_ylim([-3.5, 3.5])
	pendulePlot.axis("off") # Cache le graphe avec les abcisses et les ordonnées

	pendulePlot.scatter([0, -3.5, 3.5], [0, 0, 0], s=0)


    # Dessine le support du fil en noir, le fil en rouge et la boule en orange
	pendulePlot.plot([-3.5, 3.5], [0, 0], c="black") 
	pendulePlot.scatter(rUpdate*cos(thetaUpdate-pi/2), rUpdate*sin(thetaUpdate-pi/2), s=500, c="orange", zorder=2)
	pendulePlot.plot([0, rUpdate*cos(thetaUpdate-pi/2)], [0, rUpdate*sin(thetaUpdate-pi/2)], c="red", zorder=1)

	animationPenduleCanvas.draw()

# Lance l'animation du pendule en prenant en argument la gravité et la durée de la simulation
def penduleAnimation(g, t):
	periode = 2*pi*sqrt(r/g)
	infosPendule['text'] = "Période : {} s\n Temps restant : 0h, 0m, 0s".format(round(periode, 1))
	h = 0.1 # Constante arbitraire permettant de définir la fréquence à laquelle les "images" du pendule apparait à chaque fois
	omega = sqrt(g/r)
	for i in range(0, int(t/h)):
		thetaAnim = (thetaMax)*sin(omega*i*h + pi/2) # Calcul de l'angle theta à l'instant t en fonction de l'angle de départ (et donc du temps)
		updatePenduleAnimation(thetaMax, r, g, thetaAnim) # Création de l'image du pendule à sa nouvelle position
		plt.pause(h/1.6) # Le 2.2 est une fonction arbitraire qui synchronise le temps réelle et celui de la simulation


# Les 4 fonctions qui suivent modifient les variables en lien direct avec le mouvement du pendule
# Elle sont appelées lorsque l'utilisateur fait varier la barre de défilement et permet donc de récupérer une nouvelle valeur
# Les coordonnées sont recalculées et le pendule est replacé avec la fonction updatePenduleAnimation
def changeR(newR):
	global r
	r = float(newR)
	updatePenduleAnimation(thetaMax, r, g, theta)

def changeThetaMax(newThetaMax):
	global thetaMax
	global theta
	thetaMax = (float(newThetaMax)*pi)/180
	theta = (thetaMax)*sin(pi/2)
	updatePenduleAnimation(thetaMax, r, g, theta)

def changeG(newG):
	global g
	g = float(newG)

def changeT(newT):
	global t
	t = float(newT)

# Fonctions relatives à la boule

def startBouleSimulationFunc():
	# Initialisation des Paramètres
		# Le programme récupère les valeurs entrées sur l'interface par l'utilisateur
		# Il catch l'exception et vérifie que les nombres saisis sont bien des floattants ou des entiers
	try:
		h = float(hauteurBoule.get())
		r = float(rayonBoule.get())
		m = float(masseBoule.get())*1000
	except Exception as e:
		errorBouleLabel.place(rely=0.6, relx=0.07, relwidth=0.9, relheight=0.1)
		print("[Erreur] [Simulation boule] Veuillez rentrer un entier ou un nombre floattant. Pour séparer la partie entière de la partie décimale, utilisez un point.")
		return
	
	errorBouleLabel.place_forget()
	
	startBouleSimulation.config(state=DISABLED)

	# Constantes
	g = 9.8
	pt = 2.9*10**3 # Densité du sol
	# Paramétrage de l'échelle
	echelle = h/(200) # Avancer de 1 sur l'écran correspond à un déplacement de h/200 mètres dans la réalité
	
	# Calcul de valeurs numériques
	tmax = sqrt(2*h/g) # Durée théorique de la chute
	Vmax = sqrt(2*g*h) # Vitesse max
	Emax = (1/2)*m*(Vmax**2) # Energie mécanique, Energie au moment de l'impact
	
	p = m/(4*pi*r**3/3) # Calcul de la masse volumique de la boule
	d = 2*r
	
	# Calcul du diamètre du cratère
	D = 1.161*(p/pt)**(1/3)*d**0.78*Vmax**0.44*g**-0.22
	
	# Creation de tableaux pour réaliser des boucles d'animation
		# Le premier tableau contient plusieurs instants t (en s) allant de 0 jusqu'à l'instant tmax où la boule touche le sol. Le pas entre les instants est de 40 ms, permettant de générer 25 images par seconde lors de l'animation.
	t = np.arange(0,tmax+0.04,0.04)
	a = (D/2)/echelle # Calcul du paramètre a qui est le rayon du cratère mis à l'échelle
	
	# Création d'un tableau pour animer l'évolution de la boule qui s'enfonce dans le sol jusqu'au fond du cratère, c'est-à-dire à a mètres
	# Si le cratère est petit par rapport à la boule, crée un petit tableau qui sera vite parcouru, permettant de ne pas avoir une chute trop lente pour une petite distance
	if D/(2*r) < 1:
		R = np.linspace(0,a,10)
	# Sinon, crée un tableau plus grand
	else:
		 R = np.linspace(0,a,100 )
	# Le tableau sera parcouru dans une boucle qui dessine l'animation
	
	# Légende
		# Dessine les informations de la boule en bas de l'écran
	turtleL = RawTurtle(infoBouleCanvas) # Initialise un crayon qui dessine dans la fenêtre de la légende
	turtleL.dot(1000, "white")
	turtleL.ht()
	x,y = 0,0
	turtleL.up()
	turtleL.setpos(-100, -5)
	turtleL.down()
	turtleL.forward(10) # Dessine une ligne de 10 pixels qui représente l'echelle
	turtleL.up()
	turtleL.setpos(-85,y-12.5)
	turtleL.down()
	turtleL.write("  :  {}m".format(10*echelle)) # Affiche l'echelle : 10 pixels dans la simulations valent un certain nombre de mètres dans la vraie vie
	turtleL.up()
	turtleL.setpos(-85,-25)
	turtleL.down()
	turtleL.write("Vitesse max = {}m/s".format(round(Vmax,2)))
	turtleL.up()
	turtleL.setpos(-85,y-35)
	turtleL.down()
	turtleL.write("Energie mécanique = {}J".format(round(Emax,2)))
	turtleL.up()
	turtleL.setpos(50,y-12.5)
	turtleL.down()
	turtleL.write("Durée théorique de la chute = {}s".format(round(tmax,2)))
	turtleL.up()
	turtleL.setpos(50,y-25)
	turtleL.down()
	turtleL.write("Diamètre du cratère = {}m".format(round(D,2)))
	# Animation de la chute
		# Paramétrage des crayons
	turtleBoule = TurtleScreen(animationBouleCanvas) # Transforme le Canvas en objet TurtleScreen
	x,y = turtleBoule.window_width(), turtleBoule.window_height() # Initiatialison de crayons pour dessiner dans le Canvas
	boule = RawTurtle(turtleBoule) # Crayon de la boule
	# Les crayons explosions vont effacer le sol au fur et à mesure de l'agrandissement du cratère
	explosion1 = RawTurtle(turtleBoule)
	explosion2 = RawTurtle(turtleBoule)
	explosion3 = RawTurtle(turtleBoule)
	cratere = RawTurtle(turtleBoule) # Crayon du cratère
	soufle = RawTurtle(turtleBoule) # Crayon du soufle généré à l'impact
	explosion1.ht()
	explosion2.ht()
	explosion3.ht()
	cratere.ht()
	soufle.ht()
	# Les crayons sont rendus invisibles sauf la boule
	# La vitesse des crayons est mise au maximum pour avoir une animation fluide
	boule.speed(0)
	explosion1.speed(0)
	explosion2.speed(0)
	explosion3.speed(0)
	cratere.speed(0)
	soufle.speed(0)
	# Les crayons sont utilisés comme effaceur : ils sont donc mis en couleur blanche et effaceront les dessins précédents en repassant dessus
	explosion1.pencolor("white")
	explosion2.pencolor("white")
	explosion3.pencolor("white")
	
	soufle.pencolor("blue") #Le soufle de l'explosion est affiché en blue
	
	# Création de la boule
	if r/h <= 1/200: # Si la boule est trop petite par rapport à l'echelle, fixe son rayon à 1
		b = 1
	else: # Sinon, la boule est mise à l'echelle
		b = (r/h)*(200)
	# Création d'un cercle plein qui servira à représenter la boule dans l'animation
	boule.begin_poly()
	boule.circle(b)
	boule.end_poly()
	poly = boule.get_poly()
	turtleBoule.register_shape("boule",poly) # Le crayon "boule" prend l'apparence de la boule pour l'animation
	boule.shape("boule")
	boule.clear()
	# Création du décor
	boule.up()
	boule.setpos(-x,-200)
	boule.down()
	boule.setpos(x,0-200)
	boule.up()
	
	# Chute de la boule
	boule.setpos(100,0)
	turtleBoule.delay(30) # Mise en place d'un délai d'environ 40ms en chaque imaage
	for i in t:
		# Le coefficient de -200 varie de 0 à 1, faisant descendre la boule de y = 0 jusqu'à y = -200 au cours de l'animation
		# Le membre +/- b dans les coordonnées permet de centrer la boule
		boule.setpos(-b+100,(-200)*(((1/2)*g*(i**2))/h)+b)
	turtleBoule.delay(1) 
	for i in R:
		cratere.clear()
		soufle.up()
		cratere.up()
		soufle.setpos(3*i+100,0-200)
		soufle.setheading(90)
		cratere.setpos(i+100,0-200)
		cratere.setheading(90)
		soufle.down()
		cratere.down()
		soufle.circle(3*i,180) # Dessin du soufle
		cratere.circle(i,-180) # Dessin du cratère
		# Effaceurs qui cachent le sol qui s'efface au fur et à mesure de l'ouverture du cratère
		explosion1.goto(i+100,0-200)
		explosion2.goto(-i+100,0-200)
		explosion3.goto(i+100,0-200)
		explosion3.goto(-i+100,0-200)
		boule.setpos(-b+100,b-i-200)
		soufle.clear()
	startBouleSimulation.config(state=NORMAL)

# Fonctions relatifs aux "Options"
    # Couleurs
mainColorStr = "#232369"
secondaryColorStr = "white"

# Fonction qui modifie la couleur de l'application
def changeColorElements(colorPlace, color):
    if(colorPlace == 1): # Si l'utilisateur change la couleur principale
        global mainColorStr
        mainColorStr = color
        # Parcours les listes des éléments ayant une couleur principale et change leur couleur principale
        for i in BgFgElements:
            i['bg'] = mainColorStr
        for i in FgBgElements:
            i['fg'] = mainColorStr
        for i in scrollElements:
            i['bg'] = mainColorStr
        for i in BgElements:
            i['bg'] = mainColorStr
    elif(colorPlace == 2): # Si l'utilisateur change la couleur secondaire
        global secondaryColorStr
        secondaryColorStr = color
        # Parcours les listes des éléments ayant une couleur principale et change leur couleur principale
        for i in BgFgElements:
            i['fg'] = secondaryColorStr
        for i in FgBgElements:
            i['bg'] = secondaryColorStr
        for i in scrollElements:
            i['troughcolor'] = secondaryColorStr
            if(isinstance(i, Scale)):
                i['fg'] = secondaryColorStr
        for i in FgElements:
            i['bg'] = secondaryColorStr
        for i in borderElements:
            i['highlightbackground'] = secondaryColorStr
            i['highlightcolor'] = secondaryColorStr

# Fonction qui convertit les triplets de couleurs en base 10 en héxadécimal
def convertRGBtoHex(red, green, blue):
    redHex = format(red, "02x")
    greenHex = format(green, "02x")
    blueHex = format(blue, "02x")
    hexColor = ("#" + redHex + greenHex + blueHex)
    return hexColor

# Fonction qui appelle la fonction changeColorElements pour changer la couleur de l'application à partir d'un triplet de couleur en base 10 (de 0 à 255)
def visualizeColor(colorPlace, red, green, blue):
    hexColor = convertRGBtoHex(red, green, blue)
    changeColorElements(colorPlace, hexColor)

# Fonctions qui changent la couleur de l'application en temps réel en récupérant les valeurs des Scrollbar
def changeRedMainColor(newRed):
    visualizeColor(1, int(newRed), greenMainColor.get(), blueMainColor.get())

def changeGreenMainColor(newGreen):
    visualizeColor(1, redMainColor.get(), int(newGreen), blueMainColor.get())

def changeBlueMainColor(newBlue):
    visualizeColor(1, redMainColor.get(), greenMainColor.get(), int(newBlue))

def changeRedSecondaryColor(newRed):
    visualizeColor(2, int(newRed), greenSecondaryColor.get(), blueSecondaryColor.get())

def changeGreenSecondaryColor(newGreen):
    visualizeColor(2, redSecondaryColor.get(), int(newGreen), blueSecondaryColor.get())

def changeBlueSecondaryColor(newBlue):
    visualizeColor(2, redSecondaryColor.get(), greenSecondaryColor.get(), int(newBlue))

# Sauvegarde

# Fonction qui crée une sauvegarde
    # Stock dans un fichier tous les élements à sauvegarder et les récupère grâce à la fonction suivante
def saveConfig():
    saveConfig = tkinter.filedialog.asksaveasfilename(title="Enregistrer une sauvegarde", filetypes=[("Fichier texte", ".txt")], initialfile="Sauvegarde_PyPS.txt", defaultextension=".txt", parent=pyps) # Crée le fichier de sauvegarde
    saveConfigFile = open(saveConfig, "w") # Ouvre le fichier de sauvegarde pour écrire dedans

	# Stockage des élements de sauvegarde dans le fichier, par l'intermédiaire d'un tableau/liste
	
    fileLines = [
    "Fichier de sauvegarde | PyPS",
    "",
    "Pendule :",
    "\Angle = {}".format(anglePendule.get()),
    "\tRayon = {}".format(threadPendule.get()),
    "\tGravité = {}".format(gravityPendule.get()),
    "\tTemps = {}".format(timePendule.get()),
    "",
    "Boule :",
    "\tHauteur = {}".format(hauteurBoule.get()),
    "\tRayon = {}".format(rayonBoule.get()),
    "\tMasse = {}".format(masseBoule.get()),
    "Options :",
    ("\tCouleurs = " + str(redMainColor.get()) + " " + str(greenMainColor.get()) + " " + str(blueMainColor.get()) + " " + str(redSecondaryColor.get()) + " " + str(greenSecondaryColor.get()) + " " + str(blueSecondaryColor.get()))
    ]

    for i in fileLines:
        saveConfigFile.write(i + " \n")
        
    saveConfigFile.close() # Ferme le fichier de sauvegarde

# Fonction qui ouvre une sauvegarde
def openConfig():
    openConfig = tkinter.filedialog.askopenfilename(title="Charger une sauvegarde", filetypes=[("Fichier texte", ".txt")], multiple=False,  initialfile="Sauvegarde_PyPS.txt", defaultextension=".txt", parent=pyps) # Ouverture du fichier de sauvegarde, désigné par cette variable
    openConfigFile = open(openConfig, "r") # Ouvre le fichier de sauvegarde pour le lire

    linesSaveFile = openConfigFile.readlines() # Récupére chaque ligne du fichier de sauvegarde et les met dans un tableau
    
    # Sépare les élements de la ligne réservé aux couleurs, dans le but de récupérer ces dernières
    cL = linesSaveFile[13].split()
    (redMColor, greenMColor, blueMColor, redSColor, greenSColor, blueSColor) = (int(cL[2]), int(cL[3]), int(cL[4]), int(cL[5]), int(cL[6]), int(cL[7]))
    # Applique la sauvegarde
    visualizeColor(1, redMColor, greenMColor, blueMColor)
    visualizeColor(2, redSColor, greenSColor, blueSColor)
    redMainColor.set(redMColor)
    greenMainColor.set(greenMColor)
    blueMainColor.set(blueMColor)
    redSecondaryColor.set(redSColor)
    greenSecondaryColor.set(greenSColor)
    blueSecondaryColor.set(blueSColor)
    
    # Sépare les élements des lignes réservé aux variables du pendule, dans le but de les récupérer
    (aPendule, rPendule, gPendule, tPendule) = (float(linesSaveFile[3].split()[2]), float(linesSaveFile[4].split()[2]), float(linesSaveFile[5].split()[2]), float(linesSaveFile[6].split()[2]))
    # Applique la sauvegarde
    updatePenduleAnimation(aPendule, rPendule, gPendule, tPendule)
    anglePendule.set(aPendule)
    threadPendule.set(rPendule)
    gravityPendule.set(gPendule)
    timePendule.set(tPendule)
    
    # Sépare les élements des lignes réservé aux variables de la boule, dans le but de les récupérer
    (hBoule, rBoule, mBoule) = (float(linesSaveFile[9].split()[2]), float(linesSaveFile[10].split()[2]), float(linesSaveFile[11].split()[2]))
    # Applique la sauvegarde
    hauteurBoule.delete(0, END)
    hauteurBoule.insert(0, hBoule)
    rayonBoule.delete(0, END)
    rayonBoule.insert(0, rBoule)
    masseBoule.delete(0, END)
    masseBoule.insert(0, mBoule)

	# Ferme le fichier de sauvegarde
    openConfigFile.close()




mainFont = "Roboto 12 bold"



# --------------------------------------------------------------------
# Construction de la fenêtre
# --------------------------------------------------------------------

# Fenêtre #
pyps.title("PyPS | Python Physics Simulator")
pyps.geometry("900x600")
# pyps.iconbitmap("pyps_logo.ico")

# En-tête #
header = Frame(pyps, bg=mainColorStr, highlightbackground=secondaryColorStr)
header.place(relx=0, rely=0, relwidth=1, relheight=0.05)
BgElements.append(header)
borderElements.append(header)

headerTitle = Label(header, text="Accueil", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
headerTitle.place(relx=0.5, rely=0.5, anchor=CENTER)
BgFgElements.append(headerTitle)

homeButton = Button(header, text="Accueil", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", font=mainFont)
BgFgElements.append(homeButton)

# Menu #
menu = Frame(pyps, bg=secondaryColorStr, highlightbackground=secondaryColorStr, highlightthickness=0)
menu.place(relx=0, rely=0.05, relwidth=0.3, relheight=0.9)
FgElements.append(menu)
borderElements.append(menu)

# Placement du panel "Paramètres" qui reste en place lorsqu'on accède à une simulation et fait apparaître des formulaire pour permettre à l'utilisateur de rentrer ses valeurs
tools = Frame(menu, bg=mainColorStr, highlightbackground=secondaryColorStr)
tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.65)
BgElements.append(tools)
borderElements.append(tools)

chooseTools = Label(tools, text="Choississez une simulation", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER)
BgFgElements.append(chooseTools)

# Création d'un bouton qui permet d'accéder au panel "Options" en appelant la fonction changePaned
options = Button(menu, text="Options", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, optionPaned, options), font=mainFont)
options.place(relx=0.05, rely=0.74, relwidth=0.90, relheight=0.10)
BgFgElements.append(options)

# Création d'un bouton qui permet d'accéder à la fenêtre "Histoire/Crédits" en appelant la fonction changePaned
creditsMenu = Button(menu, text="Histoire - Credits", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, historyPaned, creditsMenu), font=mainFont)
creditsMenu.place(relx=0.05, rely=0.87, relwidth=0.90, relheight=0.10)
BgFgElements.append(creditsMenu)


# Principal (Choix simulations) #
main = Frame(pyps, bg=secondaryColorStr, highlightbackground=secondaryColorStr)
main.place(relx=0.3, rely=0.05, relwidth=0.7, relheight=0.9)
FgElements.append(main)
borderElements.append(main)

home = PanedWindow(main, bg=secondaryColorStr)
home.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
FgElements.append(home)

# Création d'un bouton qui permet d'accéder à la simulation du pendule simple en appelant la fonction changePaned

penduleButton = Button(home, text="Pendule simple", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, penduleSimulation, penduleButton), font=mainFont)
penduleButton.place(relx=0.1, rely=0.1, relwidth=0.35, relheight=0.35)
BgFgElements.append(penduleButton)

# Création d'un bouton "soon" pour la 3e simulation qui n'a pas été faite
penduleNButton = Button(home, text="Soon", bg="grey", fg=secondaryColorStr, cursor="hand2", font=mainFont)
penduleNButton.place(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.35)

# Création d'un bouton qui permet d'accéder à la simulation de la chute d'une boule en appelant la fonction changePaned
bouleButton = Button(home, text="Chute d'une boule", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, bouleSimulation, bouleButton), font=mainFont)
bouleButton.place(relx=0.55, rely=0.55, relwidth=0.35, relheight=0.35)
BgFgElements.append(bouleButton)

# Création d'un 2e bouton soon
soonButton = Button(home, text="Soon", bg="grey", fg=secondaryColorStr, cursor="hand2", font=mainFont)
soonButton.place(relx=0.1, rely=0.55, relwidth=0.35, relheight=0.35)

# Panel "Options"
optionPaned = PanedWindow(pyps, bg=secondaryColorStr)
FgElements.append(optionPaned)

    # Couleurs
colorOptions = Canvas(optionPaned, bg=mainColorStr, highlightbackground=secondaryColorStr)
colorOptions.place(relx=0.025, rely=0.02, relwidth=0.95, relheight=0.7)
BgElements.append(colorOptions)
borderElements.append(colorOptions)

titleColorOptions = Label(colorOptions, text="Couleurs", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
titleColorOptions.place(relx=0.5, rely=0.07, anchor=CENTER)
BgFgElements.append(titleColorOptions)

mainColor = Canvas(colorOptions, bg=mainColorStr, highlightbackground=secondaryColorStr)
mainColor.place(relx=0.04, rely=0.18, relwidth=0.45, relheight=0.72)
BgElements.append(mainColor)
borderElements.append(mainColor)

# Création de scrollbar qui modifient la couleur principale à l'écran en prenant les valeurs données par l'utilisateur
redMainColor = Scale(mainColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Rouge', bg=mainColorStr, fg=secondaryColorStr, troughcolor="red", command=changeRedMainColor, font=mainFont)
greenMainColor = Scale(mainColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Vert', bg=mainColorStr, fg=secondaryColorStr, troughcolor="green", command=changeGreenMainColor, font=mainFont)
blueMainColor = Scale(mainColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Bleu', bg=mainColorStr, fg=secondaryColorStr, troughcolor="blue", command=changeBlueMainColor, font=mainFont)
visualizeMainColor = Canvas(mainColor, bg=mainColorStr, highlightbackground=secondaryColorStr)

BgFgElements.append(redMainColor)
BgFgElements.append(greenMainColor)
BgFgElements.append(blueMainColor)
BgElements.append(visualizeMainColor)
borderElements.append(visualizeMainColor)

# Initialise les valeurs des couleurs par défaut lors du lancement de l'application
redMainColor.pack(fill=X)
redMainColor.set(35)
greenMainColor.pack(fill=X)
greenMainColor.set(35)
blueMainColor.pack(fill=X)
blueMainColor.set(105)
visualizeMainColor.pack(fill=X)

titleMainColor = Label(colorOptions, text="Principale", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
titleMainColor.place(relx=0.27, rely=0.14, anchor=CENTER)
BgFgElements.append(titleMainColor)

secondaryColor = Canvas(colorOptions, bg=mainColorStr, highlightbackground=secondaryColorStr)
secondaryColor.place(relx=0.51, rely=0.18, relwidth=0.45, relheight=0.72)
BgElements.append(secondaryColor)
borderElements.append(secondaryColor)

titleSecondaryColor = Label(colorOptions, text="Secondaire", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
titleSecondaryColor.place(relx=0.74, rely=0.14, anchor=CENTER)
BgFgElements.append(titleSecondaryColor)

# Pareil que les scrollbar précédentes pour la couleur secondaire
redSecondaryColor = Scale(secondaryColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Rouge', bg=mainColorStr, fg=secondaryColorStr, troughcolor="red", command=changeRedSecondaryColor, font=mainFont)
greenSecondaryColor = Scale(secondaryColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Vert', bg=mainColorStr, fg=secondaryColorStr, troughcolor="green", command=changeGreenSecondaryColor, font=mainFont)
blueSecondaryColor = Scale(secondaryColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Bleu', bg=mainColorStr, fg=secondaryColorStr, troughcolor="blue", command=changeBlueSecondaryColor, font=mainFont)
visualizeSecondaryColor = Canvas(secondaryColor, bg=secondaryColorStr, highlightbackground=secondaryColorStr)

BgFgElements.append(redSecondaryColor)
BgFgElements.append(greenSecondaryColor)
BgFgElements.append(blueSecondaryColor)
FgElements.append(visualizeSecondaryColor)
borderElements.append(visualizeSecondaryColor)

# Initialise les valeurs des couleurs par défaut lors du lancement de l'application
redSecondaryColor.pack(fill=X)
redSecondaryColor.set(255)
greenSecondaryColor.pack(fill=X)
greenSecondaryColor.set(255)
blueSecondaryColor.pack(fill=X)
blueSecondaryColor.set(255)
visualizeSecondaryColor.pack(fill=X)

    # Sauvegarde
saveOptions = Canvas(optionPaned, bg=mainColorStr, highlightbackground=secondaryColorStr)
saveOptions.place(relx=0.025, rely=0.76, relwidth=0.95, relheight=0.22)
BgElements.append(saveOptions)
borderElements.append(saveOptions)

titleSaveOptions = Label(saveOptions, text="Sauvegarde", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
titleSaveOptions.place(relx=0.5, rely=0.2, anchor=CENTER)
BgFgElements.append(titleSaveOptions)

# Création d'un bouton qui crée une sauvegarde en appelant la fonction saveConfig
createSaveButton = Button(saveOptions, text="Créer une sauvegarde", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=saveConfig , font=mainFont)
createSaveButton.place(relx=0.04, rely=0.43, relwidth=0.45, relheight=0.35)
BgFgElements.append(createSaveButton)

# Création d'un bouton qui ouvre une sauvegarde en appelant la fonction openConfig
loadSaveButton = Button(saveOptions, text="Charger une sauvegarde", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=openConfig, font=mainFont)
loadSaveButton.place(relx=0.51, rely=0.43, relwidth=0.45, relheight=0.35)
BgFgElements.append(loadSaveButton)

# Paramètres options
toolsButtons = Canvas(tools, bg=secondaryColorStr, highlightthickness=0)
FgElements.append(toolsButtons)

# Panel "Histoire - Credits"
historyPaned = PanedWindow(pyps, bg=mainColorStr)
BgElements.append(historyPaned)

historyTextScroll = Scrollbar(historyPaned, bg=mainColorStr, troughcolor="white", width=15)
historyTextScroll.pack(side=RIGHT, fill=Y)
scrollElements.append(historyTextScroll)

historyText = Text(historyPaned, wrap=WORD, bg=mainColorStr, fg=secondaryColorStr, padx=10, pady=10, font=mainFont)
historyText.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
historyText.insert(END, "Nizar et Loïc sont 2 jeunes lycéens du Lycée Henri IV très intéressés par les sciences. Pour un de leurs projets de NSI, ils ont décidé de créer, non pas un jeu comme la majorité des élèves mais bien une application de simulations physiques que vous utilisez actuellement !\n\nVous pouvez pour l'instant accéder à deux simulations : le mouvement d'un pendule simple et l'expérience d’une boule en chute libre.\n\n- La simulation du mouvement d’un pendule nous montre le mouvement approximatif d'un pendule simple qui oscille. Cette simulation est réalisée à partir d'équations mathématiques qui permettent d'obtenir le mouvement du pendule à partir de la longueur du fil qui le tient, l'angle de départ du pendule et la gravité à laquelle il est soumis. Il faut noter que le mouvement du pendule n'est réaliste que pour de faibles amplitudes. En effet, au-delà de cette amplitude, les équations du mouvements ne sont plus linéaires, c'est-à-dire qu'on ne peut pas définir d'équation précise pour caractériser le mouvement du pendule.\n\n- La deuxième simulation est l'expérience d’une boule en chute libre. Elle consiste en un lâcher d'une boule de masse et de rayon à définir respectivement en tonnes et en mètres à partir d'une hauteur en mètres, elle aussi à définir. Dans cette expérience, les frottements de l'air sont négligés et la chute de la boule ne dépend ni de sa masse, ni de son volume, ni de sa densité : elle ne dépend que de sa hauteur. De plus, il est à noter que cette simulation est le résultat de calculs théoriques qui nous montrent donc des résultats réalistes pour des valeurs raisonnables mais aussi époustouflants pour des valeurs absurdes qui sont impossibles dans la vraie vie : c'est là toute la magie de la théorie, de pouvoir faire apparaître l’inaccessible depuis notre réalité.\n\nVoici donc les 2 premières simulations que nous avons conçues avec le langage Python et nous espérons pouvoir continuer sur cette voie en vue de devenir de vraies scientifiques et ingénieurs compétents dans les années à venir.\n\nMerci à tous ceux ayant participé de près ou de loin à la réalisation de ce projet. Par ailleurs, nous vous avons mis à disposition plusieurs boutons qui vous redirigeront vers diverses pages internet.\n- Le bouton « Github du projet », qui permet d’accéder aux sources du projet, laisser ainsi en libre-accès.\n- Le bouton « Mathadomicile », qui vous redirigera vers le site internet de notre professeur de NSI. Ce site contient de nombreuses ressources, tant en informatique qu’en mathématiques et plus particulièrement des cours de qualités, laissés en libre-accès, à tous ! \n- Le bouton « Lycée Henri IV », vous redirigera vers le site de notre lycée.\n\n\nNizar NOUBIR & Loic WANTIEP-KAMWA")
historyText.config(state=DISABLED)
BgFgElements.append(historyText)

historyText.config(yscrollcommand=historyTextScroll.set)
historyTextScroll.config(command=historyText.yview)

githubButton = Button(historyPaned, text="Github du projet", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:webbrowser.open("github.com/Birnou75/PyPS"), font=mainFont)
githubButton.place(relx=0.05, rely=0.87, relwidth=0.28, relheight=0.1)
BgFgElements.append(githubButton)

mathadomicileButton = Button(historyPaned, text="Mathadomicile", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:webbrowser.open("ph.moutou.free.fr"), font=mainFont)
mathadomicileButton.place(relx=0.36, rely=0.87, relwidth=0.28, relheight=0.1)
BgFgElements.append(mathadomicileButton)

henri4button = Button(historyPaned, text="Lycée Henri IV", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:webbrowser.open("lycee-henri4.com"), font=mainFont)
henri4button.place(relx=0.67, rely=0.87, relwidth=0.28, relheight=0.1)
BgFgElements.append(henri4button)


# Panel de la simulation "Pendule"
penduleSimulation = PanedWindow(main, bg=secondaryColorStr)
FgElements.append(penduleSimulation)

# Création de scrollbar ui modifient les variables de la simulation en prenant les valeurs données par l'utilisateur
anglePendule = Scale(toolsButtons, orient="horizontal", from_=0, to=180, resolution=1, tickinterval=90, label='Angle (deg)', bg=mainColorStr, fg=secondaryColorStr, troughcolor=secondaryColorStr, command=changeThetaMax, font=mainFont)
threadPendule = Scale(toolsButtons, orient="horizontal", from_=1, to=3, resolution=0.01, tickinterval=1, label='Longueur du fil (mètres)', bg=mainColorStr, fg=secondaryColorStr, troughcolor=secondaryColorStr, command=changeR, font=mainFont)
gravityPendule = Scale(toolsButtons, orient="horizontal", from_=1, to=10, resolution=1, tickinterval=2, label='Gravité (lieu)', bg=mainColorStr, fg=secondaryColorStr, troughcolor=secondaryColorStr, command=changeG, font=mainFont)
timePendule = Scale(toolsButtons, orient="horizontal", from_=10, to=100, resolution=1, tickinterval=30, label='Temps de la simulation (sec)', bg=mainColorStr, fg=secondaryColorStr, troughcolor=secondaryColorStr, command=changeT, font=mainFont)

scrollElements.append(anglePendule)
scrollElements.append(threadPendule)
scrollElements.append(gravityPendule)
scrollElements.append(timePendule)

infosPendule = Label(penduleSimulation, text="Période : 0 s", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
infosPendule.place(relx=0.6, rely=0.9, relwidth=0.4, relheight=0.09)
BgFgElements.append(infosPendule)

	# Animation, partie majeure
animationPendule = Canvas(penduleSimulation, bg="white", highlightbackground=secondaryColorStr)
animationPendule.place(relx=0.025, rely=0.05, relheight=0.8, relwidth=0.95)
borderElements.append(animationPendule)

# Création d'un bouton qui lance l'animation en appelant la fonction penduleAnimation
graphButton = Button(penduleSimulation, text="Lacher le pendule", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:penduleAnimation(g, t), font=mainFont)
graphButton.place(relx=0.025, rely=0.92, relwidth=0.3, relheight=0.07)
BgFgElements.append(graphButton)

# Mise en place du pendule simple avec les valeurs par défaut
penduleFig = Figure(figsize=(8, 6), dpi=100)
pendulePlot = penduleFig.add_subplot(111)

ax = penduleFig.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
pendulePlot.set_xlim([-3.5, 3.5])
pendulePlot.set_ylim([-3.5, 3.5])
pendulePlot.axis("off")

(thetaMax, r, g, t) = (0, 1, 1, 10)
theta = (thetaMax)*sin(-pi/2)

pendulePlot.scatter([0, -3.5, 3.5], [0, 0, 0], s=0)
pendulePlot.plot([-3.5, 3.5], [0, 0], c="black")
pendulePlot.plot([0, r*cos(theta-pi/2)], [0, r*sin(theta-pi/2)], c="red", zorder=1)
pendulePlot.scatter(r*cos(theta-pi/2), r*sin(theta-pi/2), s=500, c="orange", zorder=2)

animationPenduleCanvas = FigureCanvasTkAgg(penduleFig, master = animationPendule)
animationPenduleCanvas.draw()
animationPenduleCanvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER)

# Panel de la simulation "Boule"
bouleSimulation = PanedWindow(main, bg=secondaryColorStr)
FgElements.append(bouleSimulation)

# Création du Canvas où est affichée la simulation boule
animationBouleCanvas = Canvas(bouleSimulation, bg="white", highlightbackground=secondaryColorStr, highlightthickness=0)
animationBouleCanvas.place(relx=0.025, rely=0.05, relheight=0.8, relwidth=0.95)
borderElements.append(animationBouleCanvas)

# Création d'un Canvas pour ecrire la légende de la simulation chute d'une boule
infoBouleCanvas = Canvas(bouleSimulation, bg="white", highlightbackground=secondaryColorStr, highlightthickness=0)
infoBouleCanvas.place(relx=0.025, rely=0.84, relheight=0.12, relwidth=0.95)
borderElements.append(infoBouleCanvas)

#Création de formulaires qui modifient les variables de la simulation en prenant les valeurs données par l'utilisateur
hauteurBouleLabel = Label(toolsButtons, text="Hauteur de la boule\n(mètres)", bg=secondaryColorStr, fg=mainColorStr,  font=mainFont)
hauteurBoule = Entry(toolsButtons, bg=mainColorStr, fg=secondaryColorStr, insertbackground=secondaryColorStr, highlightthickness=0, font=mainFont)
rayonBouleLabel = Label(toolsButtons, text="Rayon de la boule\n(mètres)", bg=secondaryColorStr, fg=mainColorStr, font=mainFont)
rayonBoule = Entry(toolsButtons, bg=mainColorStr, fg=secondaryColorStr, insertbackground=secondaryColorStr, highlightthickness=0, font=mainFont)
masseBouleLabel = Label(toolsButtons, text="Masse de la boule\n(en tonnes)", bg=secondaryColorStr, fg=mainColorStr, font=mainFont)
masseBoule = Entry(toolsButtons, bg=mainColorStr, fg=secondaryColorStr, insertbackground=secondaryColorStr, highlightthickness=0, font=mainFont)

errorBouleLabel = Label(toolsButtons, text="Saisissez un float !", bg=secondaryColorStr, fg="red",  font=mainFont)
FgBgElements.append(errorBouleLabel)

BgFgElements.append(hauteurBoule)
FgBgElements.append(hauteurBouleLabel)
BgFgElements.append(rayonBoule)
FgBgElements.append(rayonBouleLabel)
BgFgElements.append(masseBoule)
FgBgElements.append(masseBouleLabel)

# Valeurs par défaut de la simulation
hauteurBoule.insert(0, 100)
rayonBoule.insert(0, 20)
masseBoule.insert(0, 100000)

# Création d'un bouton qui lance la simulation en appelant la fonction startBouleSimulationFunc
startBouleSimulation = Button(toolsButtons, bg=mainColorStr, fg=secondaryColorStr, text="Lancer la boule", command=startBouleSimulationFunc, cursor="hand2", font=mainFont)
BgFgElements.append(startBouleSimulation)


# Pied de page #
footer = Frame(pyps, bg=mainColorStr, highlightbackground=secondaryColorStr)
footer.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)
BgElements.append(footer)
borderElements.append(footer)

footerCredits = Label(footer, text="Version 1.0 | Par Nizar et Loïc", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
footerCredits.place(relx=0.5, rely=0.5, anchor=CENTER)
BgFgElements.append(footerCredits)


# Logo #



# --------------------------------------------------------------------
# Lancement de la fenêtre
# --------------------------------------------------------------------

pyps.mainloop()
