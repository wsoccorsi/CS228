import  pickle
import  numpy

class READER:

    def load_and_print(self):
        pickle_in = open("userData/gesture", "rb")
        gesture_data = pickle.load(pickle_in)
        print(gesture_data)