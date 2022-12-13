from services.character_service import CharacterService


class DeleteAllCommand:
    """A class for deleting all of the saved characters
    """
    def __init__(self, character: CharacterService):
        """The constructor of the class

        Args:
            character (CharacterService): an object made of the CharacterService class that is used to access the delete command
        """
        self._character = character
        self._game_guide = "Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n3 generate a guide for a character\n\
4 delete generated characters\n"

    def run(self):
        """the run function that deletes all of the listed characters and prints the game guide
        """
        self._character.delete_listed_characters()
        print(self._game_guide)
