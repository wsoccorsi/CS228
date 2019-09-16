import  pickle
import  numpy
import os
class READER:

    def load_and_print(self):
        pickle_in = open("userData/gesture", "rb")
        gesture_data = pickle.load(pickle_in)
        print(gesture_data)

    def Number_Of_Gesture(self):
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)

    def Restart_Directory(self):
        print('hiiiii')
        print(os.getcwd())
        os.remove('userData')
        os.mkdir('userData')