from random import randint

class Classes:
    def __init__(self):
        self._classes = ["Two-Handed Warrior", "Battlemage", "One-Handed Warrior", "Stealth Archer", "Assassin", "Berserker", "Night Blade"]
        self._random_class = self._classes[randint(0, len(self._classes)-1)]

    def generate_class(self):
        return self._random_class

    def list_classes(self):
        return self._classes