class ConsoleIO:
    ### A class which imitates inputs and outputs
    def __init__(self):
        ### constructor which right now has no use
        self._text = None

    def printout(self, text):
        ### A function which prints out given text
        print(text)
        return text
    def read(self, text):
        ### A function which reads user input
        retval = input(text)
        return retval