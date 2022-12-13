class ConsoleIO:
    """A class which imitates inputs and outputs
    """

    def __init__(self):
        """The constructor of the class
        """
        self._text = None

    def printout(self, text):
        """A function that prints out given text

        Args:
            text (_str_): the text that is printed

        Returns:
            _str_: returns the same text
        """
        print(text)
        return text

    def read(self, text):
        """A function for reading user input

        Args:
            text (_str_): information text that is shown to the user

        Returns:
            _str_: returns the text that the user inputs
        """
        retval = input(text)
        return retval

    """def class_printout(self, race, playstyle, quest):
        val = f"Your race will be {race} and your \
            class will be {playstyle}. Your primary questline is {quest}"
        print(val)
        return val
        """
