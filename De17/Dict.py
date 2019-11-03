import pickle



def init_database():

    database = pickle.load(open('userData/database.p', 'rb'))
    userName = raw_input('Please enter your name: ')

    if userName in database:
        print('welcome back ' + userName + '.')
        database[userName]['logins']['attempts'] +=1

    else:
        database[userName] = { 'logins' : {'attempts' : 1},
                               'digit0attempted': 0,
                               'digit1attempted': 0,
                               'digit2attempted': 0, #digit two will be picked
                               'digit3attempted': 0,
                               'digit4attempted': 0,
                               'digit5attempted': 0,
                               'digit6attempted': 0,
                               'digit7attempted': 0,
                               'digit8attempted': 0,
                               'digit9attempted': 0,
                               'digit10attempted': 0,

                               #im aware this is bad code and I should refactor my dict but im lazy!
                               'mean0time': 0,
                               'mean1time' : 0,
                               'mean2time' : 0,
                               'mean3time' : 0,
                               'mean4time' : 0,
                               'mean5time' : 0,
                               'mean6time' : 0,
                               'mean7time' : 0,
                               'mean8time' : 0,
                               'mean9time' : 0,
                               }

        print('welcome ' + userName + '.')

    pickle.dump(database,open('userData/database.p','wb'))
    return userName, database

def input_database_sign(userName, signTryed):
    database = pickle.load(open('userData/database.p', 'rb'))
    database[userName][signTryed] += 1
    pickle.dump(database,open('userData/database.p','wb'))

    return dict(database) #time_attempted

def update_database_time(userName, signTryed, timeTaken):
    database = pickle.load(open('userData/database.p', 'rb'))
    database[userName][signTryed] = (database[userName][signTryed] + timeTaken)/database[userName][signTryed] if database[userName][signTryed] != 0 else timeTaken
    pickle.dump(database,open('userData/database.p','wb'))

    return database