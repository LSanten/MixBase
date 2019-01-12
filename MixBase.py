import sqlite3

conn = sqlite3.connect('transition_database.db') #is being created automatically if doesn't exist - otherwise uses existing one
c = conn.cursor()

def create_table():
    """Create table calles 'transitionTable' in database calles 'transition_database.db'"""
    c.execute('CREATE TABLE IF NOT EXISTS transitionTable(id INTEGER primary key autoincrement, song_a TEXT not null, song_b TEXT not null, info TEXT not null)')


class InputTransition():
    """Input from user - Song A - Song B - Information about transition"""
    def __init__(self):
        self.song_a_name = None
        self.song_b_name = None
        self.transition_information = None

    def input_request(self):
        self.song_a_name = input('Please enter name of first song:  ')
        self.song_b_name = input('Please enter name of second song:  ')
        self.transition_information = input('Please enter information about the transition:   ')
        print('Here are song A and B:')
        print(self.song_a_name)
        print(self.song_b_name)
        print(self.transition_information)

    def data_entry(self):
        c.execute("INSERT INTO transitionTable(song_a, song_b, info) VALUES('TEST A', 'SELF B', 'INFORMATION')")
        conn.commit()
        c.close()
        conn.close()

def Main():
    create_table()
    while True:
        input_transition = InputTransition()
        input_transition.input_request() #request information about songs and save as attributes of class object

        # break if song name or info is 'quit' (probablye temporary solution) - if not saves information in database
        if input_transition.song_a_name == 'quit' or input_transition.song_b_name == 'quit' or input_transition.transition_information == 'quit':
            break

        input_transition.data_entry()
if __name__ == '__main__':
    Main()
