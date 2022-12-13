from pathlib import Path
from config import data_file_path


class CSRepository:
    """A class for saving generated characters into a file
    """
    def __init__(self, file_path):
        """The constructor where the path is defined for the file where the characters are saved to

        Args:
            file_path: Path to the file where the characters are saved to
        """
        self._file_path = file_path

    def find_all(self):
        """A function for making a list of all the lines of the file

        Returns:
            _list_ : returns a list of all the characters that are generated by using the _read() function
            to convert the lines into doubles in a list
        """
        return self._read()

    def find_by_line(self, line):
        """A function for getting a certain line from the file. First the function gets the whole file and
        converts it to a list and then returns the wanted line

        Args:
            line (_str_): Character input for getting the wanted line from the file

        Returns:
            _double_: returns a double of the contents of the line that was seeked for
        """
        characters = self.find_all()
        line = int(line)
        line -= 1
        return characters[line]

    def add_character(self, character):
        """A function for adding characters to the file

        Args:
            character (_double_): A double that is generated in the CharacterService module and is then added to the list
            of generated characters

        Returns:
            _double_: returns the same character that was given after adding it into the file
        """
        characters = self.find_all()
        characters.append(character)
        self._write(characters)
        return character

    def delete_all(self):
        """A function for deleting all of the data in the file
        """
        self._write([])

    def _file_exist_check(self):
        """A function for making sure that the file that is used for saving generated characters exists
        """
        Path(self._file_path).touch()

    def _read(self):
        """A function that reads the contents of the file and converts them into a list with doubles that contain 
        the character information

        Returns:
            _list_: returns a list of all the generated characters
        """
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
        """A function for writing the file

        Args:
            characters (_list_): Contains a list that is then written into the file. If the list is empty then the file
            will be emptied as well. This is used mostly to add characters to the file by adding them to the list first
            through the add_character() function
        """
        self._file_exist_check()
        with open(self._file_path, "w") as file:
            for character in characters:
                race = character[0]
                playclass = character[1]
                quest = character[2]
                row = f"{race};{playclass};{quest}"
                file.write(row+"\n")


character_service_repository = CSRepository(data_file_path)
