from services.character_service import CharacterService


class DeleteAllCommand:
    def __init__(self, character: CharacterService):
        self._character = character

    def run(self):
        self._character.delete_listed_characters()
