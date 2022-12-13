from services.character_service import CharacterService


class GenerateClassCommand:
    """A UI class for generating characters
    """

    def __init__(self, character: CharacterService):
        """The constructor of the class 

        Args:
            character (CharacterService): an object made of the CharacterService class that is used to generate a new character
        """
        self._character = character

    def run(self):
        """The run function for generating a character

        Returns:
            _double_: returns the character as a double that is in format: (race, class, quest)
        """
        character = self._character.generate_character()
        print(
            f"Your race will be {character[0]} and your class will be {character[1]}. Your primary questline is {character[2]}")
        return self._character
