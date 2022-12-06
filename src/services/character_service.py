from generators.classes import Classes
from generators.quests import Quests
from generators.races import Races
from repositories.character_service_repository import character_service_repository as default_repository


class CharacterService:
    # A class that generates pseudorandom playable characters for the player
    # The class also upholds a list of the generated characters
    def __init__(self):
        self.repository = default_repository

    def generate_character(self):
        # Function that generates the character
        race = Races().generate_race()
        playclass = Classes().generate_class()
        quest = Quests(playclass).primary_questline()
        character = (race, playclass, quest)
        self.repository.add_character(character)
        return (character)

    def list_generated_characters(self):
        # Function that returns a list of generated characters
        characters = self.repository.find_all()
        self.repository._write(characters)
        return characters

    def delete_listed_characters(self):
        self.repository.delete_all()