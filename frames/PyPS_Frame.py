# PyPS_Frame -> Fichier constituant la fenêtre principale du logiciel

# --------------------------------------------------------------------
# Importations / Initialisation de la fenêtre
# --------------------------------------------------------------------
import os

from tkinter import *
import tkinter.filedialog

from turtle import *

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

from math import *

pyps = Tk()
pyps.minsize(width=700, height=625)


# --------------------------------------------------------------------
# Fonctions et variables relatifs au GUI
# --------------------------------------------------------------------
saveConfigPath="Desktop/NSI/PyPS/saves/"


# Listes d'élements en fonction de leurs attributs
BgFgElements = []
FgBgElements = []
BgElements = []
FgElements = []
scrollElements = []
borderElements = []


# Fonctions générales
def changePaned(panedToDestroy, panedToPlace, buttonPanedName):
    panedToDestroy.place_forget()
    panedToPlace.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    headerTitle['text'] = buttonPanedName['text']

    if(panedToPlace != home):
        homeButton['command']=lambda:[changePaned(panedToPlace, panedToDestroy, homeButton)]
        homeButton.place(relx=0.017, rely=0.1, relheight=0.8, relwidth=0.1)
        chooseTools.place(relx=0.5, rely=0.05, anchor=CENTER)
        chooseTools.config(text="Paramètres")
        options.place_forget()
        creditsMenu.place_forget()
        tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.9)
        simulationSettings(panedToPlace, True)
    else:
        simulationSettings(panedToDestroy, False)
        chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER)
        chooseTools.config(text="Choisissez une simulation")
        homeButton.place_forget()
        tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.65)
        options.place(relx=0.05, rely=0.74, relwidth=0.90, relheight=0.10)
        creditsMenu.place(relx=0.05, rely=0.87, relwidth=0.90, relheight=0.10)
    if(panedToPlace == optionPaned):
        tools.place_forget()
        panedToPlace.place_forget()
        panedToPlace.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.86)

def simulationSettings(paned, enable):
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
    if(paned == bouleSimulation):
        if(enable == True):
            toolsButtons.place(rely=0.12, relx=0.087, relwidth=0.82, relheight=0.8)
            hauteurBouleLabel.pack(pady=10)
            hauteurBoule.pack(fill=X)
            rayonBouleLabel.pack(pady=10)
            rayonBoule.pack(fill=X)
            masseBouleLabel.pack(pady=10)
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
            startBouleSimulation.place_forget()

# Fonctions relatifs au "Pendule simple"
def updatePenduleAnimation(thetaMaxUpdate, rUpdate, gUpdate, thetaUpdate):
	pendulePlot.clear()

	ax.spines['left'].set_position('zero')
	ax.spines['bottom'].set_position('zero')
	pendulePlot.set_xlim([-3.5, 3.5])
	pendulePlot.set_ylim([-3.5, 3.5])
	pendulePlot.axis("off")

	pendulePlot.scatter([0, -3.5, 3.5], [0, 0, 0], s=0)
	pendulePlot.plot([-3.5, 3.5], [0, 0], c="black")
	pendulePlot.scatter(rUpdate*cos(thetaUpdate-pi/2), rUpdate*sin(thetaUpdate-pi/2), s=500, c="orange", zorder=2)
	pendulePlot.plot([0, rUpdate*cos(thetaUpdate-pi/2)], [0, rUpdate*sin(thetaUpdate-pi/2)], c="red", zorder=1)

	animationPenduleCanvas.draw()

def penduleAnimation(g, t):
	periode = 2*pi*sqrt(r/g)
	infosPendule['text'] = "Période : {} s\n Temps restant : 0h, 0m, 0s".format(round(periode, 1))

	h = 0.1
	omega = sqrt(g/r)

	for i in range(0, int(t/h)):
		thetaAnim = (thetaMax)*sin(omega*i*h + pi/2)
		updatePenduleAnimation(thetaMax, r, g, thetaAnim)
		plt.pause(h/2.6)

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

#Fonctions relatives à la boule
    #parametrage des crayons
