import pickle

database = pickle.load(open('userData/database.p','rb'))

print(database)
userName = raw_input('Please enter your name: ')
if userName in database:
    print('welcome back ' + userName + '.')
else:
    database[userName] = {}
    print('welcome ' + userName + '.')

pickle.dump(database,open('userData/database.p','wb'))