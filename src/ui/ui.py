from ui.generate_class_command import GenerateClassCommand
from ui.print_generated_command import PrintGeneratedCommand
from ui.print_game_guide_command import PrintGameGuideCommand
from ui.delete_all_command import DeleteAllCommand

class UserInterface:
    # A class made for the UI of the program which still for now is text-based
    def __init__(self, io, service):
        # The constructor that takes an Input-Output class and a character-service class as arguments

        # Guide text for commands
        self._guide_text = "Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n3 generate a guide for a character\n4 delete generated characters\n"

        # Variable for Input-Output
        self._io = io
        # Variable for the character-service
        self._service = service
        # Variable for commands
        self._commands = {
            "0": "Stop",
            "1": GenerateClassCommand(self._service),
            "2": PrintGeneratedCommand(self._service),
            "3": PrintGameGuideCommand(self._io, self._service),
            "4": DeleteAllCommand(self._service)
        }

    def start(self):
        # A function that starts the program

        # The guide text is printed
        print(self._guide_text)
        while True:
            # Input is read and saved to the key variable
            key = self._io.read("Command: ")

            # If input is not in the predefined command list, False input! is printed as well as the guide text and the loop starts over
            if key not in self._commands:
                self._io.printout("False input!")
                print(self._guide_text)
                continue

            # Input for stopping the application
            if key == "0":
                break
            else:
                self._commands[key].run()
