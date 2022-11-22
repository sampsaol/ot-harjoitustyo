from classes import Classes
from quests import Quests
from races import Races
from command_io import ConsoleIO
### Code still lacks comments due to shortness of time ###

class UserInterface:
    def __init__(self):
        self._generated_playthroughs = []
        self._guide_text = "Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n"
        self._io = ConsoleIO()

    def start(self):
        print(self._guide_text)
        while True:
            key = self._io.read("command: ")
            if key not in ["0", "1", "2"]:
                print("False input!")
                print(self._guide_text)
                continue
            if key == "0":
                break
            elif key == "1":
                playstyle = Classes().generate_class()
                race = Races().generate_race()
                quest = Quests(playstyle).primary_questline()

                playthrough = f"Your race will be {race} and your class will be {playstyle}. Your primary questline is {quest}"
                print(playthrough)
                self._generated_playthroughs.append(playthrough)
            else:
                for i in self._generated_playthroughs:
                    print(i)
