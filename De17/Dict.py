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
                               'digit10attempted': 0,}

        print('welcome ' + userName + '.')

    pickle.dump(database,open('userData/database.p','wb'))
    return userName, database

def input_database_sign(userName, signTryed):
    database = pickle.load(open('userData/database.p', 'rb'))
    database[userName][signTryed] += 1

    pickle.dump(database,open('userData/database.p','wb'))

    return dict(database) #time_attempted
