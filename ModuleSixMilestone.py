#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

def instructions():
    print('You are starting in the Great Hall')
    print('')
    print('Please Enter: South, North, East, West')
    print('')
    print('When finished enter Exit to quit game')
    print('')

instructions()
user_input = input()
location = 'Great Hall'


while user_input != 'exit' and user_input != 'Exit':
    if user_input == 'South' and location == 'Great Hall':
        location = rooms['Great Hall']['South']
        print('Your location is', location)
    elif location == rooms['Great Hall']['South'] and user_input == 'East':
        location = rooms['Bedroom']['East']
        print('Your location is', location)
    elif location == rooms['Great Hall']['South'] and user_input == 'North':
        location = 'Great Hall'
        print('Your location is', location)
    elif location == 'Cellar' and user_input == 'West':
        location = rooms['Cellar']['West']
        print('Your location is', location)
    else:
        print('Error, Enter Again')
        print('')
        print('Your location is', location)
    user_input = input()
print("You have exited the game")
