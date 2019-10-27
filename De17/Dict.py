import pickle



def init_database():
    database = pickle.load(open('userData/database.p', 'rb'))
    # print(database)
    userName = raw_input('Please enter your name: ')
    if userName in database:
        print('welcome back ' + userName + '.')
        database[userName]['logins'] +=1
    else:
        database[userName] = { 'logins' : 1,
                               'digit0attempted': 0,
                               'digit1attempted': 0,
                               'digit2attempted': 0,
                               'digit3attempted': 0,
                               'digit4attempted': 0,
                               'digit5attempted': 0,
                               'digit6attempted': 0,
                               'digit7attempted': 0,
                               'digit8attempted': 0,
                               'digit9attempted': 0 }

        print('welcome ' + userName + '.')

    pickle.dump(database,open('userData/database.p','wb'))
    return userName, database

def input_database_sign(userName, signTryed):
    database = pickle.load(open('userData/database.p', 'rb'))

    database[userName][signTryed] +=1
    pickle.dump(database,open('userData/database.p','wb'))


    return database
