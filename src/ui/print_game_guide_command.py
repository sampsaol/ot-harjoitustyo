from generators.guide import Guide
from services.character_service import CharacterService


class PrintGameGuideCommand:
    def __init__(self, io, service: CharacterService):
        self._io = io
        self._service = service

    def run(self):
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
                print("Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n3 generate a guide for a character\n")
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
            print("Commands:\n0 quit\n1 generate a playthrough\n2 print all generated playthroughs\n3 generate a guide for a character\n")
            return generated_guide
