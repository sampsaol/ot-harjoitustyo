from services.character_service import CharacterService


class PrintGeneratedCommand:
    """A UI class for printing out all the previously generated characters
    """

    def __init__(self, character: CharacterService):
        """The constructor of the class

        Args:
            character (CharacterService): an object made of the CharacterService class to access the list
            that has the generated characters
        """
        self._service = character

    def run(self):
        """the run function that prints out all the generated characters or alternatively a notification if no characters
        are yet generated.

        Returns:
            _list_: returns a list of all the generated characters if there is further need for it.
        """
        retlist = self._service.list_generated_characters()
        if len(retlist) == 0:
            print("You have not generated any characters!")
            return retlist
        for i in retlist:
            print(
                f"Your race will be {i[0]} and your class will be {i[1]}. Your primary questline is {i[2]}")
        return retlist
