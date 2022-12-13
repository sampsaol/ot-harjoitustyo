from random import randint


class Races:
    """A class that pseudorandomly chooses the race that the player should pick
    """

    def __init__(self):
        """The constructor where the playable races are defined and a race is randomly chosen
        """
        self._races = ["Altmer / High Elf", "Argonian", "Bosmer / Wood Elf",
                       "Breton", "Dunmer / Dark Elf", "Imperial", "Khajiit", "Nord",
                       "Orsimer / Orc", "Redguard"]
        self._random_race = self._races[randint(0, len(self._races)-1)]

    def generate_race(self):
        """A function that returns the generated race

        Returns:
            _str_: the generated race
        """
        return self._random_race
