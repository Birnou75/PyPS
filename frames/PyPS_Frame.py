# PyPS_Frame -> Fichier constituant la fenêtre principale du logiciel

# --------------------------------------------------------------------
# Importations / Initialisation de la fenêtre
# --------------------------------------------------------------------

from tkinter import *

pyps = Tk()

# --------------------------------------------------------------------
# Construction de la fenêtre
# --------------------------------------------------------------------

pyps.title("PyPS | Python Physics Simulator")


"""
pyps.iconbitmap("pyps_logo.ico")
"""

# --------------------------------------------------------------------
# Lancement de la fenêtre
# --------------------------------------------------------------------
pyps.mainloop()