def startBouleSimulationFunc():
	x, y = screensize()
	#Paramétrage des crayons
	speed(0)
	explosion1 = Turtle()
	explosion2 = Turtle()
	explosion3 = Turtle()
	cratere = Turtle()
	soufle = Turtle()
	legende = Turtle()
	explosion1.ht()
	explosion2.ht()
	explosion3.ht()
	cratere.ht()
	soufle.ht()
	legende.ht()
	explosion1.speed(0)
	explosion2.speed(0)
	explosion3.speed(0)
	cratere.speed(0)
	soufle.speed(0)
	explosion1.pencolor("white")
	explosion2.pencolor("white")
	explosion3.pencolor("white")

	#--------Paramètres-----------
	h = float(input("Choisissez la hauteur en mètres \n"))
	r = float(input("Choisissez le rayon de la boule en mètres \n"))
	m = float(input("Choisissez la masse de la boule en kg \n"))
	#--------Constantes----------
	g = 9.8
	#--------Paramétrage de l'échelle----------
	echelle = h/(y-50)

	#--------Calcul de valeurs numériques---------
	tmax = sqrt(2*h/g)
	Vmax = sqrt(2*g*h)
	Emax = (1/2)*m*(Vmax**2)

	p = m/(4*pi*r**3/3)
	pt = 2.9*10**3
	d = 2*r
	#---------Calcul du diamètre du cratère--------
	D = 1.161*(p/pt)**(1/3)*d**0.78*Vmax**0.44*g**-0.22

	#---------Creation de tableaux pour réaliser des boucles d'animation-----
	a = (D/2)/echelle
	t = np.arange(0,tmax+0.04,0.04)
	if D/(2*r) < 1:
		R = np.linspace(0,a,10)
	else:
		 R = np.linspace(0,a,100)

	#--------Légende------------
	legende.up()
	legende.setpos(-20,-92.5)
	legende.down()
	legende.forward(10)
	legende.up()
	legende.setpos(-10,-100)
	legende.down()
	legende.write("  :  {}m".format(10*echelle))
	legende.up()
	legende.setpos(-10,-110)
	legende.down()
	legende.write("Vitesse max = {}m/s".format(round(Vmax,2)))
	legende.up()
	legende.setpos(-10,-120)
	legende.down()
	legende.write("Energie mécanique = {}J".format(round(Emax,2)))
	legende.up()
	legende.setpos(-10,-130)
	legende.down()
	legende.write("Durée théorique de la chute = {}s".format(round(tmax,2)))
	legende.up()
	legende.setpos(-10,-140)
	legende.down()
	legende.write("Diamètre du cratère = {}m".format(round(D,2)))

	#---------Création de la boule-------
	if r/h <= 1/(y-50):
		b = 1
	elif r/h > 1/(y-50) and r/h < 1:
		b = (r/h)*(y-50)
	elif r/h >= 1:
		b = y-50
	begin_poly()
	circle(b)
	end_poly()
	p = get_poly()
	register_shape("boule", p)
	shape("boule")
	clear()
	#--------Fonctions------------

	up()
	setpos(-x,0)
	down()
	setpos(x,0)
	up()
	setpos(0,y-50)
	delay(30)
	for i in t:
		setpos(-b,(y-50)*((h-(1/2)*g*(i**2))/h)+b)
	delay(1)
	for i in R:
		cratere.clear()
		soufle.up()
		cratere.up()
		soufle.setpos(3*i,0)
		soufle.setheading(90)
		cratere.setpos(i,0)
		cratere.setheading(90)
		soufle.down()
		cratere.down()
		soufle.circle(3*i,180)
		cratere.circle(i,-180)
		explosion1.goto(i,0)
		explosion2.goto(-i,0)
		explosion3.goto(i,0)
		explosion3.goto(-i,0)
		setpos(-b,b-i)
		soufle.clear()


# Fonctions relatifs aux "Options"
    # Couleurs
mainColorStr = "#232369"
secondaryColorStr = "#ffffff"

def changeColorElements(colorPlace, color):
    if(colorPlace == 1):
        global mainColorStr
        mainColorStr = color
        for i in BgFgElements:
            i['bg'] = mainColorStr
        for i in FgBgElements:
            i['fg'] = mainColorStr
        for i in scrollElements:
            i['bg'] = mainColorStr
        for i in BgElements:
            i['bg'] = mainColorStr
    elif(colorPlace == 2):
        global secondaryColorStr
        secondaryColorStr = color
        for i in BgFgElements:
            i['fg'] = secondaryColorStr
        for i in FgBgElements:
            i['bg'] = secondaryColorStr
        for i in scrollElements:
            i['fg'] = secondaryColorStr
            i['troughcolor'] = secondaryColorStr
        for i in FgElements:
            i['bg'] = secondaryColorStr
        for i in borderElements:
            i['highlightbackground'] = secondaryColorStr
            i['highlightcolor'] = secondaryColorStr

