class Guide:
    """A class for generating a guide for the player
    based on the playstyle he is using and the questline he is doing
    """

    def __init__(self, playclass, quest):
        """A constructor where the major skills the player should level are defined

        Args:
            playclass (_str_): the playstyle that the character uses
            quest (_str_): the questline the character is supposed to do first
        """
        self._armorlist = ["Light Armor", "Heavy Armor"]
        self._attacklist = ["One-Handed", "Two-Handed",
                            "Destruction", "Archery", "Block"]
        self._misclist = ["Sneak", "Illusion"]
        self._playclass = playclass
        self._quest = quest

    def generate_guide(self):
        """A function for generating the guide for the character. The major skills
        that the player should first level are based on the playstyle he is using.
        The function also adds to the guide the startpoint where the players questline starts.

        Returns:
            _list_: a list that consists of the major skills that
            should be leveled and the startpoint of the characters questline
        """
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

        if self._quest == "The College of Winterhold":
            retlist.append("Winterhold")
        elif self._quest == "The Companions":
            retlist.append("Whiterun")
        elif self._quest == "The Thieves Guild":
            retlist.append("Riften")
        else:
            retlist.append("Windhelm (speak to innkeepers for gossip)")
        return retlist
