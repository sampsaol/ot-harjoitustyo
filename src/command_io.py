class ConsoleIO:
    def __init__(self):
        self._text = None

    def printout(self, text):
        print(text)
        return text
    def read(self, text):
        retval = input(text)
        return retval