def convertRGBtoHex(red, green, blue):
    redHex = format(red, "02x")
    greenHex = format(green, "02x")
    blueHex = format(blue, "02x")
    hexColor = ("#" + redHex + greenHex + blueHex)
    return hexColor

def visualizeColor(colorPlace, red, green, blue):
    hexColor = convertRGBtoHex(red, green, blue)
    changeColorElements(colorPlace, hexColor)

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
def saveConfig():
    saveConfig = tkinter.filedialog.asksaveasfilename(title="Enregistrer une sauvegarde", filetypes=[("Fichier texte", ".txt")],              initialfile="Sauvegarde_PyPS.txt", defaultextension=".txt", initialdir=saveConfigPath, parent=pyps)
    saveConfigFile = open(saveConfig, "w")

    fileLines = [
    "Fichier de sauvegarde | PyPS",
    "",
    "Pendule :",
    "anglePendule = {}".format(anglePendule.get()),
    "Rayon = {}".format(threadPendule.get()),
    "Gravité = {}".format(gravityPendule.get()),
    "Temps = {}".format(timePendule.get()),
    "",
    "Boule :",
    "",
    "Options :",
    ("Couleurs = " + str(redMainColor.get()) + " " + str(greenMainColor.get()) + " " + str(blueMainColor.get()) + " " + str(redSecondaryColor.get()) + " " + str(greenSecondaryColor.get()) + " " + str(blueSecondaryColor.get()))
    ]

    for i in fileLines:
        saveConfigFile.write(i + " \n")
    saveConfigFile.close()

def openConfig():
    openConfig = tkinter.filedialog.askopenfilename(title="Charger une sauvegarde", filetypes=[("Fichier texte", ".txt")], multiple=False,  initialfile="Sauvegarde_PyPS.txt", defaultextension=".txt", initialdir=saveConfigPath, parent=pyps)
    openConfigFile = open(openConfig, "r")

    linesSaveFile = openConfigFile.readlines()
    print(linesSaveFile)

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

tools = Frame(menu, bg=mainColorStr, highlightbackground=secondaryColorStr)
tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.65)
BgElements.append(tools)
borderElements.append(tools)

chooseTools = Label(tools, text="Choississez une simulation", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER)
BgFgElements.append(chooseTools)

options = Button(menu, text="Options", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, optionPaned, options), font=mainFont)
options.place(relx=0.05, rely=0.74, relwidth=0.90, relheight=0.10)
BgFgElements.append(options)

creditsMenu = Button(menu, text="Histoire - Credits", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", font=mainFont)
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

penduleButton = Button(home, text="Pendule simple", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, penduleSimulation, penduleButton), font=mainFont)
penduleButton.place(relx=0.1, rely=0.1, relwidth=0.35, relheight=0.35)
BgFgElements.append(penduleButton)

penduleNButton = Button(home, text="Pendule de Newton", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, penduleNSimulation, penduleNButton), font=mainFont)
penduleNButton.place(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.35)
BgFgElements.append(penduleNButton)

bouleButton = Button(home, text="Chute d'une boule", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, bouleSimulation, bouleButton), font=mainFont)
bouleButton.place(relx=0.1, rely=0.55, relwidth=0.35, relheight=0.35)
BgFgElements.append(bouleButton)

