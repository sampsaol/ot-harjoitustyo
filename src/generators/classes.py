from random import randint


class Classes:
    # A class that generates the playstyle that the player will be using,
    # or in other words the players class

    def __init__(self):
        # The constructor where the list of playable classes is defined.
        # The constructor also pseudorandomly chooses a class from the list
        self._classes = ["Two-Handed Warrior", "Battlemage", "One-Handed Warrior",
                         "Stealth Archer", "Assassin", "Berserker", "Night Blade"]
        self._random_class = self._classes[randint(0, len(self._classes)-1)]

    def generate_class(self):
        # A function, which when called upon returns the pseudorandomly chosen class
        return self._random_class

    def list_classes(self):
        # A function which returns a list of all the defined classes
        return self._classes
