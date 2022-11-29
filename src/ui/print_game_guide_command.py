from guide import Guide
from character_service import CharacterService


class PrintGameGuideCommand:
    def __init__(self, io, character):
        self._io = io
        self._list = character.list_generated_characters()
        self._guide = f"Choose which character you want a guide for, 0 will quit:\n"
        self._allowed_keys = []

    def run(self):
        for i in range(len(self._list)):
            self._guide += f"{i+1}: Your race will be {self._list[i][0]} and your class will be {self._list[i][1]}. Your primary questline is {self._list[i][2]}\n"
            self._allowed_keys.append(str(i+1))
        self._io.printout(self._guide)
        while True:
            key = self._io.read("Command: ")
            if key == "0":
                print("Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n3 generate a guide for a character\n")
                break
            elif key in self._allowed_keys:
                guide = Guide(
                    self._list[int(key)-1][1], self._list[int(key)-1][2])
                generated_guide = guide.generate_guide()
            else:
                self._io.printout("False input!")
                self._io.printout(self._guide)
                continue

            print(
                f"{int(key)}: Your race will be {self._list[int(key)-1][0]} and your class will be {self._list[int(key)-1][1]}. Your primary questline is {self._list[int(key)-1][2]}\n")
            print(
                f"You should primaly level {generated_guide[0]} skill and secondarily level {generated_guide[1]} skill. Your questline starts at {generated_guide[2]}\n")
            print("Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n3 generate a guide for a character\n")
            return generated_guide
