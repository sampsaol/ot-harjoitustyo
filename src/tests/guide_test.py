import unittest
from generators.guide import Guide
from generators.quests import Quests


class TestClasses(unittest.TestCase):
    def setUp(self):
        self.classlist = ["Two-Handed Warrior", "Battlemage", "One-Handed Warrior",
                          "Stealth Archer", "Assassin", "Berserker", "Night Blade"]
        self.questlist = ["Dark Brotherhood", "The Companions",
                          "The Thieves Guild", "The College of Winterhold"]
        self.allskills = ["Light Armor", "Heavy Armor", "One-Handed", "Two-Handed",
                          "Destruction", "Archery", "Block", "Sneak", "Illusion"]
        self.matchdict = {"Two-Handed Warrior": ["Two-Handed", "Heavy Armor", "Whiterun"], "Battlemage": ["Destruction", "Light Armor", "Winterhold"],
                          "One-Handed Warrior": ["One-Handed", "Heavy Armor- and Block", "Whiterun"], "Stealth Archer": ["Archery", "Sneak", "Riften"],
                          "Assassin": ["One-Handed", "Sneak", "Windhelm (speak to innkeepers for gossip)"], "Berserker": ["One-Handed", "Heavy Armor", "Whiterun"],
                          "Night Blade": ["Illusion- and One-Handed", "Sneak", "Windhelm (speak to innkeepers for gossip)"]}

    def test_constructor_creates_right_lists(self):
        testguide = Guide(self.classlist[0], self.questlist[1])
        helplist = []
        for i in testguide._armorlist:
            helplist.append(i)
        for i in testguide._attacklist:
            helplist.append(i)
        for i in testguide._misclist:
            helplist.append(i)
        self.assertEqual(helplist, self.allskills)

    def test_right_guide_is_given(self):
        helplist = []
        retdict = {}
        for i in self.classlist:
            quest = Quests(i)
            val = quest.primary_questline()
            helplist.append((i, val))
        for i in helplist:
            val = Guide(i[0], i[1])
            retdict[i[0]] = val.generate_guide()
        self.assertEqual(retdict, self.matchdict)
