from ui.generate_class_command import GenerateClassCommand
from ui.print_generated_command import PrintGeneratedCommand
from ui.print_game_guide_command import PrintGameGuideCommand
from ui.delete_all_command import DeleteAllCommand


class UserInterface:
    """A class for the UI which for now at least is text based
    """
    def __init__(self, io, service):
        """The constructor that creates the UI

        Args:
            io : The used Input-Output application, other than in test-cases the command_io.py module is mostly used in this program

            service (CharacterService): an object made of the CharacterService class. Gives acces to characterservice commands
            and is given as an argument for all the UI "subclasses"
        """

        self._guide_text = "Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n3 generate a guide for a character\n4 delete generated characters\n"
        self._io = io
        self._service = service
        self._commands = {
            "0": "Stop",
            "1": GenerateClassCommand(self._service),
            "2": PrintGeneratedCommand(self._service),
            "3": PrintGameGuideCommand(self._io, self._service),
            "4": DeleteAllCommand(self._service)
        }

    def start(self):
        """A function for running the UI. It prints out a guide for using the UI in the beginning, every time a false command is given
        and when returning from different UI functions that use the IO
        """
        print(self._guide_text)
        while True:
            key = self._io.read("Command: ")

            if key not in self._commands:
                self._io.printout("False input!")
                print(self._guide_text)
                continue
            if key == "0":
                break
            else:
                self._commands[key].run()
