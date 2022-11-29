from character_service import CharacterService


class PrintGeneratedCommand:
    def __init__(self, character: CharacterService):
        self._list = character.list_generated_characters()

    def run(self):
        for i in self._list:
            print(
                f"Your race will be {i[0]} and your class will be {i[1]}. Your primary questline is {i[2]}")
        return self._list
