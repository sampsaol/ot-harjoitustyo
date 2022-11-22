from random import randint

class Races:
    def __init__(self):
        self._races = ["Altmer / High Elf", "Argonian", "Bosmer / Wood Elf", "Breton", "Dunmer / Dark Elf", "Imperial", "Khajiit", "Nord", "Orsimer / Orc", "Redguard"]
        self._random_race = self._races[randint(0, len(self._races)-1)]

    def generate_race(self):
        return self._random_race