from random import randint


class Classes:
    """A class for pseudorandomly choosing the playstyle for the character
    """

    def __init__(self):
        """The constructor of the class where the playable playstyles are defined and the 
        random class is chosen from the list
        """
        self._classes = ["Two-Handed Warrior", "Battlemage", "One-Handed Warrior",
                         "Stealth Archer", "Assassin", "Berserker", "Night Blade"]
        self._random_class = self._classes[randint(0, len(self._classes)-1)]

    def generate_class(self):
        """A function that returns the generated playstyle

        Returns:
            _str_: returns the generated playstyle
        """
        return self._random_class

    def list_classes(self):
        """A function for returning a list of all the defined playstyles

        Returns:
            _list_: list of the defined playstyles
        """
        return self._classes
