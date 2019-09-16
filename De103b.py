import pickle
import numpy as np
from Reader import READER

reader = READER()
reader.Restart_Directory()
reader.load_and_print()