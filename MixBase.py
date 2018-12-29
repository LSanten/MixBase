class InputTransition():
    """Input from user - Song A - Song B - Information about transition"""
    def __init__(self):
        self.song_a_name = None
        self.song_b_name = None

    def input_request(self):
        self.song_a_name = input('Please enter name of first song:  ')
        self.song_b_name = input('Please enter name of second song:  ')
        print('Here are song A and B:')
        print(self.song_a_name)
        print(self.song_b_name)


def Main():
    input_transition = InputTransition()
    input_transition.input_request()

if __name__ == '__main__':
    Main()
