class Quests:
    def __init__(self, generated_class):
        self._questlines = ["Dark Brotherhood", "The Companions", "The Thieves Guild", "The College of Winterhold"]
        self._class = generated_class

    def primary_questline(self):
        if self._class in ["Two-Handed Warrior", "One-Handed Warrior", "Berserker"]:
            return self._questlines[1]
        elif self._class in ["Assassin", "Night Blade"]:
            return self._questlines[0]
        elif self._class in ["Stealth Archer"]:
            return self._questlines[2]
        else:
            return self._questlines[3]