import pickle
dictionary = {}
pickle.dump(dictionary,open('userData/database.p','wb'))
time_attempted = {}
pickle.dump(time_attempted,open('userData/time_attempted.p','wb'))