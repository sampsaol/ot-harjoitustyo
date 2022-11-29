from classes import Classes
from quests import Quests
from races import Races


class CharacterService:
    # A class that generates pseudorandom playable characters for the player
    # The class also upholds a list of the generated characters
    def __init__(self):
        self._generated_characters = []

    def generate_character(self):
        # Function that generates the character
        race = Races().generate_race()
        playclass = Classes().generate_class()
        quest = Quests(playclass).primary_questline()
        self._generated_characters.append((race, playclass, quest))
        return (race, playclass, quest)

    def list_generated_characters(self):
        # Function that returns a list of generated characters
        return self._generated_characters
