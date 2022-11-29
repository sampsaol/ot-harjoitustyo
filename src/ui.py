from classes import Classes
from quests import Quests
from races import Races

class UserInterface:
    ### A class made for the UI of the program which still for now is text-based
    def __init__(self, io):
        ### The constructor that takes some Input-Output class as an argument

        ### A list that holds the generated characters
        self._generated_playthroughs = []

        ### A list that holds all of the text that has been printed except the guide text
        self._printed_text = []

        ### Guide text for commands
        self._guide_text = "Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n"

        ### Variable for Input-Output
        self._io = io

    def start(self):
        ### A function that starts the program

        ### The guide text is printed
        print(self._guide_text)
        while True:
            ### Input is read and saved to the key variable
            key = self._io.read("command: ")

            ### If input is not in the predefined command list, False input! is printed as well as the guide text and the loop starts over
            if key not in ["0", "1", "2"]:
                self._io.printout("False input!")
                self._printed_text.append("False input!")
                print(self._guide_text)
                continue

            ### Input for stopping the application
            if key == "0":
                break

            ### Input for generating a character as well as printing the race, class and questline. Character is then added to the generated playthroughs list
            elif key == "1":
                playstyle = Classes().generate_class()
                race = Races().generate_race()
                quest = Quests(playstyle).primary_questline()

                playthrough = f"Your race will be {race} and your class will be {playstyle}. Your primary questline is {quest}"
                self._io.printout(playthrough)
                self._printed_text.append(playthrough)
                self._generated_playthroughs.append(playthrough)
            
            ### Input for printing out all of the generated characters
            else:
                for i in self._generated_playthroughs:
                    self._printed_text.append(i)
                    self._io.printout(i)

