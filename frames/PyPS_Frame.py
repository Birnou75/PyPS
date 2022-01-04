# PyPS_Frame -> Fichier constituant la fenêtre principale du logiciel

# --------------------------------------------------------------------
# Importations / Initialisation de la fenêtre
# --------------------------------------------------------------------

from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import *

pyps = Tk()
pyps.minsize(width=700, height=625)


# --------------------------------------------------------------------
# Fonctions et variables relatifs au GUI
# --------------------------------------------------------------------

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
        
def simulationSettings(paned, enable):
    if(paned == penduleSimulation):
        if(enable == True):
            toolsScrollBar.configure(command=toolsButtons.yview)
            toolsButtons.configure(yscrollcommand=toolsScrollBar.set)
            toolsButtons.place(rely=0.12, relx=0.06, relwidth=0.82, relheight=0.8)
            toolsScrollBar.pack(side=RIGHT, fill=Y)

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

# Fonctions relatifs au "Pendule simple"
def updatePenduleAnimation(thetaMaxUpdate, rUpdate, gUpdate, thetaUpdate):
	pendulePlot.clear()
	
	ax.grid(True)
	ax.spines['left'].set_position('zero')
	ax.spines['bottom'].set_position('zero')
	pendulePlot.set_xlim([-pi, pi])
	pendulePlot.set_ylim([-pi, pi])

	pendulePlot.scatter([0, rUpdate*cos(thetaUpdate-pi/2)], [0, rUpdate*sin(thetaUpdate-pi/2)])
	pendulePlot.plot([0, rUpdate*cos(thetaUpdate-pi/2)], [0, rUpdate*sin(thetaUpdate-pi/2)])
	
	animationCanvas.draw()
	
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

# Fonctions relatifs aux "Options"

mainColorStr = "#232369"
secondaryColorStr = "#ffffff"

def convertRGBtoHex(red, green, blue):
    redHex = format(red, "02x")
    greenHex = format(green, "02x")
    blueHex = format(blue, "02x")
    
    hexColor = ("#" + redHex + greenHex + blueHex)
    return hexColor
    
def visualizeColor(object, red, green, blue):
    hexColor = convertRGBtoHex(red, green, blue)
    object['bg'] = hexColor

def changeRedMainColor(newRed):
    visualizeColor(visualizeMainColor, int(newRed), greenMainColor.get(), blueMainColor.get())
    
def changeGreenMainColor(newGreen):
    visualizeColor(visualizeMainColor, redMainColor.get(), int(newGreen), blueMainColor.get())
    
def changeBlueMainColor(newBlue):
    visualizeColor(visualizeMainColor, redMainColor.get(), greenMainColor.get(), int(newBlue))
    
def changeRedSecondaryColor(newRed):
    visualizeColor(visualizeSecondaryColor, int(newRed), greenSecondaryColor.get(), blueSecondaryColor.get())
    
def changeGreenSecondaryColor(newGreen):
    visualizeColor(visualizeSecondaryColor, redSecondaryColor.get(), int(newGreen), blueSecondaryColor.get())
    
def changeBlueSecondaryColor(newBlue):
    visualizeColor(visualizeSecondaryColor, redSecondaryColor.get(), greenSecondaryColor.get(), int(newBlue))
	

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

headerTitle = Label(header, text="Accueil", bg="#232369", fg=secondaryColorStr, font=mainFont)
headerTitle.place(relx=0.5, rely=0.5, anchor=CENTER)

homeButton = Button(header, text="Accueil", bg="#232369", fg=secondaryColorStr, cursor="hand2", font=mainFont)


# Menu #
menu = Frame(pyps, bg=secondaryColorStr, highlightthickness=2)
menu.place(relx=0, rely=0.05, relwidth=0.3, relheight=0.9)

tools = Frame(menu, bg="#232369")
tools.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.65)

chooseTools = Label(tools, text="Choississez une simulation", bg="#232369", fg=secondaryColorStr, font=mainFont)
chooseTools.place(relx=0.5, rely=0.5, anchor=CENTER)

