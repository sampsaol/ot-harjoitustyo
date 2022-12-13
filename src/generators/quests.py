class Quests:
    """A class for generating the primary questline that the player should do first based on their
    playstyle
    """
    def __init__(self, generated_class):
        """The constructor of the class where the questlines are defined

        Args:
            generated_class (_str_): the playstyle that the character uses
        """
        self._questlines = ["Dark Brotherhood", "The Companions",
                            "The Thieves Guild", "The College of Winterhold"]
        self._class = generated_class

    def primary_questline(self):
        """A function that chooses the primary questline

        Returns:
            _str_: returns the primary questline
        """
        if self._class in ["Two-Handed Warrior", "One-Handed Warrior", "Berserker"]:
            retval = self._questlines[1]
        elif self._class in ["Assassin", "Night Blade"]:
            retval = self._questlines[0]
        elif self._class in ["Stealth Archer"]:
            retval = self._questlines[2]
        else:
            retval = self._questlines[3]
        return retval
