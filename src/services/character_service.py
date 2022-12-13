from generators.classes import Classes
from generators.quests import Quests
from generators.races import Races
from repositories.character_service_repository import character_service_repository as default_repository


class CharacterService:
    """A class for generating random characters for the user
    """
    def __init__(self):
        """The constructor where the repository is chosen for saving characters
        """
        self.repository = default_repository

    def generate_character(self):
        """Function for generating characters. Uses modules from the generator directory

        Returns:
            _double_: returns a double that has the characters race, class and primary questline
        """
        race = Races().generate_race()
        playclass = Classes().generate_class()
        quest = Quests(playclass).primary_questline()
        character = (race, playclass, quest)
        self.repository.add_character(character)
        return (character)

    def list_generated_characters(self):
        """A function for returning a list of all the generated characters.

        Returns:
            _list_: returns a list of all the generated characters
        """
        characters = self.repository.find_all()
        return characters

    def delete_listed_characters(self):
        """A function for deleting all of the generated characters
        """
        self.repository.delete_all()
