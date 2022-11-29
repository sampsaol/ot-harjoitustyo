class Guide:
    # A class that generates a guide based on the class that the player is using
    # as well as the location where to start the questline
    def __init__(self, playclass, quest):
        # constructor where all the major skills that the player should level are listed
        self._armorlist = ["Light Armor", "Heavy Armor"]
        self._attacklist = ["One-Handed", "Two-Handed",
                            "Destruction", "Archery", "Block"]
        self._misclist = ["Sneak", "Illusion"]
        self._playclass = playclass
        self._quest = quest

    def generate_guide(self):
        # Function for generating guides in the form of primary/secondary skills for the class
        if self._playclass == "Two-Handed Warrior":
            retlist = [self._attacklist[1], self._armorlist[1]]
        elif self._playclass == "One-Handed Warrior":
            retlist = [self._attacklist[0], "Heavy Armor- and Block"]
        elif self._playclass == "Battlemage":
            retlist = [self._attacklist[2], self._armorlist[0]]
        elif self._playclass == "Stealth Archer":
            retlist = [self._attacklist[3], self._misclist[0]]
        elif self._playclass == "Assassin":
            retlist = [self._attacklist[0], self._misclist[0]]
        elif self._playclass == "Berserker":
            retlist = [self._attacklist[0], self._armorlist[1]]
        else:
            retlist = ["Illusion- and One-Handed", self._misclist[0]]
    # Part of the function where the starting point of the questline is defined
        if self._quest == "The College of Winterhold":
            retlist.append("Winterhold")
        elif self._quest == "The Companions":
            retlist.append("Whiterun")
        elif self._quest == "The Thieves Guild":
            retlist.append("Riften")
        else:
            retlist.append("Windhelm (speak to innkeepers for gossip)")
        return retlist
