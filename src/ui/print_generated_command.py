from services.character_service import CharacterService


class PrintGeneratedCommand:
    def __init__(self, character: CharacterService):
        self._service = character

    def run(self):
        retlist = self._service.list_generated_characters()
        for i in retlist:
            print(
                f"Your race will be {i[0]} and your class will be {i[1]}. Your primary questline is {i[2]}")
        return retlist
