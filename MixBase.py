import sqlite3

class DatabaseManagement():
    """Class for database management, initialization etc"""
    def __init__(self):
        pass

    def connect_to_database_and_cursor(self, database_name):
        """Connect to database and creates new database if not existent"""
        global conn
        conn = sqlite3.connect('transition_database.db') #is being created automatically if doesn't exist - otherwise uses existing one # TODO change database name to variable based on function input
        global c
        c = conn.cursor()

    def create_table(self, transitionTable_name):
        """Create table called 'transitionTable' in database calles 'transition_database.db'"""
        c.execute('CREATE TABLE IF NOT EXISTS transitionTable(id INTEGER primary key autoincrement, song_a_name TEXT not null, song_a_artist TEXT not null, song_b_name TEXT not null, song_b_artist TEXT not null, info TEXT not null)')
        #TODO change table name to variable based on name input from function

    def close_connection(self):
        c.close()
        conn.close()

class InputTransition():
    """Input from user - Song A - Song B - Information about transition"""
    def __init__(self):
        self.song_a_name = None
        self.song_a_artist = '-'
        self.song_b_name = None
        self.song_b_artist = '-'
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




def Main():
    database = DatabaseManagement() #instantiate database class to work with database
    database.connect_to_database_and_cursor('transition_database.db') #opens connection to database and opens cursor
    database.create_table('transitionTable') # creates table in database

    while True: #while loop to keep adding songs running
        input_transition = InputTransition() #instantiate InputTransition-class again every loop
        input_transition.input_request() #request information about songs and save as attributes of class object

        # break if song name or info is 'quit' (probablye temporary solution) - if not saves information in database
        if input_transition.song_a_name == 'quit' or input_transition.song_b_name == 'quit' or input_transition.transition_information == 'quit':
            break

        input_transition.data_entry()

    database.close_connection()
if __name__ == '__main__':
    Main()
