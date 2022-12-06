from pathlib import Path
from config import data_file_path

class CSRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def find_by_line(self, line):
        characters = self.find_all()
        line = int(line)
        line -= 1
        return characters[line]

    def add_character(self, character):
        characters = self.find_all()
        characters.append(character)
        self._write(characters)
        return character

    def delete_all(self):
        self._write([])

    def _file_exist_check(self):
        Path(self._file_path).touch()

    def _read(self):
        characters = []
        self._file_exist_check()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                generated_values = row.split(";")
                race = generated_values[0]
                playclass = generated_values[1]
                quest = generated_values[2]
                characters.append((race, playclass, quest))
        return characters

    def _write(self, characters):
        self._file_exist_check()
        with open(self._file_path, "w") as file:
            for character in characters:
                race = character[0]
                playclass = character[1]
                quest = character[2]
                row = f"{race};{playclass};{quest}"
                file.write(row+"\n")

character_service_repository = CSRepository(data_file_path)