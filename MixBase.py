"""
Leon Santen

IMPORTANT:
There are two different files: MixBase.py and run.py
- MixBase.py is for development purposes and creates the database transition_database.db which contains fake information
- run.py is for usage purposes anc creates the database run.db which contains real valuable data
"""

import sqlite3
from time import sleep

class DatabaseManagement():
    """Class for database management, initialization etc"""

    def __init__(self):
        pass

    def connect_to_database_and_cursor(self):
        """Connect to database and creates new database if not existent"""
        global conn
        conn = sqlite3.connect('transition_database.db') #is being created automatically if doesn't exist - otherwise uses existing one
        #TODO change database name to variable based on function input
        global c
        c = conn.cursor()

    def create_table(self):
        """Create table called 'transitionTable' in database calles 'transition_database.db'"""
        c.execute('CREATE TABLE IF NOT EXISTS transitionTable(id INTEGER primary key autoincrement, song_a_name TEXT not null, song_a_artist TEXT not null, song_b_name TEXT not null, song_b_artist TEXT not null, info TEXT not null)')
        #TODO change table name to variable based on name input from function

    def close_connection(self):
        c.close()
        conn.close()

class InputTransition():
    """Input from user - Song A - Song B - Information about transition
    - song_a_name --  string - should not be NONE to be saved in databank --> doesn't accept NULL value
    - song_a_artist -- string - look above
    - song_b_name -- string - look above
    - song_b_artist -- string - look above
    - transition_information -- string - look above
    """

    def __init__(self):
        self.song_a_name = None
        self.song_a_artist = None
        self.song_b_name = None
        self.song_b_artist = None
        self.transition_information = None

    def input_request(self):
        print('\n- - - ENTER NEW TRANSITION BELOW - - -\n' )
        self.song_a_name = input('NAME of song # 1 :  ')
        self.song_a_artist = input('ARTIST of song # 1 :  ')
        self.song_b_name = input('NAME of song # 2 :  ')
        self.song_b_artist = input('ARTIST of song # 2 :  ')
        self.transition_information = input('Please enter information about the transition:   ')
        print('\n--- Here are song # 1 and # 2 : ---')
        print('# 1 :  ',self.song_a_name, '-', self.song_a_artist)
        print('# 2 :  ',self.song_b_name, '-', self.song_b_artist)
        print('INFO:  ', self.transition_information)

    def data_entry(self):
        """Saves  transition data in table """
        c.execute("INSERT INTO transitionTable(song_a_name, song_a_artist, song_b_name, song_b_artist, info) VALUES(?, ?, ?, ?, ?)", (self.song_a_name, self.song_a_artist, self.song_b_name, self.song_b_artist, self.transition_information))
        conn.commit()
        print('\nDATA SUCCESSFULLY ADDED !')
        sleep(1.2)
        print('----------------------------')


class Menu():
    """Controls what the programm should be executing: input transition, search for transition etc.
    - state -- string - different states of the state machine: 'menu', 'add', 'search', 'quit'
    """

    def __init__(self):
        self.state = 'menu'

    def ask_for_action(self):
        print("\nWhat do you want to do? Type\n\n --> add \t- to add a new transition\n --> search \t- to search for a transition with the trackname\n --> quit \t- to close the program\n")
        self.state = input(' --> ')

    def execute_action(self):
        """executes the action of the state machine - includes the state 'menu' which asks for an action"""

        if self.state == 'menu':
            self.ask_for_action()

        elif self.state == 'add':
            input_transition = InputTransition() #instantiate InputTransition-class again every loop
            input_transition.input_request() #request information about songs and save as attributes of class object
            input_transition.data_entry() #saves transition data in table

            self.state = 'menu' #starts with menu state again

        elif self.state == 'search':
            print('\n\nThis does not work currently!')
            self.state = 'menu'
            sleep(2)

        elif self.state == 'quit':
            pass

        else:
            print('\nNO VALID ENTRY')
            sleep(1)
            self.state = 'menu'

def Main():
    database = DatabaseManagement() #instantiate database class to work with database
    database.connect_to_database_and_cursor() #opens connection to database and opens cursor
    database.create_table() # creates table in database
    menu = Menu() #instantiate menu that is terminal based

    while True:
        menu.execute_action()
        if menu.state == 'quit':
            break

    database.close_connection()

if __name__ == '__main__':
    Main()