options = Button(menu, text="Options", bg="#232369", fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, optionPaned, options), font=mainFont)
options.place(relx=0.05, rely=0.74, relwidth=0.90, relheight=0.10)

creditsMenu = Button(menu, text="Histoire - Credits", bg="#232369", fg=secondaryColorStr, cursor="hand2", font=mainFont)
creditsMenu.place(relx=0.05, rely=0.87, relwidth=0.90, relheight=0.10)


# Principal (Choix simulations) #
main = Frame(pyps, bg=secondaryColorStr)
main.place(relx=0.3, rely=0.05, relwidth=0.7, relheight=0.9)

home = PanedWindow(main, bg=secondaryColorStr)
home.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

penduleButton = Button(home, text="Pendule simple", bg="#232369", fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, penduleSimulation, penduleButton), font=mainFont)
penduleButton.place(relx=0.1, rely=0.1, relwidth=0.35, relheight=0.35)

penduleNButton = Button(home, text="Pendule de Newton", bg="#232369", fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, penduleNSimulation, penduleNButton), font=mainFont)
penduleNButton.place(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.35)

bouleButton = Button(home, text="Chute d'une boule", bg="#232369", fg=secondaryColorStr, cursor="hand2", command=lambda:changePaned(home, bouleSimulation, bouleButton), font=mainFont)
bouleButton.place(relx=0.1, rely=0.55, relwidth=0.35, relheight=0.35)

soonButton = Button(home, text="Bientôt..", bg="#232369", fg=secondaryColorStr, cursor="hand2", font=mainFont)
soonButton.place(relx=0.55, rely=0.55, relwidth=0.35, relheight=0.35)

# Panel "Options"

optionPaned = PanedWindow(main, bg=secondaryColorStr)

colorOptions = Canvas(optionPaned, bg="#232369")
colorOptions.place(relx=0.025, rely=0.05, relwidth=0.95, relheight=0.7)

titleColorOptions = Label(colorOptions, text="Couleurs", bg="#232369", fg=secondaryColorStr, font=mainFont)
titleColorOptions.place(relx=0.5, rely=0.07, anchor=CENTER)

mainColor = Canvas(colorOptions, bg="#232369")
mainColor.place(relx=0.04, rely=0.18, relwidth=0.45, relheight=0.72)

