class Quests:
    # A class that generates which questline the player should do based on the players class
    def __init__(self, generated_class):
        # The constructor where the questlines are defined
        #  and which takes the class that was generated as one argument
        self._questlines = ["Dark Brotherhood", "The Companions",
                            "The Thieves Guild", "The College of Winterhold"]
        self._class = generated_class

    def primary_questline(self):
        # A function that uses the generated class to choose which questline should be done
        if self._class in ["Two-Handed Warrior", "One-Handed Warrior", "Berserker"]:
            retval = self._questlines[1]
        elif self._class in ["Assassin", "Night Blade"]:
            retval = self._questlines[0]
        elif self._class in ["Stealth Archer"]:
            retval = self._questlines[2]
        else:
            retval = self._questlines[3]
        return retval
