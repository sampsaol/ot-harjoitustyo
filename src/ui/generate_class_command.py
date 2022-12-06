from services.character_service import CharacterService


class GenerateClassCommand:
    def __init__(self, character: CharacterService):
        self._character = character

    def run(self):
        character = self._character.generate_character()
        print(
            f"Your race will be {character[0]} and your class will be {character[1]}. Your primary questline is {character[2]}")
        return self._character