soonButton = Button(home, text="Bientôt..", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", font=mainFont)
soonButton.place(relx=0.55, rely=0.55, relwidth=0.35, relheight=0.35)
BgFgElements.append(soonButton)

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

redMainColor = Scale(mainColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Rouge', bg=mainColorStr, fg=secondaryColorStr, troughcolor="red", command=changeRedMainColor, font=mainFont)
greenMainColor = Scale(mainColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Vert', bg=mainColorStr, fg=secondaryColorStr, troughcolor="green", command=changeGreenMainColor, font=mainFont)
blueMainColor = Scale(mainColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Bleu', bg=mainColorStr, fg=secondaryColorStr, troughcolor="blue", command=changeBlueMainColor, font=mainFont)
visualizeMainColor = Canvas(mainColor, bg=mainColorStr, highlightbackground=secondaryColorStr)

BgFgElements.append(redMainColor)
BgFgElements.append(greenMainColor)
BgFgElements.append(blueMainColor)
BgElements.append(visualizeMainColor)
borderElements.append(visualizeMainColor)

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

redSecondaryColor = Scale(secondaryColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Rouge', bg=mainColorStr, fg=secondaryColorStr, troughcolor="red", command=changeRedSecondaryColor, font=mainFont)
greenSecondaryColor = Scale(secondaryColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Vert', bg=mainColorStr, fg=secondaryColorStr, troughcolor="green", command=changeGreenSecondaryColor, font=mainFont)
blueSecondaryColor = Scale(secondaryColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Bleu', bg=mainColorStr, fg=secondaryColorStr, troughcolor="blue", command=changeBlueSecondaryColor, font=mainFont)
visualizeSecondaryColor = Canvas(secondaryColor, bg=secondaryColorStr, highlightbackground=secondaryColorStr)

BgFgElements.append(redSecondaryColor)
BgFgElements.append(greenSecondaryColor)
BgFgElements.append(blueSecondaryColor)
FgElements.append(visualizeSecondaryColor)
borderElements.append(visualizeSecondaryColor)

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

createSaveButton = Button(saveOptions, text="Créer une sauvegarde", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=saveConfig , font=mainFont)
createSaveButton.place(relx=0.04, rely=0.43, relwidth=0.45, relheight=0.35)
BgFgElements.append(createSaveButton)

loadSaveButton = Button(saveOptions, text="Charger une sauvegarde", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=openConfig, font=mainFont)
loadSaveButton.place(relx=0.51, rely=0.43, relwidth=0.45, relheight=0.35)
BgFgElements.append(loadSaveButton)

# Paramètres options
toolsButtons = Canvas(tools, bg=mainColorStr, highlightbackground=secondaryColorStr)
FgElements.append(toolsButtons)
borderElements.append(toolsButtons)

# Panel de la simulation "Pendule"
penduleSimulation = PanedWindow(main, bg=secondaryColorStr)
FgElements.append(penduleSimulation)

anglePendule = Scale(toolsButtons, orient="horizontal", from_=0, to=180, resolution=1, tickinterval=90, label='anglePendule (deg)', bg=mainColorStr, fg=secondaryColorStr, troughcolor=secondaryColorStr, command=changeThetaMax, font=mainFont)
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

graphButton = Button(penduleSimulation, text="Lacher le pendule", bg=mainColorStr, fg=secondaryColorStr, cursor="hand2", command=lambda:penduleAnimation(g, t), font=mainFont)
graphButton.place(relx=0.025, rely=0.92, relwidth=0.3, relheight=0.07)
BgFgElements.append(graphButton)

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


# Panel de la simulation "Pendule de Newton"
penduleNSimulation = PanedWindow(main, bg=secondaryColorStr)
FgElements.append(penduleNSimulation)

# Panel de la simulation "Boule"
bouleSimulation = PanedWindow(main, bg=secondaryColorStr)
FgElements.append(bouleSimulation)

animationBouleCanvas = Canvas(bouleSimulation, bg=mainColorStr, highlightbackground=secondaryColorStr)
animationBouleCanvas.place(relx=0.025, rely=0.05, relheight=0.8, relwidth=0.95)
FgElements.append(animationBouleCanvas)
borderElements.append(animationBouleCanvas)

hauteurBouleLabel = Label(toolsButtons, text="Hauteur de la boule", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
hauteurBoule = Entry(toolsButtons, bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
rayonBouleLabel = Label(toolsButtons, text="Rayon de la boule", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
rayonBoule = Entry(toolsButtons, bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
masseBouleLabel = Label(toolsButtons, text="Hauteur de la boule", bg=mainColorStr, fg=secondaryColorStr, font=mainFont)
masseBoule = Entry(toolsButtons, bg=mainColorStr, fg=secondaryColorStr, font=mainFont)

BgFgElements.append(hauteurBoule)
BgFgElements.append(hauteurBouleLabel)
BgFgElements.append(rayonBoule)
BgFgElements.append(rayonBouleLabel)
BgFgElements.append(masseBoule)
BgFgElements.append(masseBouleLabel)

hauteurBoule.insert(0, 100)
rayonBoule.insert(0, 20)
masseBoule.insert(0, 100000)

startBouleSimulation = Button(toolsButtons, bg=mainColorStr, fg=secondaryColorStr, text="Faire chuter la boule", command=startBouleSimulationFunc, cursor="hand2", font=mainFont)
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
