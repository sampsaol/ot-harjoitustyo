from generators.guide import Guide
from services.character_service import CharacterService


class PrintGameGuideCommand:
    """A UI class for generating playthrough guides for characters
    """

    def __init__(self, io, service: CharacterService):
        """The constructor where the used IO and CharacterService is defined

        Args:
            io : The used Input-Output application, other than in test cases the command_io.py file is mostly used in this program
            service (CharacterService): an object made of the CharacterService class. Gives acces to characterservice commands
            for generating playthrough guides
        """
        self._io = io
        self._service = service
        self._game_guide = "Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n3 generate a guide for a character\n\
4 delete generated characters\n"

    def run(self):
        """The run function for generating a playthrough guide. The function asks for user input where the user chooses
        the character he wants a gameguide for. A double for the playthrough guide is then generated in the Guide class
        and this UI function prints the guide for the user to see.

        Returns:
            _double_: returns a double that is generated in the Guide class if there is further need for it.
        """
        guidetext = f"Choose which character you want a guide for, 0 will return to main menu:\n"
        allowed_keys = []
        rowlength = self._service.repository.find_all()
        for i in range(len(rowlength)):
            guidetext += f"{i+1}: Your race will be {rowlength[i][0]} and your class will be {rowlength[i][1]}. Your primary questline is to seek dick in {rowlength[i][2]}\n"
            allowed_keys.append(str(i+1))
        self._io.printout(guidetext)
        while True:
            key = self._io.read("Command: ")
            if key == "0":
                print(self._game_guide)
                break
            elif key in allowed_keys:
                character = self._service.repository.find_by_line(key)
                guide = Guide(character[1], character[2])
                generated_guide = guide.generate_guide()
            else:
                self._io.printout("False input!")
                self._io.printout(guidetext)
                continue

            print(
                f"{int(key)}: Your race will be {rowlength[int(key)-1][0]} and your class will be {rowlength[int(key)-1][1]}. Your primary questline is {rowlength[int(key)-1][2]}\n")
            print(
                f"You should primaly level the {generated_guide[0]} skill(s) and secondarily level the {generated_guide[1]} skill(s). Your questline starts at {generated_guide[2]}\n")
            print(self._game_guide)
            return generated_guide
