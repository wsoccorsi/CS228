import pickle
import numpy as np
from Reader import READER
from pygameWindow_De103 import PYGAME_WINDOW

pw = PYGAME_WINDOW()

reader = READER(pw)
reader.Print_Gestures()
reader.Draw_Gestures()

# reader.Restart_Directory()