redMainColor = Scale(mainColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Rouge', bg="#232369", fg=secondaryColorStr, troughcolor="red", command=changeRedMainColor, font=mainFont)
greenMainColor = Scale(mainColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Vert', bg="#232369", fg=secondaryColorStr, troughcolor="green", command=changeGreenMainColor, font=mainFont)
blueMainColor = Scale(mainColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Bleu', bg="#232369", fg=secondaryColorStr, troughcolor="blue", command=changeBlueMainColor, font=mainFont)
visualizeMainColor = Canvas(mainColor, bg="#232369")

redMainColor.pack(fill=X)
redMainColor.set(35)
greenMainColor.pack(fill=X)
greenMainColor.set(35)
blueMainColor.pack(fill=X)
blueMainColor.set(105)
visualizeMainColor.pack(fill=X)

titleMainColor = Label(colorOptions, text="Principale", bg="#232369", fg=secondaryColorStr, font=mainFont)
titleMainColor.place(relx=0.27, rely=0.14, anchor=CENTER)

secondaryColor = Canvas(colorOptions, bg="#232369")
secondaryColor.place(relx=0.51, rely=0.18, relwidth=0.45, relheight=0.72)

titleSecondaryColor = Label(colorOptions, text="Secondaire", bg="#232369", fg=secondaryColorStr, font=mainFont)
titleSecondaryColor.place(relx=0.74, rely=0.14, anchor=CENTER)

redSecondaryColor = Scale(secondaryColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Rouge', bg="#232369", fg=secondaryColorStr, troughcolor="red", command=changeRedSecondaryColor, font=mainFont)
greenSecondaryColor = Scale(secondaryColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Vert', bg="#232369", fg=secondaryColorStr, troughcolor="green", command=changeGreenSecondaryColor, font=mainFont)
blueSecondaryColor = Scale(secondaryColor, orient="horizontal", from_=0, to=255, resolution=1, tickinterval=255, label='Bleu', bg="#232369", fg=secondaryColorStr, troughcolor="blue", command=changeBlueSecondaryColor, font=mainFont)
visualizeSecondaryColor = Canvas(secondaryColor, bg=secondaryColorStr)

redSecondaryColor.pack(fill=X)
redSecondaryColor.set(255)
greenSecondaryColor.pack(fill=X)
greenSecondaryColor.set(255)
blueSecondaryColor.pack(fill=X)
blueSecondaryColor.set(255)
visualizeSecondaryColor.pack(fill=X)

# Panel de la simulation "Pendule"
penduleSimulation = PanedWindow(main, bg=secondaryColorStr)

toolsButtons = Canvas(tools, bg="#232369")
toolsScrollBar = Scrollbar(tools, orient=VERTICAL)

angle = Scale(toolsButtons, orient="horizontal", from_=0, to=180, resolution=1, tickinterval=90, label='Angle (deg)', bg="#232369", fg=secondaryColorStr, troughcolor=secondaryColorStr, command=changeThetaMax, font=mainFont)
angle2 = Scale(toolsButtons, orient="horizontal", from_=1, to=3, resolution=0.01, tickinterval=1, label='Longueur du fil (mètres)', bg="#232369", fg=secondaryColorStr, troughcolor=secondaryColorStr, command=changeR, font=mainFont)
angle3 = Scale(toolsButtons, orient="horizontal", from_=1, to=10, resolution=1, tickinterval=2, label='Gravité (lieu)', bg="#232369", fg=secondaryColorStr, troughcolor=secondaryColorStr, command=changeG, font=mainFont)
angle4 = Scale(toolsButtons, orient="horizontal", from_=10, to=100, resolution=1, tickinterval=30, label='Temps de la simulation (sec)', bg="#232369", fg=secondaryColorStr, troughcolor=secondaryColorStr, command=changeT, font=mainFont)

infosPendule = Label(penduleSimulation, text="Période : 0 s", bg="#232369", fg=secondaryColorStr, font=mainFont)
infosPendule.place(relx=0.6, rely=0.9, relwidth=0.4, relheight=0.09)

	# Animation, partie majeure
animationPendule = Canvas(penduleSimulation, bg="#232369")
animationPendule.place(relx=0.025, rely=0.05, relheight=0.8, relwidth=0.95)

graphButton = Button(penduleSimulation, text="Lacher le pendule", bg="#232369", fg=secondaryColorStr, cursor="hand2", command=lambda:penduleAnimation(g, t), font=mainFont)
graphButton.place(relx=0.025, rely=0.92, relwidth=0.3, relheight=0.07)

penduleFig = Figure(figsize=(4, 4), dpi=100)
pendulePlot = penduleFig.add_subplot(111)

ax = penduleFig.gca()
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
pendulePlot.set_xlim([-pi, pi])
pendulePlot.set_ylim([-pi, pi])

(thetaMax, r, g, t) = (0, 1, 1, 10)
theta = (thetaMax)*sin(-pi/2)

pendulePlot.scatter([0, r*cos(theta-pi/2)], [0, r*sin(theta-pi/2)])
pendulePlot.plot([0, r*cos(theta-pi/2)], [0, r*sin(theta-pi/2)])

animationCanvas = FigureCanvasTkAgg(penduleFig, master = animationPendule)
animationCanvas.draw()
animationCanvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER)


# Panel de la simulation "Pendule de Newton"
penduleNSimulation = PanedWindow(main, bg=secondaryColorStr)

# Panel de la simulation "Boule"
bouleSimulation = PanedWindow(main, bg=secondaryColorStr)


# Pied de page #
footer = Frame(pyps, bg="#232369")
footer.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)

footerCredits = Label(footer, text="Version 1.0 | Par Nizar et Loïc", bg="#232369", fg=secondaryColorStr, font=mainFont)
footerCredits.place(relx=0.5, rely=0.5, anchor=CENTER)


# Logo #




# --------------------------------------------------------------------
# Lancement de la fenêtre
# --------------------------------------------------------------------

pyps.mainloop()
