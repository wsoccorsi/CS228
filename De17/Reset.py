import pickle
dictionary = {}
pickle.dump(dictionary,open('userData/database.p','wb'))
topTimeSigned = { '0' : {},
                  "1" : {},
                  '2' : {},
                  '3' : {},
                  '4' : {},
                  '5' : {},
                  '6' : {},
                  '7' : {},
                  '8' : {},
                  '9' : {},}
pickle.dump(topTimeSigned,open('userData/topTime.p','wb'))